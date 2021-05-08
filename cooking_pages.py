from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("How to cook Chana Masala")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='c:/icon/cook.png'))
root.geometry("1000x700")

image0 = PhotoImage(file='c:/icon/image0.png')
background_1 = Label(root, image=image0, anchor = "nw")
background_1.grid(row = 10, column = 10)

frame = tk.Frame(root)

image1 = PhotoImage(file='c:/icon/chole1.png')
image2 = PhotoImage(file = 'c:/icon/pan1.png')
image3 = PhotoImage(file = 'c:/icon/slice1.png')
image4 = PhotoImage(file = 'c:/icon/spices.png')
image5 = PhotoImage(file = 'c:/icon/chef.png')
image6 = PhotoImage(file = 'c:/icon/done.png')


C = Canvas(frame, bg="blue", height=250, width=300)
filename = PhotoImage(file='c:/icon/chole1.png')
background_label = Label(frame, image=filename, anchor = "nw")
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#my_label = Label(root, image = image1)
#my_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
#my_text = Label(root, text = "Checklist and Ingredients", font = 1000, anchor = "center")
#my_text.place(x = 100, y = 90)

#my_canvas = Canvas(root, height=250, width=300)
#my_canvas.pack(fill="both", expand=True)

#my_canvas.create_image(0, 0, image=image1, anchor="nw")
#my_label.create_text(500, 100, text="Checklist and Ingredients", anchor="center", font=100, fill="maroon")


#button1 = Button(root, text="start", anchor = "se", font = 100)
#button1.place(x = 850, y = 80)
#button2 = Button(root, text="back", anchor = "se", font = 100)
#button2.place(x = 800, y = 80)

def timer():
    my_timer = Label(root, text = "Time Up!!", fg = "red", font = 50)
    my_timer.place(x = 250, y = 250)


def opening():
    my_label = Label(root, image=image1)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_text = Label(root, text="Checklist and Ingredients", font=1000, anchor="center")
    my_text.place(x=100, y=90)


    i1 = Checkbutton(root, text="Chickpeas", font=25, bg="light yellow")
    i1.place(relx=0.1, rely=0.2)

    i2 = Checkbutton(root, text="Garam Masala", font=25, bg="light yellow")
    i2.place(relx=0.1, rely=0.3)

    i3 = Checkbutton(root, text="Sliced Tomatoes", font=25, bg="light yellow")
    i3.place(relx=0.1, rely=0.4)

    i4 = Checkbutton(root, text="Sliced Onions", font=25, bg="light yellow")
    i4.place(relx=0.1, rely=0.5)

    i5 = Checkbutton(root, text="Mustard Seeds", font=25, bg="light yellow")
    i5.place(relx=0.1, rely=0.6)

    i6 = Checkbutton(root, text="Salt", font=25, bg="light yellow")
    i6.place(relx=0.1, rely=0.7)

    i7 = Checkbutton(root, text="Chili Powder", font=25, bg="light yellow")
    i7.place(relx=0.1, rely=0.8)

    i8 = Checkbutton(root, text="Turmeric Powder", font=25, bg="light yellow")
    i8.place(relx=0.1, rely=0.9)

    button0 = Button(root, text="opening page", command=opening)
    button0.grid(row=0, column=0)

    button1 = Button(root, text="page 1", command=page1)
    button1.grid(row=0, column=1)

    button2 = Button(root, text="page 2", command=page2)
    button2.grid(row=0, column=2)

    button3 = Button(root, text="page 3", command=page3)
    button3.grid(row=0, column=3)

    button4 = Button(root, text="page 4", command=page4)
    button4.grid(row=0, column=4)

    button5 = Button(root, text="page 5", command=page5)
    button5.grid(row=0, column=5)


def page1():
    my_label = Label(root, image=image2)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_text = Label(root, text="heat the pan and add some oil", font=1000, fg = "green")
    my_text.place(x=100, y=90)

    button0 = Button(root, text="opening page", command=opening)
    button0.grid(row=0, column=0)

    button1 = Button(root, text="page 1", command=page1)
    button1.grid(row=0, column=1)

    button2 = Button(root, text="page 2", command=page2)
    button2.grid(row=0, column=2)

    button3 = Button(root, text="page 3", command=page3)
    button3.grid(row=0, column=3)

    button4 = Button(root, text="page 4", command=page4)
    button4.grid(row=0, column=4)

    button5 = Button(root, text="page 5", command=page5)
    button5.grid(row=0, column=5)


