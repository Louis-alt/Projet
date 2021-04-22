# -*- coding: cp1252 -*-

from tkinter import *
from random import randrange


def avancer ():
    global car_coord, step, arret_bcl, car, pts, temp
    pomme()         
    
    
    i = 0
    while (i <= (len(car)-1)):
        car_coord[i][0] = car_coord[i][0] + car_coord[i][2]
        car_coord[i][1] = car_coord[i][1] + car_coord[i][3]
        canv.coords(car[i], car_coord[i][0], car_coord[i][1], car_coord[i][0] + 10, car_coord[i][1] + 10)
        
        if (i == 0):
            temp[0] = [car_coord[i][2], car_coord[i][3]]
        else :
            temp[1] = [car_coord[i][2], car_coord[i][3]]
            car_coord[i][2] = temp[0][0]
            car_coord[i][3] = temp[0][1]
            temp[0] = temp[1]

            
            if ((car_coord[0][0] == car_coord[i][0]) and (car_coord[0][1] == car_coord[i][1])):
                arret_bcl = 1                
        i = i + 1
    
    if ((car_coord[0][0] == 0) or (car_coord[0][0] == 590)):
        arret_bcl = 1
    elif ((car_coord[0][1] == 0) or (car_coord[0][1] == 390)):
        arret_bcl = 1

    if (arret_bcl == 0):
        fen.after(50, avancer)

    
def commencer():
    global car_coord, car, pts, arret_bcl, temp, pom_la, pom_ov, pomx, pomy
    
    i = 0
    while (i <= (len(car)-1)):      
        canv.delete(car[i])
        i = i + 1
    canv.delete(pom_ov)    

    
    pts = 0
    car = [0] *4
    car_coord = [[0, 0, 0, 0]] *4
    arret_bcl = 0
    temp = [[0,0]]*2
    pom_la, pom_ov, pomx, pomy = -1, 0, 0, 0

    
    i = 0
    while (i <= (len(car)-1)):      
        if (i == 0):
            car_coord[i] = [300, 200, -10, 0]
        else :
            car_coord[i] = [car_coord[i-1][0] + 10, 200, -10, 0]
            
        car[i] = canv.create_rectangle(car_coord[i][0], car_coord[i][1], car_coord[i][0] + 10, car_coord[i][1] + 10, fill='white')

        i = i + 1
    avancer()   

    
def pomme ():
    global pom_la, pom_ov, pomx, pomy, car, car_coord, pts
    if (pom_la == 1):
        if ((car_coord[0][0] == pomx) and (car_coord[0][1] == pomy)):
            car.append(0)         
            x, y = car_coord[len(car_coord)-1][0] - car_coord[len(car_coord)-1][2] , car_coord[len(car_coord)-1][1] - car_coord[len(car_coord)-1][3]
            stepx, stepy = car_coord[len(car_coord)-1][2], car_coord[len(car_coord)-1][3]
            car_coord.append([x, y, stepx, stepy])
            
            car[len(car)-1] = canv.create_rectangle(x, y, x+10, y+10, fill='yellow')
            
            pts = pts + 10      
            lb_pts.configure(text="Points = " + str(pts))   
            pom_la = 0
    else:
        pomx, pomy = (randrange(57) + 1)*10, (randrange(38) + 1)*10
        if (pom_la != 0):
            pom_ov = canv.create_rectangle(pomx, pomy, pomx+10, pomy+10, fill='yellow')
        else :
            canv.coords(pom_ov, pomx, pomy, pomx+10, pomy+10)
        pom_la = 1
    
    
def left(event):
    global car_coord
    if (car_coord[0][2] != 10):
        car_coord[0][2] = -10
        car_coord[0][3] = 0
    
def right(event):
    global car_coord
    if (car_coord[0][2] != -10):
        car_coord[0][2] = 10
        car_coord[0][3] = 0
    
def up(event):
    global car_coord
    if (car_coord[0][3] != 10):
        car_coord[0][2] = 0
        car_coord[0][3] = -10
    
def down(event):
    global car_coord
    if (car_coord[0][3] != -10):
        car_coord[0][2] = 0
        car_coord[0][3] = 10


pts = 0        
car = [0] *4        
car_coord = [[0, 0, 0, 0]] *4      
arret_bcl = 0       
temp = [[0,0]]*2    
pom_la, pom_ov, pomx, pomy = -1, 0, 0, 0      


fen = Tk()
fen.title('{Snake}')
fen.bind("<Left>", left)
fen.bind("<Right>", right)
fen.bind("<Up>", up)
fen.bind("<Down>", down)


Label(fen, text='RECORD = 410 points ', font="weight=BOLD").grid(row=0, sticky=W, padx=10)
lb_pts = Label(fen, text='Points = aucun')
lb_pts.grid(row=0, column=1, sticky=E, padx=20)
canv = Canvas(fen, width=600, height=400, bg='green')
canv.grid(row=1, column=0, columnspan=2)
Button(fen, text='Nouvelle Partie', command=commencer).grid(row=2, column=0, padx=30, pady=30)
Button(fen, text='Quitter', command=fen.quit).grid(row=2, column=1, padx=30, pady=30)

# Main :
fen.mainloop()

# After main :
fen.destroy()

