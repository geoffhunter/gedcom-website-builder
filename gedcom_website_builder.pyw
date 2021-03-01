from tkinter import *
import ged_lib as gl
import process_document_images as pdi
import create_tree as ct

want_ui = True

def clicked1():
    gl.process_ged_file()

def clicked2():
    gl.process_ged_file()
    pdi.process_document_images()
    ct.create_tree()

def exit():
    root.destroy()

if want_ui:
    font = "Tahoma"
    font_size = 10
    root = Tk()
    root.title("")
    root.geometry('370x450') #width, height
    f00 = Label(root, text=" V1.00",font=(font, font_size))
    f00.grid(row=0, column=0)
    space1 = Label(root, text="  ",font=(font, 10))
    space1.grid(row=1, column=1)
    heading = Label(root, text="Family Tree Website Builder",font=(font, font_size))
    heading.grid(row=2, column=1)
    space2 = Label(root, text=" ",font=(font, font_size))
    space2.grid(row=3, column=1)
    button1 = Button(root, text=" Process GED File ", font=(font, font_size), command=clicked1)
    button1.grid(row=4, column=1)
    space3 = Label(root, text=" ",font=(font, font_size))
    space3.grid(row=5, column=1)
    button2 = Button(root, text="   Build Website  ", font=(font, font_size), command=clicked2)
    button2.grid(row=6, column=1)
    space4 = Label(root, text=" ",font=(font, font_size))
    space4.grid(row=7, column=1)
    button3 = Button(root, text="          Exit         ", font=(font, font_size), command=exit)
    button3.grid(row=8, column=1)
    space5 = Label(root, text=" ",font=(font, font_size))
    space5.grid(row=9, column=1)
    button4 = Button(root, text=" Edit Parameters ", font=(font, font_size), command=gl.edit_params)
    button4.grid(row=10, column=1)
    root.mainloop()
else:
    gl.process_ged_file()
    pdi.process_document_images()
    ct.create_tree()
