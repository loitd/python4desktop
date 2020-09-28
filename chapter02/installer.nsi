;NSIS Modern User Interface
;Modified by Tran Duc Loi based on NSIS Modern User Interface Written by Joost Verburg
;Python For Desktop Chapter 02 Book
;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

;--------------------------------
;General

  ;Name and file
  Name "Python4Desktop GUI Downloader"
  OutFile "guidownloader-setup-1.0-x64.exe"
  Unicode True

  ;Default installation folder
  InstallDir "$LOCALAPPDATA\Python4Desktop\GUI Downloader"
  
  ;Get installation folder from registry if available
  InstallDirRegKey HKCU "Software\Python4Desktop GUI Downloader" ""

  ;Request application privileges for Windows Vista
  RequestExecutionLevel user

;--------------------------------
;Variables

  Var StartMenuFolder

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING

;--------------------------------
;Pages

  !insertmacro MUI_PAGE_LICENSE "LICENSE"
  !insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  
  ;Start Menu Folder Page Configuration
  !define MUI_STARTMENUPAGE_REGISTRY_ROOT "HKCU" 
  !define MUI_STARTMENUPAGE_REGISTRY_KEY "Software\Python4Desktop GUI Downloader" 
  !define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "Tran Duc Loi Python4Desktop"
  
  !insertmacro MUI_PAGE_STARTMENU Application $StartMenuFolder
  
  !insertmacro MUI_PAGE_INSTFILES
  
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES

;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections: 

SectionGroup /e "All" SEC_GROUP

    Section "Python4Desktop GUI Downloader" SEC_PIV
        SectionIn RO
        SetOutPath "$INSTDIR"
        
        ;ADD YOUR OWN FILES HERE...: 
        File /r "dist\guidownloader\*"
        
        ;Store installation folder
        WriteRegStr HKCU "Python4Desktop GUI Downloader" "" $INSTDIR
        
        ;Create uninstaller
        WriteUninstaller "$INSTDIR\Uninstall.exe"
        
        !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
            ;Create shortcuts
            CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
            CreateShortcut "$SMPROGRAMS\$StartMenuFolder\GUI Downloader.lnk" "$INSTDIR\guidownloader.exe"
            CreateShortcut "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
        !insertmacro MUI_STARTMENU_WRITE_END

    SectionEnd

    ;Section "optional" SEC_OPT
    ;SectionEnd

SectionGroupEnd

;--------------------------------
;Descriptions

  ;Language strings
  LangString DESC_SEC_PIV ${LANG_ENGLISH} "Python4Desktop GUI Downloader"

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SEC_PIV} $(DESC_SEC_PIV)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END
 
;--------------------------------
;Uninstaller Section

Section "Uninstall"

  ;ADD YOUR OWN FILES HERE...

  Delete "$INSTDIR\Uninstall.exe"

  RMDir "$INSTDIR"
  
  !insertmacro MUI_STARTMENU_GETFOLDER Application $StartMenuFolder
    
  Delete "$SMPROGRAMS\$StartMenuFolder\Uninstall.lnk"
  Delete "$SMPROGRAMS\$StartMenuFolder\GUI Downloader.lnk"
  RMDir "$SMPROGRAMS\$StartMenuFolder"
  
  DeleteRegKey /ifempty HKCU "Software\Python4Desktop GUI Downloader"
  DeleteRegKey /ifempty HKCU "Python4Desktop GUI Downloader"

SectionEnd

