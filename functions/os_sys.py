import os
import subprocess as sp

path = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_calculator():
    sp.Popen(path['calculator'])