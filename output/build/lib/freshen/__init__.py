from . import modules, reginstall
import os
import ctypes
import sys
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, os.path.join(
    __file__, '..', 'reginstall.py'), None, 1)
