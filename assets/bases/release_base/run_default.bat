@echo off


cd %~dp0


set exe_file="%CD%\UnrealAutoModCLI.exe"
set settings_json="%CD%\default\settings.json"
set arg=test_mods_all
set command=%exe_file% %settings_json% %arg%


rem echo %command%
%command%


rem pause


exit /b