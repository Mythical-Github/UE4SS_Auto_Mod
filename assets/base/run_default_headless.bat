@echo off

cd /D %~dp0

set exe_file=%CD%\UnrealAutoModCLI.exe
set settings_json=%CD%\default\settings.json
set arg=test_mods_all
set command=%exe_file% %settings_json% %arg%

start "" /B mshta.exe vbscript:(CreateObject("WScript.Shell").Run("cmd /c ""%command%""",0))(Window.Close)

exit /b