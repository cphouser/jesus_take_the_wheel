
set -ex

APP_DIR=$PWD
VENV_BIN=$APP_DIR/.venv/bin/python 
python3 -m venv .venv
.venv/bin/python3 -m pip install -r requirements.txt
echo -e "[Desktop Entry]\nType=Application\nName=TheWheel\nExec=xterm -e \"$VENV_BIN $APP_DIR/the_wheel.py\"" \
	> "/home/$LOGNAME/.local/share/applications/the-wheel.desktop"
echo -e "#!/usr/bin/sh\n\"$VENV_BIN\" $APP_DIR/jesus.py" > ./jesus
chmod +x jesus ~/.local/share/applications/the-wheel.desktop




