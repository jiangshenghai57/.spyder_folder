import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"],
                     "excludes": ["tkinter"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "libor_scraper",
      version = "0.1",
      description = "",
      options = {"build_exe": build_exe_options},
      executables = [Executable("C:\\Users\\Shenghai.ETIDOMAIN\\.spyder-py3\\libor_scraper\\libor_scraper.py", base = base)]
      )
