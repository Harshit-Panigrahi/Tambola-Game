import socket
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image

IP_ADDR="127.0.0.1"
PORT=5000

SERVER=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.connect((IP_ADDR, PORT))

window=Tk()

def askName():
  window.title("Tambola Game")
  window.state("zoomed")

  scrW=window.winfo_screenwidth()
  scrH=window.winfo_screenheight()
  bg=Image.open("./background.png")
  bg=bg.resize((scrW, scrH))

  bg=ImageTk.PhotoImage(bg)
  canvas=Canvas(window, width=scrW, height=scrH)
  canvas.pack(fill=BOTH, expand=True)
  canvas.create_image(0, 0, image=bg, anchor=NW)
  canvas.create_text(scrW/2, scrH/5, anchor=CENTER, text="Enter your name:", font=("Chalkboard SE", 50))

  name_entry=Entry(window, justify=CENTER, font=("Helvetica", 35))
  name_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

  button = Button(
    window,
    text="Join",
    bg="royalblue",
    fg="white",
    font=("Helvetica", 25),
    command=lambda:saveName(name_entry.get()),
    padx=20
  )
  button.place(relx=0.5, rely=0.75, anchor=CENTER)

  window.mainloop()

def saveName(name):
  """ """
  if (name != ""):
    window.destroy()
    SERVER.send(name.encode("utf-8"))


def receive():
  """ """

askName()

recvThread = Thread(target=receive)
recvThread.start()

