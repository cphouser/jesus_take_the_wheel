#!/usr/bin/env python3

import curses
import os
import socket
import sys
import time
from pathlib import Path

from pynput.keyboard import Key, Controller, Listener


#reverses = {ordinal: name for name, ordinal in vars(curses).items() 
#        if isinstance(ordinal, int) and "KEY_" in name}
#print(reverses)

CONTROL = {
    9: Key.tab,
    13: Key.enter,
    22: None, #control-v
    27: None, #escape
    258: Key.down,
    259: Key.up,
    260: Key.left,
    261: Key.right,
    263: Key.backspace,
}

keyboard = Controller()

server_address = Path(os.environ.get("XDG_RUNTIME_DIR", "/tmp")
        ) / "psychokinetic_plane.socket"

# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the port
sys.stderr.write('starting up on %s' % server_address)
sock.bind(bytes(server_address))

sock.listen(1)

while True:
    sys.stderr.write('waiting for a connection')
    try:
        connection, client_address = sock.accept()
        while (data := connection.recv(4)):
            ordinal = int.from_bytes(data, "big")
            if (pynput_key := CONTROL.get(ordinal)):
                character = pynput_key
            else:
                character = chr(ordinal)
            keyboard.press(character)
            time.sleep(0.01)
            keyboard.release(character)
    finally:
        try:
            connection.close()
        except NameError:
            sock.close()
