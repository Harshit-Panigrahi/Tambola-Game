import socket, random
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image

IP_ADDR="127.0.0.1"
PORT=5000

SERVER=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.connect((IP_ADDR, PORT))

window1=None
window2=None
scrW=None
scrH=None
ticketGrid=[]
curNumLst=[]

def askName():
  global window1, scrW, scrH
  window1= Tk()
  window1.title("Tambola Game")

  scrW=window1.winfo_screenwidth()
  scrH=window1.winfo_screenheight()
  window1.state("zoomed")

  canvas=Canvas(window1, width=scrW, height=scrH)
  canvas.pack(fill=BOTH, expand=True)

  bg=Image.open("./bg1.png")
  bg=bg.resize((scrW, scrH))
  bg=ImageTk.PhotoImage(bg)
  canvas.create_image(0, 0, image=bg, anchor=NW)

  canvas.create_text(
    scrW/2, scrH/5,
    anchor=CENTER,
    text="Enter your name:",
    font=("Chalkboard SE", 50)
  )

  name_entry=Entry(window1, justify=CENTER, font=("Helvetica", 35))
  name_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

  button = Button(
    window1,
    text="Join",
    bg="royalblue",
    fg="white",
    font=("Helvetica", 25),
    command=lambda:saveName(name_entry.get()),
    padx=20
  )
  button.place(relx=0.5, rely=0.75, anchor=CENTER)

  window1.mainloop()

def saveName(name):
  if (name != ""):
    window1.destroy()
    SERVER.send(name.encode("utf-8"))
    gameWindow()
    
def gameWindow():
  global window2, scrW, scrW
  window2=Tk()
  window2.title("Tambola Game")

  window2.state("zoomed")

  canvas=Canvas(window2, width=scrW, height=scrH)
  canvas.pack(fill=BOTH, expand=True)

  bg=Image.open("./bg2.png")
  bg=bg.resize((scrW, scrH))
  bg=ImageTk.PhotoImage(bg)
  canvas.create_image(0, 0, image=bg, anchor=NW)
  canvas.create_text(
    scrW/2,
    scrH/5,
    text="Tambola Game",
    font="Helvetica 45 bold italic",
    fill="gold",
    anchor=CENTER)

  createTicket()

  window2.mainloop()

def createTicket():
  global window2, scrW, scrH, ticketGrid
  ticketBg=Label(window2, bg="white")
  ticketBg.place(x=scrW/2, y=scrH/1.8, width=scrW/1.59, height=280, anchor=CENTER)

  for a in range(3):
    btnLst=[]
    for b in range(10):
      newBtn = Button(
        window2,
        bg="#ff785a",
        relief="flat",
        width=9,
        height=5
      )
      btnLst.append(newBtn)
      newBtn.place(x=(scrW/5.2)+(b*79.5), y=(scrH/2.7)+(a*90))
    ticketGrid.append(btnLst)
  placeNumbers()
  
def placeNumbers():
  global ticketGrid, curNumLst

  numDict={
    "0": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "1": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    "2": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
    "3": [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
    "4": [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
    "5": [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
    "6": [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
    "7": [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
    "8": [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
    "9": [90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
  }

  for row in range(0, 3):
    randClLst=[]
    for i in range(5):
      randCol=random.randint(0, 9)
      if (randCol not in randClLst):
        randClLst.append(randCol)

    for i in range(len(randClLst)):
      colNum = randClLst[i]
      numbersListByIndex = numDict[str(colNum)]
      randomNumber = random.choice(numbersListByIndex)

      if (randomNumber not in curNumLst) :
        numberBox=ticketGrid[row][colNum]
        numberBox.config(text=randomNumber, bg="royalblue")
        curNumLst.append(randomNumber)


askName()
