#!/usr/bin/python

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from os import path
import subprocess

global newpath
newpath = "{}\\".format(path.dirname(path.abspath(__file__)))


class Application(tk.Tk):

    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        # Values
        resolution_values = ['1920x1080', '1280x720', '720x480']
        bitrate_values = ['12000k', '5000k', '500k']
        fps_values = ['60', '29.97', '23.976']
        gop_values = ['50', '25', '15', '5']

        # Variables
        resolution = tk.StringVar()
        bitrate = tk.StringVar()
        fps = tk.StringVar()
        gop = tk.StringVar()
        pause = tk.IntVar()

        # Objects
        self.comboBox1 = ttk.Combobox(self, values=resolution_values,
                                      textvariable=resolution,
                                      width=15, height=20)
        self.comboBox2 = ttk.Combobox(self, values=bitrate_values,
                                      textvariable=bitrate,
                                      width=15, height=20)
        self.comboBox3 = ttk.Combobox(self, values=fps_values,
                                      textvariable=fps, width=15, height=20)
        self.comboBox4 = ttk.Combobox(self, values=gop_values,
                                      textvariable=gop, width=15, height=20)

        self.checkBox1 = tk.Checkbutton(self, text='Pause', variable=pause)

        self.label1 = tk.Label(self, text='Resolution')
        self.label2 = tk.Label(self, text='Bitrate')
        self.label3 = tk.Label(self, text='FPS')
        self.label4 = tk.Label(self, text='GOP')

        # Position
        self.comboBox1.grid(column=0, row=0, padx=10, pady=10)
        self.comboBox2.grid(column=0, row=1, padx=10)
        self.comboBox3.grid(column=0, row=2, padx=10, pady=10)
        self.comboBox4.grid(column=0, row=3, padx=5)

        self.checkBox1.grid(column=0, row=4, sticky='WE', padx=5, pady=12)

        self.label1.grid(column=1, row=0, sticky='W')
        self.label2.grid(column=1, row=1, sticky='W')
        self.label3.grid(column=1, row=2, sticky='W')
        self.label4.grid(column=1, row=3, sticky='W')

        def onClick():
            create_execute(resolution, bitrate, fps, gop)

        def create_execute(resolution, bitrate, fps, gop):
            commands = []
            commands.append('@set curpath=%~dp0')
            commands.append('@cd /d %curpath%')
            commands.append('@echo %curpath%')
            commands.append('set \"cont=mp4\"')
            commands.append('for %%i in (../in/*.*) do (')

            # Read variables values
            bitrate = bitrate.get()
            resolution = resolution.get()
            fps = fps.get()
            gop = gop.get()

            # Show error if bitrate is empty
            if not bitrate:
                msg.showwarning('Error!', 'Specify video bit rate.')
                return

            if not resolution:
                pass
            else:
                resolution = " -s " + resolution + ""

            if not fps:
                pass
            else:
                fps = " -r " + fps + ""

            if not gop:
                pass
            else:
                gop = " -g " + gop + ""

            commands.append("ffmpeg -i \"../in/%%i\" -vcodec h264" + resolution + "" + fps + "" + gop + " -b " + bitrate + " -bt " + bitrate + " -acodec mp3 -ar 44100 -ab 128k \"../out/%%~ni.%cont%\")")

            if pause.get():
                commands.append("pause")
            commands.append("@del %0")

            with open(newpath + 'Bin\\convert.bat', 'w',
                      encoding='utf-8') as myfile:
                for item in commands:
                    myfile.write('%s\n' % item)
            # Execute .bat file
            subprocess.Popen("Bin\\convert.bat",
                             creationflags=subprocess.CREATE_NEW_CONSOLE)

        # "Create and execute" button
        self.button1 = tk.Button(self, text='Create and execute',
                                 command=onClick)
        self.button1.grid(column=1, row=4, pady=10, sticky='W')


if __name__ == '__main__':
    app = Application(None)
    app.title("pyCoder v0.1")  # Title
    app.resizable(False, False)  # Disable resize
    w = 250  # Width of the window
    h = 180  # Height of the window

    # Get the path to programm and set the icon
    app.iconbitmap(newpath + 'th06r.ico')

    # Center screen
    ws = app.winfo_screenwidth()  # width of the screen
    hs = app.winfo_screenheight()  # height of the screen

    # Calculates x and y coordinates for the main window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # App's size and start position on the screen
    app.geometry('%dx%d+%d+%d' % (w, h, x, y))
    app.mainloop()
