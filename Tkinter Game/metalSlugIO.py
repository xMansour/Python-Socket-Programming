import random
from tkinter import *


window = Tk()
leaderboards = Tk()

global x
global y

x= 0
y = - 100

def negative():
    global y
    window.after(1000,negative)
    y = -y
window.after(1000,negative)

def mouse(event):
    global playerBullet
    global coord0
    global coord1
    coord0 = canvas.coords(player)[0]
    coord1 = canvas.coords(player)[1]
    canvas.coords(playerBullet,coord0,coord1,coord0+50,coord1+50)  


def key(event):
    if event.char == "w":
        canvas.move(player,0,-100)
    elif event.char == "s":
        canvas.move(player,0,100)

canvas = Canvas(window,width=600,height=600)
canvas.bind("<Key>",key)
canvas.bind("<Button-1>",mouse)
canvas.focus_set()
canvas.pack()

playerImage = PhotoImage(file='player.png')
computerImage = PhotoImage(file='computer.png')

#player = canvas.create_rectangle(500,400,600,500,fill="#1abc9c",outline="#34495e")
player = canvas.create_image(500,200, image=playerImage)


global playerBullet
playerBullet = canvas.create_oval(0,0,0,0,fill="#1abc9c")
computerBullet = canvas.create_oval(0,50,0,0,fill="#c0392b")
#computer = canvas.create_image(700,600,800,700,fill="#c0392b",outline="#34495e")
computer = canvas.create_image(500,500, image=computerImage)
canvas.move(player,-400,0)

bulletSpeed = 2

def movePlayerBullet():
    window.after(1,movePlayerBullet)
    canvas.move(playerBullet,bulletSpeed,0)
    coord0 = canvas.coords(playerBullet)[0]
    coord1 = canvas.coords(playerBullet)[1]
    coord2 = canvas.coords(playerBullet)[2]
    coord3 = canvas.coords(playerBullet)[3]
    if canvas.find_overlapping(coord0,coord1,coord2,coord3)== (2,4) or canvas.find_overlapping(coord0,coord1,coord2,coord3)== (2,3,4):
        window.destroy()
        label= Label(leaderboards,text='You won',font=("none",50))
        label.pack()       

movePlayerBullet()

def moveComputerBulletInX():
    window.after(1,moveComputerBulletInX)
    canvas.move(computerBullet,-1 * bulletSpeed,0)
    coord0 = canvas.coords(computerBullet)[0]
    coord1 = canvas.coords(computerBullet)[1]
    coord2 = canvas.coords(computerBullet)[2]
    coord3 = canvas.coords(computerBullet)[3]
    if canvas.find_overlapping(coord0,coord1,coord2,coord3) == (1,3) or canvas.find_overlapping(coord0,coord1,coord2,coord3)== (1,2,3):
        window.destroy()
        label= Label(leaderboards,text='You lost',font=("none",50))
        label.pack()

moveComputerBulletInX()    

def moveComputerBulletInY():
    coord0 = canvas.coords(computer)[0]
    coord1 = canvas.coords(computer)[1]
    canvas.coords(computerBullet,coord0,coord1,coord0+50,coord1+50)
    window.after(700,moveComputerBulletInY)

moveComputerBulletInY()    

window.geometry('600x600')

def moveComputer():
    canvas.move(computer,0,y)

for i in range(0,50):
    x = x + 200
    window.after(x,moveComputer)
    
window.mainloop()