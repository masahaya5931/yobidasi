"""
TeaChimer-v1.0.0
(C) 2023 cyber-yuito723


This file is part of TeaChimer.

TeaChimer is free software: you can redistribute it and/or modify it under the terms of
the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

TeaChimer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with TeaChimer.
If not, see <https://www.gnu.org/licenses/>.
"""

import tkinter as tk
import tkinter.ttk as ttk
import winsound
import settings

class Main():
    def __init__(self, master):
        self.master = master
        self.master.attributes("-fullscreen", True)
        self.master.iconbitmap("./system/logo-1_icon.ico")
        self.master.title(f"TeaChimer-{version}_MAIN")
        self.master.configure(background = "white")
        self.master.focus_force()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background = "white")
        style.configure("TLabel", font = ("Yu Gothic UI", 15), anchor = "center", background = "white")
        style.configure("startup_ver.TLabel", font = ("Yu Gothic UI", 25, "bold"), anchor = "center", background = "white")
        style.configure("logo.TLabel", background = "white")
        style.configure("notice.TLabel", font = ("Yu Gothic UI", 30, "bold"), anchor = "center", background = "white")
        style.configure("TNotebook", background = "white")
        style.configure("TNotebook.Tab", width = 300, font = ("Yu Gothic UI", 35, "bold"), anchor = "center", background = "whitesmoke")
        style.configure("TButton", font = ("Yu Gothic UI", 25, "bold"), background = "whitesmoke")
        style.map("TNotebook.Tab", background = [("selected", "white")])
        style.map("TButton", background = [("active", "whitesmoke"), ("disabled", "lightgray")])

        self.startup()

        self.header()
        self.main()

        self.master.bind("<Control-q>", self.exit)

    def startup(self):
        startup = tk.Toplevel()
        startup.attributes("-fullscreen", True)
        startup.attributes("-topmost", True)
        startup.attributes("-alpha", 0.75)
        startup.iconbitmap("./system/logo-1_icon.ico")
        startup.title(f"TeaChimer-{version}_STARTUP")
        startup.configure(background = "whitesmoke")

        startup.after(7000, startup.destroy)

        startup_frame = ttk.Frame(startup, style = "TFrame")
        startup_frame.place(x = (screen_width - 700) / 2, y = (screen_height - 150) / 2, width = 700, height = 150)

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(startup_frame, image = logo, style = "logo.TLabel")
        logo_label.place(x = 0, y = 0, width = 300 + 20, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}"
        ver_label = ttk.Label(startup_frame, text = ver, style = "startup_ver.TLabel")
        ver_label.place(x = 0, y = 100, width = 300 + 20, height = 150 - 100)

        text = "TeaChimerはオープンソースソフトウェアであり、\nGNU General Public License v3.0に基づいて\n再配布したり改変したりできます\n(C) 2023 cyber-yuito723\n終了：「Ctrl」キー＋「Q」キー"
        text_label = ttk.Label(startup_frame, text = text, style = "TLabel")
        text_label.place(x = 300 + 20, y = 0, width = 700 - 300 - 20, height = 150)

    def header(self):
        header = ttk.Frame(style = "TFrame")
        header.place(x = 0, y = 0, width = screen_width, height = 100)

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(header, image = logo, style = "logo.TLabel")
        logo_label.place(x = 10, y = 0, width = 300, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}\n{settings.school_name}\n{settings.admin_name}"
        ver_label = ttk.Label(header, text = ver, style = "TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = "呼びたい先生のボタンを押してください"
        text_label = ttk.Label(header, text = text, style = "notice.TLabel")
        text_label.place(x = 10 + 300 + 10 + 300, y = 0, width = screen_width - 10 - 300 - 10 - 300, height = 100)

    def main(self):
        self.main = ttk.Notebook(self.master, style = "TNotebook")
        self.main.place(x = 0, y = 100, width = screen_width, height = screen_height - 100)

        self.main_tab_0()
        self.main_tab_1()
        self.main_tab_2()
        self.main_tab_3()
        self.main_tab_4()
        self.main_tab_5()
        self.main_tab_6()
        self.main_tab_7()
        self.main_tab_8()
        self.main_tab_9()

    def main_tab_0(self):
        main_tab_0 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_0, text = settings.main_tab_0_n)

        ttk.Button(main_tab_0, text = settings.t0_0_0_n, state = settings.t0_0_0_s, command = lambda: self.confirm(settings.t0_0_0_n, settings.t0_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_1_0_n, state = settings.t0_1_0_s, command = lambda: self.confirm(settings.t0_1_0_n, settings.t0_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_2_0_n, state = settings.t0_2_0_s, command = lambda: self.confirm(settings.t0_2_0_n, settings.t0_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_3_0_n, state = settings.t0_3_0_s, command = lambda: self.confirm(settings.t0_3_0_n, settings.t0_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_4_0_n, state = settings.t0_4_0_s, command = lambda: self.confirm(settings.t0_4_0_n, settings.t0_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_0, text = settings.t0_0_1_n, state = settings.t0_0_1_s, command = lambda: self.confirm(settings.t0_0_1_n, settings.t0_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_1_1_n, state = settings.t0_1_1_s, command = lambda: self.confirm(settings.t0_1_1_n, settings.t0_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_2_1_n, state = settings.t0_2_1_s, command = lambda: self.confirm(settings.t0_2_1_n, settings.t0_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_3_1_n, state = settings.t0_3_1_s, command = lambda: self.confirm(settings.t0_3_1_n, settings.t0_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_4_1_n, state = settings.t0_4_1_s, command = lambda: self.confirm(settings.t0_4_1_n, settings.t0_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_0, text = settings.t0_0_2_n, state = settings.t0_0_2_s, command = lambda: self.confirm(settings.t0_0_2_n, settings.t0_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_1_2_n, state = settings.t0_1_2_s, command = lambda: self.confirm(settings.t0_1_2_n, settings.t0_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_2_2_n, state = settings.t0_2_2_s, command = lambda: self.confirm(settings.t0_2_2_n, settings.t0_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_3_2_n, state = settings.t0_3_2_s, command = lambda: self.confirm(settings.t0_3_2_n, settings.t0_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_4_2_n, state = settings.t0_4_2_s, command = lambda: self.confirm(settings.t0_4_2_n, settings.t0_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_0, text = settings.t0_0_3_n, state = settings.t0_0_3_s, command = lambda: self.confirm(settings.t0_0_3_n, settings.t0_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_1_3_n, state = settings.t0_1_3_s, command = lambda: self.confirm(settings.t0_1_3_n, settings.t0_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_2_3_n, state = settings.t0_2_3_s, command = lambda: self.confirm(settings.t0_2_3_n, settings.t0_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_3_3_n, state = settings.t0_3_3_s, command = lambda: self.confirm(settings.t0_3_3_n, settings.t0_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_4_3_n, state = settings.t0_4_3_s, command = lambda: self.confirm(settings.t0_4_3_n, settings.t0_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_0, text = settings.t0_0_4_n, state = settings.t0_0_4_s, command = lambda: self.confirm(settings.t0_0_4_n, settings.t0_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_1_4_n, state = settings.t0_1_4_s, command = lambda: self.confirm(settings.t0_1_4_n, settings.t0_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_2_4_n, state = settings.t0_2_4_s, command = lambda: self.confirm(settings.t0_2_4_n, settings.t0_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_3_4_n, state = settings.t0_3_4_s, command = lambda: self.confirm(settings.t0_3_4_n, settings.t0_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_0, text = settings.t0_4_4_n, state = settings.t0_4_4_s, command = lambda: self.confirm(settings.t0_4_4_n, settings.t0_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_0.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_0.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_0.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_0.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_0.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_0.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_0.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_0.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_0.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_0.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def main_tab_1(self):
        main_tab_1 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_1, text = settings.main_tab_1_n)

        ttk.Button(main_tab_1, text = settings.t1_0_0_n, state = settings.t1_0_0_s, command = lambda: self.confirm(settings.t1_0_0_n, settings.t1_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_1_0_n, state = settings.t1_1_0_s, command = lambda: self.confirm(settings.t1_1_0_n, settings.t1_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_2_0_n, state = settings.t1_2_0_s, command = lambda: self.confirm(settings.t1_2_0_n, settings.t1_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_3_0_n, state = settings.t1_3_0_s, command = lambda: self.confirm(settings.t1_3_0_n, settings.t1_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_4_0_n, state = settings.t1_4_0_s, command = lambda: self.confirm(settings.t1_4_0_n, settings.t1_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_1, text = settings.t1_0_1_n, state = settings.t1_0_1_s, command = lambda: self.confirm(settings.t1_0_1_n, settings.t1_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_1_1_n, state = settings.t1_1_1_s, command = lambda: self.confirm(settings.t1_1_1_n, settings.t1_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_2_1_n, state = settings.t1_2_1_s, command = lambda: self.confirm(settings.t1_2_1_n, settings.t1_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_3_1_n, state = settings.t1_3_1_s, command = lambda: self.confirm(settings.t1_3_1_n, settings.t1_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_4_1_n, state = settings.t1_4_1_s, command = lambda: self.confirm(settings.t1_4_1_n, settings.t1_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_1, text = settings.t1_0_2_n, state = settings.t1_0_2_s, command = lambda: self.confirm(settings.t1_0_2_n, settings.t1_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_1_2_n, state = settings.t1_1_2_s, command = lambda: self.confirm(settings.t1_1_2_n, settings.t1_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_2_2_n, state = settings.t1_2_2_s, command = lambda: self.confirm(settings.t1_2_2_n, settings.t1_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_3_2_n, state = settings.t1_3_2_s, command = lambda: self.confirm(settings.t1_3_2_n, settings.t1_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_4_2_n, state = settings.t1_4_2_s, command = lambda: self.confirm(settings.t1_4_2_n, settings.t1_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_1, text = settings.t1_0_3_n, state = settings.t1_0_3_s, command = lambda: self.confirm(settings.t1_0_3_n, settings.t1_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_1_3_n, state = settings.t1_1_3_s, command = lambda: self.confirm(settings.t1_1_3_n, settings.t1_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_2_3_n, state = settings.t1_2_3_s, command = lambda: self.confirm(settings.t1_2_3_n, settings.t1_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_3_3_n, state = settings.t1_3_3_s, command = lambda: self.confirm(settings.t1_3_3_n, settings.t1_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_4_3_n, state = settings.t1_4_3_s, command = lambda: self.confirm(settings.t1_4_3_n, settings.t1_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_1, text = settings.t1_0_4_n, state = settings.t1_0_4_s, command = lambda: self.confirm(settings.t1_0_4_n, settings.t1_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_1_4_n, state = settings.t1_1_4_s, command = lambda: self.confirm(settings.t1_1_4_n, settings.t1_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_2_4_n, state = settings.t1_2_4_s, command = lambda: self.confirm(settings.t1_2_4_n, settings.t1_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_3_4_n, state = settings.t1_3_4_s, command = lambda: self.confirm(settings.t1_3_4_n, settings.t1_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_1, text = settings.t1_4_4_n, state = settings.t1_4_4_s, command = lambda: self.confirm(settings.t1_4_4_n, settings.t1_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_1.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_1.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_1.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_1.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_1.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_1.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_1.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_1.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_1.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_1.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def main_tab_2(self):
        main_tab_2 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_2, text = settings.main_tab_2_n)

        ttk.Button(main_tab_2, text = settings.t2_0_0_n, state = settings.t2_0_0_s, command = lambda: self.confirm(settings.t2_0_0_n, settings.t2_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_1_0_n, state = settings.t2_1_0_s, command = lambda: self.confirm(settings.t2_1_0_n, settings.t2_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_2_0_n, state = settings.t2_2_0_s, command = lambda: self.confirm(settings.t2_2_0_n, settings.t2_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_3_0_n, state = settings.t2_3_0_s, command = lambda: self.confirm(settings.t2_3_0_n, settings.t2_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_4_0_n, state = settings.t2_4_0_s, command = lambda: self.confirm(settings.t2_4_0_n, settings.t2_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_2, text = settings.t2_0_1_n, state = settings.t2_0_1_s, command = lambda: self.confirm(settings.t2_0_1_n, settings.t2_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_1_1_n, state = settings.t2_1_1_s, command = lambda: self.confirm(settings.t2_1_1_n, settings.t2_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_2_1_n, state = settings.t2_2_1_s, command = lambda: self.confirm(settings.t2_2_1_n, settings.t2_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_3_1_n, state = settings.t2_3_1_s, command = lambda: self.confirm(settings.t2_3_1_n, settings.t2_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_4_1_n, state = settings.t2_4_1_s, command = lambda: self.confirm(settings.t2_4_1_n, settings.t2_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_2, text = settings.t2_0_2_n, state = settings.t2_0_2_s, command = lambda: self.confirm(settings.t2_0_2_n, settings.t2_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_1_2_n, state = settings.t2_1_2_s, command = lambda: self.confirm(settings.t2_1_2_n, settings.t2_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_2_2_n, state = settings.t2_2_2_s, command = lambda: self.confirm(settings.t2_2_2_n, settings.t2_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_3_2_n, state = settings.t2_3_2_s, command = lambda: self.confirm(settings.t2_3_2_n, settings.t2_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_4_2_n, state = settings.t2_4_2_s, command = lambda: self.confirm(settings.t2_4_2_n, settings.t2_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_2, text = settings.t2_0_3_n, state = settings.t2_0_3_s, command = lambda: self.confirm(settings.t2_0_3_n, settings.t2_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_1_3_n, state = settings.t2_1_3_s, command = lambda: self.confirm(settings.t2_1_3_n, settings.t2_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_2_3_n, state = settings.t2_2_3_s, command = lambda: self.confirm(settings.t2_2_3_n, settings.t2_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_3_3_n, state = settings.t2_3_3_s, command = lambda: self.confirm(settings.t2_3_3_n, settings.t2_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_4_3_n, state = settings.t2_4_3_s, command = lambda: self.confirm(settings.t2_4_3_n, settings.t2_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_2, text = settings.t2_0_4_n, state = settings.t2_0_4_s, command = lambda: self.confirm(settings.t2_0_4_n, settings.t2_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_1_4_n, state = settings.t2_1_4_s, command = lambda: self.confirm(settings.t2_1_4_n, settings.t2_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_2_4_n, state = settings.t2_2_4_s, command = lambda: self.confirm(settings.t2_2_4_n, settings.t2_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_3_4_n, state = settings.t2_3_4_s, command = lambda: self.confirm(settings.t2_3_4_n, settings.t2_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_2, text = settings.t2_4_4_n, state = settings.t2_4_4_s, command = lambda: self.confirm(settings.t2_4_4_n, settings.t2_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_2.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_2.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_2.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_2.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_2.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_2.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_2.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_2.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_2.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_2.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def main_tab_3(self):
        main_tab_3 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_3, text = settings.main_tab_3_n)

        ttk.Button(main_tab_3, text = settings.t3_0_0_n, state = settings.t3_0_0_s, command = lambda: self.confirm(settings.t3_0_0_n, settings.t3_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_1_0_n, state = settings.t3_1_0_s, command = lambda: self.confirm(settings.t3_1_0_n, settings.t3_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_2_0_n, state = settings.t3_2_0_s, command = lambda: self.confirm(settings.t3_2_0_n, settings.t3_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_3_0_n, state = settings.t3_3_0_s, command = lambda: self.confirm(settings.t3_3_0_n, settings.t3_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_4_0_n, state = settings.t3_4_0_s, command = lambda: self.confirm(settings.t3_4_0_n, settings.t3_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_3, text = settings.t3_0_1_n, state = settings.t3_0_1_s, command = lambda: self.confirm(settings.t3_0_1_n, settings.t3_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_1_1_n, state = settings.t3_1_1_s, command = lambda: self.confirm(settings.t3_1_1_n, settings.t3_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_2_1_n, state = settings.t3_2_1_s, command = lambda: self.confirm(settings.t3_2_1_n, settings.t3_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_3_1_n, state = settings.t3_3_1_s, command = lambda: self.confirm(settings.t3_3_1_n, settings.t3_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_4_1_n, state = settings.t3_4_1_s, command = lambda: self.confirm(settings.t3_4_1_n, settings.t3_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_3, text = settings.t3_0_2_n, state = settings.t3_0_2_s, command = lambda: self.confirm(settings.t3_0_2_n, settings.t3_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_1_2_n, state = settings.t3_1_2_s, command = lambda: self.confirm(settings.t3_1_2_n, settings.t3_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_2_2_n, state = settings.t3_2_2_s, command = lambda: self.confirm(settings.t3_2_2_n, settings.t3_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_3_2_n, state = settings.t3_3_2_s, command = lambda: self.confirm(settings.t3_3_2_n, settings.t3_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_4_2_n, state = settings.t3_4_2_s, command = lambda: self.confirm(settings.t3_4_2_n, settings.t3_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_3, text = settings.t3_0_3_n, state = settings.t3_0_3_s, command = lambda: self.confirm(settings.t3_0_3_n, settings.t3_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_1_3_n, state = settings.t3_1_3_s, command = lambda: self.confirm(settings.t3_1_3_n, settings.t3_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_2_3_n, state = settings.t3_2_3_s, command = lambda: self.confirm(settings.t3_2_3_n, settings.t3_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_3_3_n, state = settings.t3_3_3_s, command = lambda: self.confirm(settings.t3_3_3_n, settings.t3_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_4_3_n, state = settings.t3_4_3_s, command = lambda: self.confirm(settings.t3_4_3_n, settings.t3_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_3, text = settings.t3_0_4_n, state = settings.t3_0_4_s, command = lambda: self.confirm(settings.t3_0_4_n, settings.t3_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_1_4_n, state = settings.t3_1_4_s, command = lambda: self.confirm(settings.t3_1_4_n, settings.t3_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_2_4_n, state = settings.t3_2_4_s, command = lambda: self.confirm(settings.t3_2_4_n, settings.t3_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_3_4_n, state = settings.t3_3_4_s, command = lambda: self.confirm(settings.t3_3_4_n, settings.t3_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_3, text = settings.t3_4_4_n, state = settings.t3_4_4_s, command = lambda: self.confirm(settings.t3_4_4_n, settings.t3_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_3.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_3.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_3.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_3.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_3.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_3.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_3.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_3.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_3.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_3.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def main_tab_4(self):
        main_tab_4 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_4, text = settings.main_tab_4_n)

        ttk.Button(main_tab_4, text = settings.t4_0_0_n, state = settings.t4_0_0_s, command = lambda: self.confirm(settings.t4_0_0_n, settings.t4_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_1_0_n, state = settings.t4_1_0_s, command = lambda: self.confirm(settings.t4_1_0_n, settings.t4_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_2_0_n, state = settings.t4_2_0_s, command = lambda: self.confirm(settings.t4_2_0_n, settings.t4_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_3_0_n, state = settings.t4_3_0_s, command = lambda: self.confirm(settings.t4_3_0_n, settings.t4_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_4_0_n, state = settings.t4_4_0_s, command = lambda: self.confirm(settings.t4_4_0_n, settings.t4_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_4, text = settings.t4_0_1_n, state = settings.t4_0_1_s, command = lambda: self.confirm(settings.t4_0_1_n, settings.t4_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_1_1_n, state = settings.t4_1_1_s, command = lambda: self.confirm(settings.t4_1_1_n, settings.t4_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_2_1_n, state = settings.t4_2_1_s, command = lambda: self.confirm(settings.t4_2_1_n, settings.t4_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_3_1_n, state = settings.t4_3_1_s, command = lambda: self.confirm(settings.t4_3_1_n, settings.t4_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_4_1_n, state = settings.t4_4_1_s, command = lambda: self.confirm(settings.t4_4_1_n, settings.t4_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_4, text = settings.t4_0_2_n, state = settings.t4_0_2_s, command = lambda: self.confirm(settings.t4_0_2_n, settings.t4_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_1_2_n, state = settings.t4_1_2_s, command = lambda: self.confirm(settings.t4_1_2_n, settings.t4_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_2_2_n, state = settings.t4_2_2_s, command = lambda: self.confirm(settings.t4_2_2_n, settings.t4_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_3_2_n, state = settings.t4_3_2_s, command = lambda: self.confirm(settings.t4_3_2_n, settings.t4_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_4_2_n, state = settings.t4_4_2_s, command = lambda: self.confirm(settings.t4_4_2_n, settings.t4_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_4, text = settings.t4_0_3_n, state = settings.t4_0_3_s, command = lambda: self.confirm(settings.t4_0_3_n, settings.t4_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_1_3_n, state = settings.t4_1_3_s, command = lambda: self.confirm(settings.t4_1_3_n, settings.t4_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_2_3_n, state = settings.t4_2_3_s, command = lambda: self.confirm(settings.t4_2_3_n, settings.t4_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_3_3_n, state = settings.t4_3_3_s, command = lambda: self.confirm(settings.t4_3_3_n, settings.t4_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_4_3_n, state = settings.t4_4_3_s, command = lambda: self.confirm(settings.t4_4_3_n, settings.t4_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_4, text = settings.t4_0_4_n, state = settings.t4_0_4_s, command = lambda: self.confirm(settings.t4_0_4_n, settings.t4_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_1_4_n, state = settings.t4_1_4_s, command = lambda: self.confirm(settings.t4_1_4_n, settings.t4_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_2_4_n, state = settings.t4_2_4_s, command = lambda: self.confirm(settings.t4_2_4_n, settings.t4_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_3_4_n, state = settings.t4_3_4_s, command = lambda: self.confirm(settings.t4_3_4_n, settings.t4_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_4, text = settings.t4_4_4_n, state = settings.t4_4_4_s, command = lambda: self.confirm(settings.t4_4_4_n, settings.t4_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_4.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_4.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_4.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_4.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_4.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_4.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_4.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_4.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_4.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_4.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def main_tab_5(self):
        main_tab_5 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_5, text = settings.main_tab_5_n)

        ttk.Button(main_tab_5, text = settings.t5_0_0_n, state = settings.t5_0_0_s, command = lambda: self.confirm(settings.t5_0_0_n, settings.t5_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_1_0_n, state = settings.t5_1_0_s, command = lambda: self.confirm(settings.t5_1_0_n, settings.t5_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_2_0_n, state = settings.t5_2_0_s, command = lambda: self.confirm(settings.t5_2_0_n, settings.t5_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_3_0_n, state = settings.t5_3_0_s, command = lambda: self.confirm(settings.t5_3_0_n, settings.t5_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_4_0_n, state = settings.t5_4_0_s, command = lambda: self.confirm(settings.t5_4_0_n, settings.t5_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_5, text = settings.t5_0_1_n, state = settings.t5_0_1_s, command = lambda: self.confirm(settings.t5_0_1_n, settings.t5_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_1_1_n, state = settings.t5_1_1_s, command = lambda: self.confirm(settings.t5_1_1_n, settings.t5_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_2_1_n, state = settings.t5_2_1_s, command = lambda: self.confirm(settings.t5_2_1_n, settings.t5_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_3_1_n, state = settings.t5_3_1_s, command = lambda: self.confirm(settings.t5_3_1_n, settings.t5_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_4_1_n, state = settings.t5_4_1_s, command = lambda: self.confirm(settings.t5_4_1_n, settings.t5_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_5, text = settings.t5_0_2_n, state = settings.t5_0_2_s, command = lambda: self.confirm(settings.t5_0_2_n, settings.t5_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_1_2_n, state = settings.t5_1_2_s, command = lambda: self.confirm(settings.t5_1_2_n, settings.t5_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_2_2_n, state = settings.t5_2_2_s, command = lambda: self.confirm(settings.t5_2_2_n, settings.t5_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_3_2_n, state = settings.t5_3_2_s, command = lambda: self.confirm(settings.t5_3_2_n, settings.t5_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_4_2_n, state = settings.t5_4_2_s, command = lambda: self.confirm(settings.t5_4_2_n, settings.t5_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_5, text = settings.t5_0_3_n, state = settings.t5_0_3_s, command = lambda: self.confirm(settings.t5_0_3_n, settings.t5_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_1_3_n, state = settings.t5_1_3_s, command = lambda: self.confirm(settings.t5_1_3_n, settings.t5_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_2_3_n, state = settings.t5_2_3_s, command = lambda: self.confirm(settings.t5_2_3_n, settings.t5_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_3_3_n, state = settings.t5_3_3_s, command = lambda: self.confirm(settings.t5_3_3_n, settings.t5_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_4_3_n, state = settings.t5_4_3_s, command = lambda: self.confirm(settings.t5_4_3_n, settings.t5_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_5, text = settings.t5_0_4_n, state = settings.t5_0_4_s, command = lambda: self.confirm(settings.t5_0_4_n, settings.t5_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_1_4_n, state = settings.t5_1_4_s, command = lambda: self.confirm(settings.t5_1_4_n, settings.t5_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_2_4_n, state = settings.t5_2_4_s, command = lambda: self.confirm(settings.t5_2_4_n, settings.t5_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_3_4_n, state = settings.t5_3_4_s, command = lambda: self.confirm(settings.t5_3_4_n, settings.t5_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_5, text = settings.t5_4_4_n, state = settings.t5_4_4_s, command = lambda: self.confirm(settings.t5_4_4_n, settings.t5_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_5.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_5.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_5.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_5.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_5.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_5.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_5.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_5.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_5.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_5.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def main_tab_6(self):
        main_tab_6 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_6, text = settings.main_tab_6_n)

        ttk.Button(main_tab_6, text = settings.t6_0_0_n, state = settings.t6_0_0_s, command = lambda: self.confirm(settings.t6_0_0_n, settings.t6_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_1_0_n, state = settings.t6_1_0_s, command = lambda: self.confirm(settings.t6_1_0_n, settings.t6_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_2_0_n, state = settings.t6_2_0_s, command = lambda: self.confirm(settings.t6_2_0_n, settings.t6_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_3_0_n, state = settings.t6_3_0_s, command = lambda: self.confirm(settings.t6_3_0_n, settings.t6_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_4_0_n, state = settings.t6_4_0_s, command = lambda: self.confirm(settings.t6_4_0_n, settings.t6_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_6, text = settings.t6_0_1_n, state = settings.t6_0_1_s, command = lambda: self.confirm(settings.t6_0_1_n, settings.t6_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_1_1_n, state = settings.t6_1_1_s, command = lambda: self.confirm(settings.t6_1_1_n, settings.t6_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_2_1_n, state = settings.t6_2_1_s, command = lambda: self.confirm(settings.t6_2_1_n, settings.t6_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_3_1_n, state = settings.t6_3_1_s, command = lambda: self.confirm(settings.t6_3_1_n, settings.t6_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_4_1_n, state = settings.t6_4_1_s, command = lambda: self.confirm(settings.t6_4_1_n, settings.t6_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_6, text = settings.t6_0_2_n, state = settings.t6_0_2_s, command = lambda: self.confirm(settings.t6_0_2_n, settings.t6_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_1_2_n, state = settings.t6_1_2_s, command = lambda: self.confirm(settings.t6_1_2_n, settings.t6_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_2_2_n, state = settings.t6_2_2_s, command = lambda: self.confirm(settings.t6_2_2_n, settings.t6_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_3_2_n, state = settings.t6_3_2_s, command = lambda: self.confirm(settings.t6_3_2_n, settings.t6_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_4_2_n, state = settings.t6_4_2_s, command = lambda: self.confirm(settings.t6_4_2_n, settings.t6_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_6, text = settings.t6_0_3_n, state = settings.t6_0_3_s, command = lambda: self.confirm(settings.t6_0_3_n, settings.t6_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_1_3_n, state = settings.t6_1_3_s, command = lambda: self.confirm(settings.t6_1_3_n, settings.t6_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_2_3_n, state = settings.t6_2_3_s, command = lambda: self.confirm(settings.t6_2_3_n, settings.t6_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_3_3_n, state = settings.t6_3_3_s, command = lambda: self.confirm(settings.t6_3_3_n, settings.t6_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_4_3_n, state = settings.t6_4_3_s, command = lambda: self.confirm(settings.t6_4_3_n, settings.t6_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_6, text = settings.t6_0_4_n, state = settings.t6_0_4_s, command = lambda: self.confirm(settings.t6_0_4_n, settings.t6_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_1_4_n, state = settings.t6_1_4_s, command = lambda: self.confirm(settings.t6_1_4_n, settings.t6_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_2_4_n, state = settings.t6_2_4_s, command = lambda: self.confirm(settings.t6_2_4_n, settings.t6_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_3_4_n, state = settings.t6_3_4_s, command = lambda: self.confirm(settings.t6_3_4_n, settings.t6_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_6, text = settings.t6_4_4_n, state = settings.t6_4_4_s, command = lambda: self.confirm(settings.t6_4_4_n, settings.t6_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_6.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_6.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_6.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_6.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_6.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_6.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_6.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_6.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_6.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_6.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def main_tab_7(self):
        main_tab_7 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_7, text = settings.main_tab_7_n)

        ttk.Button(main_tab_7, text = settings.t7_0_0_n, state = settings.t7_0_0_s, command = lambda: self.confirm(settings.t7_0_0_n, settings.t7_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_1_0_n, state = settings.t7_1_0_s, command = lambda: self.confirm(settings.t7_1_0_n, settings.t7_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_2_0_n, state = settings.t7_2_0_s, command = lambda: self.confirm(settings.t7_2_0_n, settings.t7_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_3_0_n, state = settings.t7_3_0_s, command = lambda: self.confirm(settings.t7_3_0_n, settings.t7_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_4_0_n, state = settings.t7_4_0_s, command = lambda: self.confirm(settings.t7_4_0_n, settings.t7_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_7, text = settings.t7_0_1_n, state = settings.t7_0_1_s, command = lambda: self.confirm(settings.t7_0_1_n, settings.t7_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_1_1_n, state = settings.t7_1_1_s, command = lambda: self.confirm(settings.t7_1_1_n, settings.t7_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_2_1_n, state = settings.t7_2_1_s, command = lambda: self.confirm(settings.t7_2_1_n, settings.t7_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_3_1_n, state = settings.t7_3_1_s, command = lambda: self.confirm(settings.t7_3_1_n, settings.t7_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_4_1_n, state = settings.t7_4_1_s, command = lambda: self.confirm(settings.t7_4_1_n, settings.t7_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_7, text = settings.t7_0_2_n, state = settings.t7_0_2_s, command = lambda: self.confirm(settings.t7_0_2_n, settings.t7_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_1_2_n, state = settings.t7_1_2_s, command = lambda: self.confirm(settings.t7_1_2_n, settings.t7_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_2_2_n, state = settings.t7_2_2_s, command = lambda: self.confirm(settings.t7_2_2_n, settings.t7_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_3_2_n, state = settings.t7_3_2_s, command = lambda: self.confirm(settings.t7_3_2_n, settings.t7_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_4_2_n, state = settings.t7_4_2_s, command = lambda: self.confirm(settings.t7_4_2_n, settings.t7_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_7, text = settings.t7_0_3_n, state = settings.t7_0_3_s, command = lambda: self.confirm(settings.t7_0_3_n, settings.t7_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_1_3_n, state = settings.t7_1_3_s, command = lambda: self.confirm(settings.t7_1_3_n, settings.t7_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_2_3_n, state = settings.t7_2_3_s, command = lambda: self.confirm(settings.t7_2_3_n, settings.t7_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_3_3_n, state = settings.t7_3_3_s, command = lambda: self.confirm(settings.t7_3_3_n, settings.t7_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_4_3_n, state = settings.t7_4_3_s, command = lambda: self.confirm(settings.t7_4_3_n, settings.t7_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_7, text = settings.t7_0_4_n, state = settings.t7_0_4_s, command = lambda: self.confirm(settings.t7_0_4_n, settings.t7_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_1_4_n, state = settings.t7_1_4_s, command = lambda: self.confirm(settings.t7_1_4_n, settings.t7_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_2_4_n, state = settings.t7_2_4_s, command = lambda: self.confirm(settings.t7_2_4_n, settings.t7_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_3_4_n, state = settings.t7_3_4_s, command = lambda: self.confirm(settings.t7_3_4_n, settings.t7_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_7, text = settings.t7_4_4_n, state = settings.t7_4_4_s, command = lambda: self.confirm(settings.t7_4_4_n, settings.t7_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_7.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_7.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_7.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_7.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_7.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_7.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_7.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_7.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_7.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_7.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def main_tab_8(self):
        main_tab_8 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_8, text = settings.main_tab_8_n)

        ttk.Button(main_tab_8, text = settings.t8_0_0_n, state = settings.t8_0_0_s, command = lambda: self.confirm(settings.t8_0_0_n, settings.t8_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_1_0_n, state = settings.t8_1_0_s, command = lambda: self.confirm(settings.t8_1_0_n, settings.t8_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_2_0_n, state = settings.t8_2_0_s, command = lambda: self.confirm(settings.t8_2_0_n, settings.t8_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_3_0_n, state = settings.t8_3_0_s, command = lambda: self.confirm(settings.t8_3_0_n, settings.t8_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_4_0_n, state = settings.t8_4_0_s, command = lambda: self.confirm(settings.t8_4_0_n, settings.t8_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_8, text = settings.t8_0_1_n, state = settings.t8_0_1_s, command = lambda: self.confirm(settings.t8_0_1_n, settings.t8_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_1_1_n, state = settings.t8_1_1_s, command = lambda: self.confirm(settings.t8_1_1_n, settings.t8_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_2_1_n, state = settings.t8_2_1_s, command = lambda: self.confirm(settings.t8_2_1_n, settings.t8_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_3_1_n, state = settings.t8_3_1_s, command = lambda: self.confirm(settings.t8_3_1_n, settings.t8_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_4_1_n, state = settings.t8_4_1_s, command = lambda: self.confirm(settings.t8_4_1_n, settings.t8_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_8, text = settings.t8_0_2_n, state = settings.t8_0_2_s, command = lambda: self.confirm(settings.t8_0_2_n, settings.t8_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_1_2_n, state = settings.t8_1_2_s, command = lambda: self.confirm(settings.t8_1_2_n, settings.t8_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_2_2_n, state = settings.t8_2_2_s, command = lambda: self.confirm(settings.t8_2_2_n, settings.t8_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_3_2_n, state = settings.t8_3_2_s, command = lambda: self.confirm(settings.t8_3_2_n, settings.t8_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_4_2_n, state = settings.t8_4_2_s, command = lambda: self.confirm(settings.t8_4_2_n, settings.t8_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_8, text = settings.t8_0_3_n, state = settings.t8_0_3_s, command = lambda: self.confirm(settings.t8_0_3_n, settings.t8_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_1_3_n, state = settings.t8_1_3_s, command = lambda: self.confirm(settings.t8_1_3_n, settings.t8_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_2_3_n, state = settings.t8_2_3_s, command = lambda: self.confirm(settings.t8_2_3_n, settings.t8_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_3_3_n, state = settings.t8_3_3_s, command = lambda: self.confirm(settings.t8_3_3_n, settings.t8_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_4_3_n, state = settings.t8_4_3_s, command = lambda: self.confirm(settings.t8_4_3_n, settings.t8_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_8, text = settings.t8_0_4_n, state = settings.t8_0_4_s, command = lambda: self.confirm(settings.t8_0_4_n, settings.t8_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_1_4_n, state = settings.t8_1_4_s, command = lambda: self.confirm(settings.t8_1_4_n, settings.t8_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_2_4_n, state = settings.t8_2_4_s, command = lambda: self.confirm(settings.t8_2_4_n, settings.t8_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_3_4_n, state = settings.t8_3_4_s, command = lambda: self.confirm(settings.t8_3_4_n, settings.t8_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_8, text = settings.t8_4_4_n, state = settings.t8_4_4_s, command = lambda: self.confirm(settings.t8_4_4_n, settings.t8_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_8.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_8.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_8.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_8.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_8.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_8.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_8.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_8.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_8.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_8.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def main_tab_9(self):
        main_tab_9 = ttk.Frame(self.main, padding = 5, style = "TFrame")
        self.main.add(main_tab_9, text = settings.main_tab_9_n)

        ttk.Button(main_tab_9, text = settings.t9_0_0_n, state = settings.t9_0_0_s, command = lambda: self.confirm(settings.t9_0_0_n, settings.t9_0_0_p), style = "TButton").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_1_0_n, state = settings.t9_1_0_s, command = lambda: self.confirm(settings.t9_1_0_n, settings.t9_1_0_p), style = "TButton").grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_2_0_n, state = settings.t9_2_0_s, command = lambda: self.confirm(settings.t9_2_0_n, settings.t9_2_0_p), style = "TButton").grid(row = 0, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_3_0_n, state = settings.t9_3_0_s, command = lambda: self.confirm(settings.t9_3_0_n, settings.t9_3_0_p), style = "TButton").grid(row = 0, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_4_0_n, state = settings.t9_4_0_s, command = lambda: self.confirm(settings.t9_4_0_n, settings.t9_4_0_p), style = "TButton").grid(row = 0, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_9, text = settings.t9_0_1_n, state = settings.t9_0_1_s, command = lambda: self.confirm(settings.t9_0_1_n, settings.t9_0_1_p), style = "TButton").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_1_1_n, state = settings.t9_1_1_s, command = lambda: self.confirm(settings.t9_1_1_n, settings.t9_1_1_p), style = "TButton").grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_2_1_n, state = settings.t9_2_1_s, command = lambda: self.confirm(settings.t9_2_1_n, settings.t9_2_1_p), style = "TButton").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_3_1_n, state = settings.t9_3_1_s, command = lambda: self.confirm(settings.t9_3_1_n, settings.t9_3_1_p), style = "TButton").grid(row = 1, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_4_1_n, state = settings.t9_4_1_s, command = lambda: self.confirm(settings.t9_4_1_n, settings.t9_4_1_p), style = "TButton").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_9, text = settings.t9_0_2_n, state = settings.t9_0_2_s, command = lambda: self.confirm(settings.t9_0_2_n, settings.t9_0_2_p), style = "TButton").grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_1_2_n, state = settings.t9_1_2_s, command = lambda: self.confirm(settings.t9_1_2_n, settings.t9_1_2_p), style = "TButton").grid(row = 2, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_2_2_n, state = settings.t9_2_2_s, command = lambda: self.confirm(settings.t9_2_2_n, settings.t9_2_2_p), style = "TButton").grid(row = 2, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_3_2_n, state = settings.t9_3_2_s, command = lambda: self.confirm(settings.t9_3_2_n, settings.t9_3_2_p), style = "TButton").grid(row = 2, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_4_2_n, state = settings.t9_4_2_s, command = lambda: self.confirm(settings.t9_4_2_n, settings.t9_4_2_p), style = "TButton").grid(row = 2, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_9, text = settings.t9_0_3_n, state = settings.t9_0_3_s, command = lambda: self.confirm(settings.t9_0_3_n, settings.t9_0_3_p), style = "TButton").grid(row = 3, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_1_3_n, state = settings.t9_1_3_s, command = lambda: self.confirm(settings.t9_1_3_n, settings.t9_1_3_p), style = "TButton").grid(row = 3, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_2_3_n, state = settings.t9_2_3_s, command = lambda: self.confirm(settings.t9_2_3_n, settings.t9_2_3_p), style = "TButton").grid(row = 3, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_3_3_n, state = settings.t9_3_3_s, command = lambda: self.confirm(settings.t9_3_3_n, settings.t9_3_3_p), style = "TButton").grid(row = 3, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_4_3_n, state = settings.t9_4_3_s, command = lambda: self.confirm(settings.t9_4_3_n, settings.t9_4_3_p), style = "TButton").grid(row = 3, column = 4, padx = 5, pady = 5, sticky = "nsew")

        ttk.Button(main_tab_9, text = settings.t9_0_4_n, state = settings.t9_0_4_s, command = lambda: self.confirm(settings.t9_0_4_n, settings.t9_0_4_p), style = "TButton").grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_1_4_n, state = settings.t9_1_4_s, command = lambda: self.confirm(settings.t9_1_4_n, settings.t9_1_4_p), style = "TButton").grid(row = 4, column = 1, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_2_4_n, state = settings.t9_2_4_s, command = lambda: self.confirm(settings.t9_2_4_n, settings.t9_2_4_p), style = "TButton").grid(row = 4, column = 2, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_3_4_n, state = settings.t9_3_4_s, command = lambda: self.confirm(settings.t9_3_4_n, settings.t9_3_4_p), style = "TButton").grid(row = 4, column = 3, padx = 5, pady = 5, sticky = "nsew")
        ttk.Button(main_tab_9, text = settings.t9_4_4_n, state = settings.t9_4_4_s, command = lambda: self.confirm(settings.t9_4_4_n, settings.t9_4_4_p), style = "TButton").grid(row = 4, column = 4, padx = 5, pady = 5, sticky = "nsew")

        main_tab_9.grid_rowconfigure(0, minsize = button_height, weight = 1)
        main_tab_9.grid_rowconfigure(1, minsize = button_height, weight = 1)
        main_tab_9.grid_rowconfigure(2, minsize = button_height, weight = 1)
        main_tab_9.grid_rowconfigure(3, minsize = button_height, weight = 1)
        main_tab_9.grid_rowconfigure(4, minsize = button_height, weight = 1)
        main_tab_9.grid_columnconfigure(0, minsize = button_width, weight = 1)
        main_tab_9.grid_columnconfigure(1, minsize = button_width, weight = 1)
        main_tab_9.grid_columnconfigure(2, minsize = button_width, weight = 1)
        main_tab_9.grid_columnconfigure(3, minsize = button_width, weight = 1)
        main_tab_9.grid_columnconfigure(4, minsize = button_width, weight = 1)

    def confirm(self, name, path):
        confirm = tk.Toplevel()
        confirm.overrideredirect(True)
        confirm.attributes("-topmost", True)
        confirm.iconbitmap("./system/logo-1_icon.ico")
        confirm.title(f"TeaChimer-{version}_CONFIRM")
        confirm.geometry(f"{screen_width}x{screen_height}")
        confirm.configure(background = "white")
        confirm.focus_force()

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(confirm, image = logo, style = "logo.TLabel")
        logo_label.place(x = 10, y = 0, width = 300, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}\n{settings.school_name}\n{settings.admin_name}"
        ver_label = ttk.Label(confirm, text = ver, style = "TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = f"{name}を呼びますか？"
        text_label = ttk.Label(confirm, text = text, style = "notice.TLabel")
        text_label.place(x = (screen_width - button_width * 2 - 10) / 2, y = 100 + ((screen_height - 100 - button_height + 30 - 50 - 10) / 2), width = (button_width * 2) + 10, height = 50 + 10)

        text = "はい"
        button = ttk.Button(confirm, text = text, command = lambda: self.playsound(confirm, name, path), style = "TButton")
        button.place(x = (screen_width - button_width * 2 - 10) / 2, y = 100 + ((screen_height - 100 - button_height + 30 - 50 - 10) / 2) + (50 + 10), width = button_width, height = button_height)

        text = "いいえ"
        button = ttk.Button(confirm, text = text, command = confirm.destroy, style = "TButton")
        button.place(x = ((screen_width - button_width * 2 - 10) / 2) + button_width + 10, y = 100 + ((screen_height - 100 - button_height + 30 - 50 - 10) / 2) + (50 + 10), width = button_width, height = button_height)

    def playsound(self, confirm, name, path):
        playsound = tk.Toplevel()
        playsound.overrideredirect(True)
        playsound.attributes("-topmost", True)
        playsound.iconbitmap("./system/logo-1_icon.ico")
        playsound.title(f"TeaChimer-{version}_PLAYSOUND")
        playsound.geometry(f"{screen_width}x{screen_height}")
        playsound.configure(background = "white")
        playsound.focus_force()

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(playsound, image = logo, style = "logo.TLabel")
        logo_label.place(x = 10, y = 0, width = 300, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}\n{settings.school_name}\n{settings.admin_name}"
        ver_label = ttk.Label(playsound, text = ver, style = "TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = f"{name}を呼んでいます"
        text_label = ttk.Label(playsound, text = text, style = "notice.TLabel")
        text_label.place(x = 0, y = 100, width = screen_width, height = screen_height - 100)

        for i in range(2):
            playsound.update()
            winsound.PlaySound(f"{path}", winsound.SND_FILENAME)
            playsound.update()

        confirm.destroy()
        playsound.destroy()

    def exit(self, event):
        exit = tk.Toplevel()
        exit.overrideredirect(True)
        exit.attributes("-topmost", True)
        exit.iconbitmap("./system/logo-1_icon.ico")
        exit.title(f"TeaChimer-{version}_EXIT")
        exit.geometry(f"{screen_width}x{screen_height}")
        exit.configure(background = "white")
        exit.focus_force()

        logo = tk.PhotoImage(file = "./system/logo-2_small.png")
        logo_label = ttk.Label(exit, image = logo, style = "logo.TLabel")
        logo_label.place(x = 10, y = 0, width = 300, height = 100)
        logo_label.image = logo

        ver = f"TeaChimer-{version}\n{settings.school_name}\n{settings.admin_name}"
        ver_label = ttk.Label(exit, text = ver, style = "TLabel")
        ver_label.place(x = 10 + 300 + 10, y = 0, width = 300, height = 100)

        text = "TeaChimerを終了しますか？"
        text_label = ttk.Label(exit, text = text, style = "notice.TLabel")
        text_label.place(x = (screen_width - button_width * 2 - 10) / 2, y = 100 + ((screen_height - 100 - button_height + 30 - 50 - 10) / 2), width = (button_width * 2) + 10, height = 50 + 10)

        text = "はい"
        button = ttk.Button(exit, text = text, command = self.master.destroy, style = "TButton")
        button.place(x = (screen_width - button_width * 2 - 10) / 2, y = 100 + ((screen_height - 100 - button_height + 30 - 50 - 10) / 2) + (50 + 10), width = button_width, height = button_height)

        text = "いいえ"
        button = ttk.Button(exit, text = text, command = exit.destroy, style = "TButton")
        button.place(x = ((screen_width - button_width * 2 - 10) / 2) + button_width + 10, y = 100 + ((screen_height - 100 - button_height + 30 - 50 - 10) / 2) + (50 + 10), width = button_width, height = button_height)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
button_width = (screen_width - 10 * 6) / 5
button_height = (screen_height - 100 - 30 - 10 * 6) / 5
version = "v1.0.0"
app = Main(root)
root.mainloop()