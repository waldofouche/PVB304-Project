# from tkinter import *  will import everything from tkinter.
# we can also use import tkinter as tk
# but that way for every attribute we must type tk.attrib-name
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.io.wavfile import read

# this is the main class, SignalProc, inherited from Frame
class SignalProc(Frame):
    # Defines settings upon initialization.
    def __init__(self, master=None):

        # parameters we want to send through Frame class
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #initialization of signalProc frame
        self.init_signalProc()

     # here we create the initialization frame
    def init_signalProc(self):

        # set the title of master widget
        self.master.title("Signal Analysis")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu, tearoff=0)

        # adds a commanda to the menu option, calling it and the
        # command it runs on event
        file.add_command(label="Load Signal", command=self.load_signals)
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)
    def create_widgets(self):
            self.browse = Button(self)
            self.browse["text"] = "Browse Signal"
            self.browse["command"] = self.load_signals
            self.browse.grid(row=0, column=0)
    # Loads Signal
    def load_signals(self):

        # Doesn't work 
        filename = filedialog.askopenfilename(filetypes = (("signal files", "*.wav;*.mp3")
                                                             ,("All files", "*.*") ))
         # read audio samples 
        input_data = read(filename)
        audio = input_data[1]
        
        # Create New figure to be plotted
        fig = plt.figure(figsize=(5,5))

        # plot the first 1024 samples
        plt.plot(audio[0:1024])
        # plot the first 1024 samples
        plt.plot(audio[0:1024])
        # label the axes
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        # set the title  
        plt.title("Sample Wav")
        
        # DrawingArea
        self.canvas = FigureCanvasTkAgg(fig, master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=LEFT)
    # Exits the Client
    def client_exit(self):
        exit()

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()
root.geometry("1024x600")
# creation of an instance
app = SignalProc(root)
# mainloop
root.mainloop()