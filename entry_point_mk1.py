import os, sys, time
import traceback

import ctypes
from typing import NamedTuple

from datetime import datetime
import pytz




def enable_virtual_terminal_processing():
    if sys.platform.system() == "Windows":
        kernel32 = ctypes.WinDLL('kernel32')
        hStdOut = kernel32.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        kernel32.GetConsoleMode(hStdOut, ctypes.byref(mode))
        mode.value |= 4  # ENABLE_VIRTUAL_TERMINAL_PROCESSING is 0x0004
        kernel32.SetConsoleMode(hStdOut, mode)

class _Colors(NamedTuple):
    green: str = "\033[92m"
    red: str = "\033[91m"
    yellow: str = "\033[93m"
    gray: str = "\033[90m"
    reset: str = "\033[0m"
    
COLORS = _Colors()

def prn(color: str, s: str):
    print(f"{color}{s}{COLORS.reset}")

def date_demo():
    kyiv_tz = pytz.timezone('Europe/Kyiv')
    kyiv_time = datetime.now(kyiv_tz)
    print(kyiv_time.strftime('%d_%m_%y  (%Y) %H:%M:%S'))

def read_file_lines(filepath: str):
    with open(filepath, 'r') as file:
        for line in file:
            pass
        
def main():
    try:
        prn(COLORS.yellow, "<< BASIC MAIN TEMPLATE >>")
        
        date_demo()
        
    except Exception as e:
        print()
        prn(COLORS.gray,f"CDW: {os.getcwd()}")
        prn(COLORS.red, f"Main Exception:")
        print(f"  {e}\n")
        traceback.print_exc()
        
if __name__ == "__main__":
    main()
