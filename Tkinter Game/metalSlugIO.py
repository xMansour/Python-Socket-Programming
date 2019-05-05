import random
from tkinter import *


window = Tk()
window.geometry('600x600')
leaderboards = Tk()
leaderboards.title("LeaderBoards!")


global x
global y

x= 0
y = - 100

def negative():
    global y
    y = -y
    window.after(1000,negative)
window.after(1000,negative)

def mouse(event):
    global playerBullet
    global playerX
    global playerY
    playerX = canvas.coords(player)[0]
    playerY = canvas.coords(player)[1]
    canvas.coords(playerBullet,playerX,playerY,playerX+50,playerY+50)  


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

player = canvas.create_image(100,200, image=playerImage)
computer = canvas.create_image(500,500, image=computerImage)


global playerBullet
playerBullet = canvas.create_oval(0,0,0,0,fill="#1abc9c")
computerBullet = canvas.create_oval(0,0,0,0,fill="#c0392b")

bulletSpeed = 2

def movePlayerBullet():
    window.after(1,movePlayerBullet)
    canvas.move(playerBullet,bulletSpeed,0)
    coord0 = canvas.coords(playerBullet)[0]
    coord1 = canvas.coords(playerBullet)[1]
    coord2 = canvas.coords(playerBullet)[2]
    coord3 = canvas.coords(playerBullet)[3]
    if canvas.find_overlapping(coord0,coord1,coord2,coord3) == (2,3):
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
    if canvas.find_overlapping(coord0,coord1,coord2,coord3) == (1,4):
        window.destroy()
        label= Label(leaderboards,text='You lost',font=("none",50))
        label.pack()

moveComputerBulletInX()    

def fireComputerBullet():
    coord0 = canvas.coords(computer)[0]
    coord1 = canvas.coords(computer)[1]
    canvas.coords(computerBullet,coord0,coord1,coord0+50,coord1+50)
    window.after(700,fireComputerBullet)

fireComputerBullet()    


def moveComputer():
    canvas.move(computer,0,y)

for i in range(0,50):
    x = x + 200
    window.after(x,moveComputer)
    
window.mainloop()