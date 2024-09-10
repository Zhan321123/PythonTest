@echo off
   setlocal enabledelayedexpansion

   for /f "tokens=1* delims==" %%a in ('pip freeze') do (
     set pkg_name=%%a
     if "!pkg_name!" neq "-e" (
       pip uninstall -y "!pkg_name!"
     )
   )