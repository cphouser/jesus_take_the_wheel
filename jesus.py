#!/usr/bin/env python3

import os
import socket
import sys
import curses
from pathlib import Path

import pyperclip

server_address = Path(os.environ.get("XDG_RUNTIME_DIR", "/tmp")) / "psychokinetic_plane.socket"

header = "Connected to Socket. Last_Pressed: [{}] {}"

def print_status(window, arg1=None, arg2=None):
    window.clear()
    window.refresh()
    window.addstr(0, 0, header.format(arg1, arg2).center(curses.COLS))

def main(window):
    curses.nonl() # Send Enter
    window.clear()

    # Create a UDS socket
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(bytes(server_address))

    print_status(window)
    try:
        while True:
            character = window.getch()
            window.clear()
            if character == 27: # ESCAPE
                break
            elif character == 22: # CONTROL-v
                clipboard = pyperclip.paste()
                print_status(window, "PASTE", clipboard)
                for char in clipboard:
                    sock.sendall(ord(char).to_bytes(4, "big"))
            else:
                print_status(window, character, chr(character))
            sock.sendall(character.to_bytes(4, "big"))
    finally:
        sock.detach()

curses.wrapper(main)



