# -*- coding: utf-8 -*-


"""templ.warn: sends messages directly to terminal."""

import os
import sys

def warn(message):
    # write to /dev/tty to allow stdout to be redirected
    os.system("echo -n " + message + " >/dev/tty")
    sys.stdout.flush()
