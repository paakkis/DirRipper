import tkinter
import tkinter as tk
from tkinter import filedialog, Text
import os
from grabber import grabber


root = tk.Tk()
dirlabel = tk.Label(root)

pdf = tk.BooleanVar()
mp4 = tk.BooleanVar()
jpg = tk.BooleanVar()
png = tk.BooleanVar()

# Ask user to define the directory where downloaded files are saved
def addDirectory():

    global dirlabel
    global dirs
    dirlabel.destroy()

    dirs = filedialog.askdirectory()
    dirlabel = tk.Label(frame, text=dirs, bg="white")
    dirlabel.pack()

# Ask user to give a link to the online directory

# TODO Ask user to define which filetypes to download
def addFileType():
    return None

# Start downloading the files from specified link
def download():
    #linkEntry.delete(0, tkinter.END)
    url = linkEntry.get()
    grabber(dirs, url)
    filename = tk.Label(frame, text=grabber.filename)
    filename.pack()

canvas = tk.Canvas(root, height=600, width=600, bg="#505050")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

saveDir = tk.Button(frame, text="Select saving directory", padx=10, pady=10, fg="black", command=addDirectory)
download = tk.Button(frame, text="Download files", padx=50, pady=10, fg="black", command=download)
linkLabel = tk.Label(frame, text="Insert a link to a HTTP directory", bg="white")
linkEntry = tk.Entry(frame, width = 100)
filetypeLabel = tk.Label(frame, text="Select filetypes to be downloaded", bg="white")

pdfButton = tk.Checkbutton(frame, text=".pdf", variable=pdf, command=addFileType)
mp4Button = tk.Checkbutton(frame, text=".mp4", variable=mp4, command=addFileType)
jpgButton = tk.Checkbutton(frame, text=".jpg", variable=jpg, command=addFileType)
pngButton = tk.Checkbutton(frame, text=".png", variable=png, command=addFileType)


root.title("DirRipper (beta) by juusopaa")

saveDir.place(x=50, y=500)
saveDir.pack()
linkLabel.pack()
linkEntry.pack()
filetypeLabel.pack()
pdfButton.pack()
mp4Button.pack()
jpgButton.pack()
pngButton.pack()


download.pack()

root.mainloop()
