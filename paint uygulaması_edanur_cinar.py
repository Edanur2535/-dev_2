import cv2
import numpy as np
from tkinter import *
from tkinter import colorchooser, filedialog
from PIL import ImageGrab



def paint(event):
    global kalemboyu
    kalemboyu=sli.get()
    x1, y1, x2, y2 = (event.x-kalemboyu), (event.y-kalemboyu), (event.x+kalemboyu), (event.y+kalemboyu)
    canvas2.create_oval(x1, y1, x2, y2, fill = kalemrengi, outline = kalemrengi)
def renkdegis(yeni_renk):
    global kalemrengi
    kalemrengi = yeni_renk


def renk_kutusu():
    id  = canvas.create_rectangle((10, 10, 30, 30), fill='black')
    canvas.tag_bind(id, "<Button-1>", lambda x: renkdegis("black"))
    id  = canvas.create_rectangle((40, 10, 60, 30), fill='red')
    canvas.tag_bind(id, "<Button-1>", lambda x: renkdegis("red"))
    id = canvas.create_rectangle((70, 10, 90, 30), fill='yellow')
    canvas.tag_bind(id, "<Button-1>", lambda x: renkdegis('yellow'))
    id = canvas.create_rectangle((100, 10, 120, 30), fill='pink')
    canvas.tag_bind(id, "<Button-1>", lambda x: renkdegis("pink"))
    id = canvas.create_rectangle((130, 10, 150, 30), fill='blue')
    canvas.tag_bind(id, "<Button-1>", lambda x: renkdegis("blue"))
    id = canvas.create_rectangle((160, 10, 180, 30), fill='green')
    canvas.tag_bind(id, "<Button-1>", lambda x: renkdegis("green"))
    id = canvas.create_rectangle((190, 10, 210, 30), fill='grey')
    canvas.tag_bind(id, "<Button-1>", lambda x: renkdegis("grey"))
    id = canvas.create_rectangle((220, 10, 240, 30), fill='orange')
    canvas.tag_bind(id, "<Button-1>", lambda x: renkdegis("orange"))
def temizle():
    canvas2.delete(ALL)
    canvas2.configure(bg="white")
def kaydet():
    file=filedialog.asksaveasfilename(filetypes=[("JPG","*.jpg")], defaultextension="jpg")
    ImageGrab.grab(bbox=(x_coordinate+130, y_coordinate+135, x_coordinate+pencere_width+280, y_coordinate+pencere_height+280)).save(file)
def renksec():
    global kalemrengi
    yeni_kalemrengi=colorchooser.askcolor(initialcolor="#00ff00", title="Renk Seçin")[1]
    kalemrengi=yeni_kalemrengi
def arkaalanrengisec():
    global arkaplanrengi
    yeni_arkaplanrengi = colorchooser.askcolor(initialcolor="#00ff00", title="Renk Seçin")[1]
    canvas2.configure(bg=yeni_arkaplanrengi)

pencere = Tk()
pencere.title("Paint Uygulaması")
pencere_width = 800
pencere_height = 600
screen_width = pencere.winfo_screenwidth()
screen_height = pencere.winfo_screenheight()
x_coordinate = int(screen_width / 2 - pencere_width / 2)
y_coordinate = int(screen_height / 2 - pencere_height / 2)
pencere.geometry("{}x{}+{}+{}".format(pencere_width, pencere_width, x_coordinate, y_coordinate))
kalemrengi = "green"
kalemboyu=5
canvas = Canvas(pencere, width=700, height=50)
canvas.pack()
canvas2 = Canvas(pencere, width=700, height=550, background="white")
canvas2.pack()
canvas2.bind('<B1-Motion>', paint)
Button(pencere, text="Sayfayı Temizle" ,command=temizle, background="purple").place(x=300, y=8)
Button(pencere, text="Kaydet" ,command=kaydet, background="pink").place(x=400, y=8)
Button(pencere, text="Kalem Rengi" ,command=renksec, background="lightblue").place(x=600, y=8)
Button(pencere, text="Arka Plan Rengi" ,command=arkaalanrengisec, background="pink").place(x=700, y=8)
sli=Scale(pencere, from_=1, to=30, orient=HORIZONTAL)
sli.place(x=470, y=-8)
sli.set(kalemboyu)
renk_kutusu()
mainloop()
