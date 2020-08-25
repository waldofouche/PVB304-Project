from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy import *
from scipy import ndimage
from matplotlib.pyplot import imread
from matplotlib.figure import Figure

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Paint(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_paint()

    #Creation of init_window
    def init_paint(self):

        # changing the title of our master widget
        self.master.title("Image Processing")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.create_widgets()
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

    def create_widgets(self):
            self.browse = Button(self)
            self.browse["text"] = "Browse Image"
            self.browse["command"] = self.loadImage
            self.browse.grid(row=0, column=0)

            self.uni_filter = Button(self)
            self.uni_filter["text"] = "Uniform Filter"
            self.uni_filter["command"] = self.unifilter
            self.uni_filter.grid(row=0, column=1)

            self.rotat_right = Button(self)
            self.rotat_right["text"]="Rotate Right"
            self.rotat_right["command"] = self.rotate_right
            self.rotat_right.grid(row=1, column=0)


            self.rotat_left = Button(self)
            self.rotat_left["text"]="Rotate Left"
            self.rotat_left["command"] = self.rotate_left
            self.rotat_left.grid(row=1, column=1)

            self.gau_filter = Button(self)
            self.gau_filter["text"]="Gaussian Filter"
            self.gau_filter["command"] = self.gaufilter
            self.gau_filter.grid(row=0, column=3)

            self.minm = Button(self)
            self.minm["text"]="Minimum"
            self.minm["command"] = self.min_val
            self.minm.grid(row=0, column=4)

            self.varianc = Button(self)
            self.varianc["text"]="Variance"
            self.varianc["command"] = self.var_val
            self.varianc.grid(row=0, column=5)

            self.text1=Entry(self)
            self.text1.grid()
            self.text1.grid(row=1, column=3)
            self.text1.focus()


    canvas=''
    def loadImage(self):

        filename = filedialog.askopenfilename(filetypes = (("image files", "*.png;*.jpg")
                                                             ,("All files", "*.*") ))

        self.image = imread(filename)
        print(type(imread(filename)))
        fig = plt.figure(figsize=(5,5))
        if self.canvas=='':
            self.im = plt.imshow(self.image) # later use a.set_data(new_data)
            axs = plt.gca()
            axs.set_xticklabels([])
            axs.set_yticklabels([])

            # a tk.DrawingArea
            self.canvas = FigureCanvasTkAgg(fig, master=root)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        else:
            self.im.set_data(self.image)
            self.canvas.draw()


    theta = 0
    def rotate_left(self):
        self.theta += 90
        rotated = ndimage.rotate(self.image, self.theta)
        self.im.set_data(rotated)
        self.canvas.draw()

    def rotate_right(self):
            self.theta -= 90
            rotated = ndimage.rotate(self.image, self.theta)
            self.im.set_data(rotated)
            self.canvas.draw()

    def unifilter(self):
        self.image = ndimage.uniform_filter(self.image, size=int(self.text1.get()))
        self.im.set_data(self.image)
        self.canvas.draw()

    def gaufilter(self):
        self.image = ndimage.gaussian_filter(self.image, sigma=int(self.text1.get()))
        self.im.set_data(self.image)
        self.canvas.draw()

    def min_val(self):
        self.text1.delete(0,END)
        self.text1.insert(0,ndimage.minimum(self.image))

    def var_val(self):
        self.text1.delete(0,END)
        self.text1.insert(0,ndimage.variance(self.image))

    def client_exit(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("1024x600")

#creation of an instance
app = Paint(root)


#mainloop
root.mainloop()