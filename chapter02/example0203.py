#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# -------------------------------------
# File: chapter02\example0203.py
# Description: This is a short description
# Author: loitd - WWW: https://github.com/loitd
# ----------
# HISTORY:
# Date      	By    	Comments
# ----------	------	---------------
# 2020-09-18	loitd	Initialized
# -------------------------------------

import os, time
from lutils import utils
from tkinter import Tk, messagebox, TOP, BOTTOM, RIGHT, LEFT, YES, NO, X, Y, filedialog, ttk, Frame, Label, Entry, Button, HORIZONTAL, PhotoImage
from queue import Queue
from functools import partial
from requests import get, exceptions
from shutil import copyfileobj
from threading import Thread, Lock

def maingui():
    root = Tk()
    root.iconbitmap("py4de.ico")
    root.title("Python4Desktop Downloader")
    # ----url
    row = Frame(root)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lbl = Label(row, width=10, text="URL:")
    lbl.pack(side=LEFT)
    ent = Entry(row, width=88)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    ent.insert(0, testurl)
    # save file name button
    row = Frame(root)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lbl2 = Label(row, width=10, text="Save as:")
    lbl2.pack(side=LEFT)
    btnSave = Button(row, text="...", command=saveFileAs)
    btnSave.pack(side=RIGHT, expand=NO)
    lblSave = Label(row, width=88, text="Please select destination file name/path")
    lblSave.pack(side=RIGHT, expand=YES, fill=X)
    btnSave['command'] = partial(saveFileAs, lblSave)
    # ProgressBar
    rowProgress = Frame(root)
    rowProgress.pack(side=TOP, fill=X, padx=5, pady=5)
    lbl = Label(rowProgress, width=10, text="PROGRESS")
    lbl.pack(side=LEFT)
    progress = ttk.Progressbar(rowProgress, orient=HORIZONTAL, length=100, mode="determinate")
    progress.pack(side=RIGHT, expand=YES, fill=X)
    # Buttons
    btnFrame = Frame(root)
    btnFrame.pack(side=BOTTOM, expand=YES, fill=X)
    # Exit
    imgexit = PhotoImage(file=r"imgexit.gif").subsample(3)
    btnExit = Button(btnFrame, text="Exit", image=imgexit, compound=LEFT, command=(lambda root=root: exit(root)))
    btnExit.image = imgexit # is a must to keep a reference
    btnExit.pack(side=LEFT, padx=5, pady=5)
    # Download
    imgdl = PhotoImage(file=r"imgdld.gif").subsample(3)
    btnDld = Button(btnFrame, text="DOWNLOAD", compound=LEFT)
    btnDld['image'] = imgdl # is a must to keep a reference
    btnDld['command'] = partial(start_download, btnDld, ent, progress, lblSave)
    btnDld.pack(side=RIGHT, padx=5, pady=5)
    # ---loops
    cmdloop(root, cmdq)
    root.mainloop()

def saveFileAs(lblSave):
    files = [('All Files', '*.*'), ('Python Files', '*.py'), ('Text Document', '*.txt')] 
    filename = filedialog.asksaveasfile(filetypes = files, defaultextension = files) 
    # print(filename, filename.name)
    cmdq.put(( updateFilename, (lblSave, filename.name), {} ))
    return filename

def cmdloop(root, cmdq):
    try:
        if not cmdq.empty():
            f,a,k = cmdq.get_nowait()
            f(*a, **k)
    except Exception as e:
        raise(e)
        # pass
    root.after(200, cmdloop, root, cmdq)

def start_download(btnDld, ent, progress, lblSave):
    try:
        # cmdq.put((messagebox.showinfo, ('title', 'message'), {}))
        cmdq.put(( tonggle_button, (btnDld, ), {} ))
        # get some inputs
        url = ent.get()
        filename = lblSave['text']
        if url and url != "": mainq.put_nowait(url)
        utils.printlog("Queue size: {0}".format(mainq.qsize()))
        lk1 = Lock()
        # start DOWNLOAD thread
        dld = Thread(name="DOWNLOAD", target=download, daemon=True, args=(filename, lk1, btnDld))
        dld.start()
        # start STATUS thread
        stt = Thread(name="STATUS", target=status, daemon=True, args=(filename, lk1, progress))
        stt.start()
        # Additional
        # JOINING - Blocking
        # dld.join()
        # stt.join()
        # mainq.join() ## block until all tasks are done -> q.task_done()
    except Exception as e:
        raise(e)
    finally:
        pass

def exit(root):
    EXITFLAG = 1
    root.quit()

def download(filename, lk1, btnDld):
    lk1.acquire() #acquire the lock before status can
    try:
        if mainq.empty(): return 0
        url = mainq.get(1, 1) #block=True, timeout=None
        # filename = url.split('/')[-1]
        utils.printlog("Start download: {0}".format(url))
        with get(url, stream=True, timeout=3) as r:
            filesize = r.headers['Content-length'].encode("utf8")
            utils.printlog("Download size: {0} kilobytes".format(filesize))
            with open(filename+".tmp", 'wb') as fh:
                fh.write(filesize)
            with open(filename, 'wb') as f:
                lk1.release()
                copyfileobj(r.raw, f)
        return filename, filesize
    except exceptions.ConnectionError as e:
        utils.printlog("Error during connect to URL: {0}".format(e))
        # messagebox.showerror("Error", "Connection to {0} timeout. Please check your internet connection.".format(url))
        return 0,0
    except exceptions.MissingSchema as e:
        utils.printlog("Invalid URL: {0}".format(e))
    except Exception as e:
        raise(e)
    finally: 
        utils.printlog("Finalizing with qsize: {0}".format(mainq.qsize()))
        if lk1.locked(): lk1.release()
        cmdq.put(( tonggle_button, (btnDld, ), {} )) #toggle the button

def status(filename, lk1, progress):
    lk1.acquire()
    try:
        with open(filename+".tmp", "rb") as fh:
            filesize = fh.read()
            filesize = int(filesize)
            utils.printlog("Got filesize = {0}".format(filesize))
        os.remove(filename+".tmp")
        while 1: #Return true if the lock is acquired
            thesize = os.stat(filename).st_size
            if thesize == filesize:
                utils.printlog("Download finished")
                if lk1.locked(): lk1.release()
                cmdq.put(( setProgress, (progress, 100), {} )) #set progress
                break 
            else:
                percent = (thesize * 100 / filesize)
                utils.printwait("{0}/{1} - Percentage: {2:.2f}% complete".format(thesize, filesize, percent), 1)
                cmdq.put(( setProgress, (progress, percent), {} )) #set progress
    except FileNotFoundError as e:
        utils.printlog("File not found")
        return 0
    except Exception as e:
        raise(e)
    finally:
        if lk1.locked(): lk1.release()

def tonggle_button(btn):
    utils.printlog("Current BTN state is: {0}".format(btn['state']))
    if btn['state'] != 'disabled':
        btn['state'] = 'disabled'
    else:
        btn['state'] = 'normal'

def setProgress(progressBar, percent):
    progressBar['value'] = percent

def updateFilename(lbl, filename):
    lbl['text'] = filename

if __name__ == "__main__":
    testurl = "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_5MG.mp3"
    testurl = "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_1MG.mp3"
    testurl = "https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_700KB.mp3"
    filename = "file_example_MP3_1MG.mp3"
    filename = "file_example_MP3_700KB.mp3"
    EXITFLAG = 0
    cmdq = Queue()
    mainq = Queue(1)
    # Start main gui thread
    gui = Thread(name="GUI", target=maingui, daemon=True, args=())
    gui.start()
    # Join the main thread
    gui.join()