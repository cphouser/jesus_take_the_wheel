# jesus_take_the_wheel
whisper voices from one session to another

## installing (assuming linux system, tested on ubuntu 20.04)
make sure xclip, python3, venv (more?) are installed. 
copy this directory (clone the repository) into wherever you'd like the resources for this program to live. 
`cd` into the project directory. run `./install.sh`. 
this will create a .desktop file for an application called "TheWheel" in your `~/.local/share/applications` directory 
and an executable called `jesus` in this (the current working) directory.
this executable can be moved to `~/.local/bin` or another directory on your PATH for easy access.

## use
1. run _TheWheel_ in the session you would like to remotely control. Generally this is a graphical login session.
2. run _jesus_ in another session, such as a non-graphical ssh session. 
keyboard strokes captured in the _jesus_ session will be sent to _TheWheel_ session. 
Backspace, Tab, Arrow Keys, Enter, and CTRL-V (as paste) are supported in additon to standard printable characters.
Escape closes the program.

Communication happens over a socket created and managed by _TheWheel_, so this can be left running while _jesus_
 invoked is whenever needed.
