"""
TeaChimer-v2.0.0
(C) 2023-2024 cyber-yuito723
"""

import sys
sys.dont_write_bytecode = True

import flet as ft
import time

with open("./system/starting.txt", "r", encoding = "utf-8") as f:
    starting_txt = f.read()
print(starting_txt)


time.sleep(3)

port = 23080