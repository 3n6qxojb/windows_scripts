:: This file should be burned in to a CDFS partition to autolaunch a file from a removable drive

@echo off

 FOR %%l in (a b c d e f g h i j k l m n o p q r s t u v w x y z) DO (
  IF EXIST %%l:\autolaunch.bat (
   start "Titlebar" "%%l:\autolaunch.bat"
   goto end_global
   )
  )
 :end_global
 exit
