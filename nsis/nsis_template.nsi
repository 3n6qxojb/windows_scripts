#N SIS wiki is here: https://nsis.sourceforge.io/Main_Page

# add dos command plugin
!addplugindir ".\addplugindir"

# define the name of the exe file
Outfile ""

# define the directory to install to
InstallDir ""
 
# default section
Section
 
# run a windows command
ExecCmd::exec ''

# define the output path for this file
SetOutPath $INSTDIR
 
# define what to install and place it in the output path
File file.name

#create a shortcut
createShortCut "" "" "" ""
 
SectionEnd