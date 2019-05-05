import random
from tkinter import *


window = Tk()
window.geometry('800x600')
leaderboards = Tk()
leaderboards.title("LeaderBoards!")

global x
global y

x= 0
y = - 100

def key(event):
    if event.char == "w":
        canvas.move(player1,0,-100)
    elif event.char == "s":
        canvas.move(player1,0,100)
    elif event.char=="e":
        player1fire(event)
    elif event.char == "8":
        canvas.move(player2,0,-100)
    elif event.char == "2":
        canvas.move(player2,0,100)
    elif event.char=="5":
        player2fire()



canvas = Canvas(window,width=800,height=600)
canvas.bind("<Key>",key)
canvas.focus_set()
canvas.pack()

player1image = PhotoImage(file='player.png')
player2image = PhotoImage(file='computer.png')

player1 = canvas.create_image(100,200, image=player1image)
player2 = canvas.create_image(700,500, image=player2image)


global playerBullet
playerBullet = canvas.create_oval(0,0,0,0,fill="#1abc9c")
player2bullet = canvas.create_oval(0,0,0,0,fill="#c0392b")


bulletSpeed = 2

def player1fire(event):
    global playerBullet
    global playerX
    global playerY
    playerX = canvas.coords(player1)[0]
    playerY = canvas.coords(player1)[1]
    canvas.coords(playerBullet,playerX,playerY,playerX+50,playerY+50)  

def movePlayer1Bullet():
    window.after(1,movePlayer1Bullet)
    canvas.move(playerBullet,bulletSpeed,0)
    coord0 = canvas.coords(playerBullet)[0]
    coord1 = canvas.coords(playerBullet)[1]
    coord2 = canvas.coords(playerBullet)[2]
    coord3 = canvas.coords(playerBullet)[3]
    if canvas.find_overlapping(coord0,coord1,coord2,coord3) == (2,3):
        window.destroy()
        label= Label(leaderboards,text='Player 1 Won',font=("none",50))
        label.pack()       

movePlayer1Bullet()



def movePlayer2Bullet():
    window.after(1,movePlayer2Bullet)
    canvas.move(player2bullet,-1 * bulletSpeed,0)
    coord0 = canvas.coords(player2bullet)[0]
    coord1 = canvas.coords(player2bullet)[1]
    coord2 = canvas.coords(player2bullet)[2]
    coord3 = canvas.coords(player2bullet)[3]
    if canvas.find_overlapping(coord0,coord1,coord2,coord3) == (1,4):
        window.destroy()
        label= Label(leaderboards,text='Player 2 Won',font=("none",50))
        label.pack()

movePlayer2Bullet()    

def player2fire():
    player2x = canvas.coords(player2)[0]
    player2y = canvas.coords(player2)[1]
    canvas.coords(player2bullet,player2x,player2y,player2x+50,player2y+50)
    
window.mainloop()