def page2():
    my_label = Label(root, image=image3)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_text = Label(root, text="add some sliced onions and tomatoes, this slide will automatically change after 3 minutes", font=1000, anchor="center")
    my_text.place(x=100, y=90)

    # adding a timer for 3 minutes to go on next slide
    root.after(1800, timer)
    root.after(3000, page3)

    button0 = Button(root, text="opening page", command=opening)
    button0.grid(row=0, column=0)

    button1 = Button(root, text="page 1", command=page1)
    button1.grid(row=0, column=1)

    button2 = Button(root, text="page 2", command=page2)
    button2.grid(row=0, column=2)

    button3 = Button(root, text="page 3", command=page3)
    button3.grid(row=0, column=3)

    button4 = Button(root, text="page 4", command=page4)
    button4.grid(row=0, column=4)

    button5 = Button(root, text="page 5", command=page5)
    button5.grid(row=0, column=5)



def page3():
    my_label = Label(root, image=image4)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_text = Label(root, text="after waiting 3 minutes, add Garam masala, turmeric, salt, chili powder, wait for another 5 minutes", font=1000, anchor="center")
    my_text.place(x=100, y=90)

    # adding a timer for 5 minutes to go on next slide
    root.after(3000, page4)

    button0 = Button(root, text="opening page", command=opening)
    button0.grid(row=0, column=0)

    button1 = Button(root, text="page 1", command=page1)
    button1.grid(row=0, column=1)

    button2 = Button(root, text="page 2", command=page2)
    button2.grid(row=0, column=2)

    button3 = Button(root, text="page 3", command=page3)
    button3.grid(row=0, column=3)

    button4 = Button(root, text="page 4", command=page4)
    button4.grid(row=0, column=4)

    button5 = Button(root, text="page 5", command=page5)
    button5.grid(row=0, column=5)

def page4():
    my_label = Label(root, image=image5)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_text = Label(root, text=" add chickpeas and steam for 10 minutes ", font=1000, anchor="center")
    my_text.place(x=100, y=90)

    # adding a timer for 10 minutes to go on next slide
    root.after(6000, page5)

    button0 = Button(root, text="opening page", command=opening)
    button0.grid(row=0, column=0)

    button1 = Button(root, text="page 1", command=page1)
    button1.grid(row=0, column=1)

    button2 = Button(root, text="page 2", command=page2)
    button2.grid(row=0, column=2)

    button3 = Button(root, text="page 3", command=page3)
    button3.grid(row=0, column=3)

    button4 = Button(root, text="page 4", command=page4)
    button4.grid(row=0, column=4)

    button5 = Button(root, text="page 5", command=page5)
    button5.grid(row=0, column=5)

def page5():
    my_label = Label(root, image=image6)
    my_label.place(x=0, y=0, relwidth=1, relheight=1)
    my_text = Label(root, text=" Ready to serve ", font=1000, anchor="center")
    my_text.place(x=100, y=90)

    button0 = Button(root, text="opening page", command=opening)
    button0.grid(row=0, column=0)

    button1 = Button(root, text="page 1", command=page1)
    button1.grid(row=0, column=1)

    button2 = Button(root, text="page 2", command=page2)
    button2.grid(row=0, column=2)

    button3 = Button(root, text="page 3", command=page3)
    button3.grid(row=0, column=3)

    button4 = Button(root, text="page 4", command=page4)
    button4.grid(row=0, column=4)

    button5 = Button(root, text="page 5", command=page5)
    button5.grid(row=0, column=5)

#def start():
    #global button1
    #global button2
    #global my_label
   # global my_text

  #  my_label.grid_forget()
   # button1 = Button(root, text="start", anchor="se", font=100, command = page1)
   # button1.place(x = 850, y = 80)

button0 = Button(root, text = "opening page", command = opening)
button0.grid(row = 0, column = 0)

button1 = Button(root, text = "page 1", command = page1)
button1.grid(row = 0, column = 1)

button2 = Button(root, text = "page 2", command = page2)
button2.grid(row = 0, column = 2)

button3 = Button(root, text="page 3", command=page3)
button3.grid(row=0, column=3)

button4 = Button(root, text="page 4", command=page4)
button4.grid(row=0, column=4)

button5 = Button(root, text="page 5", command=page5)
button5.grid(row=0, column=5)

#btn3 = Button(root, text = "page 3",  command = page3)
#btn3.grid(row = 0, column = 3)

root.mainloop()
