from tkinter import *

root = Tk()

canvas = Canvas(root, width = '600', height = '600')
canvas.pack()

def callback():
    print ('click!')

b = Button(root, text="OK", command=callback, background = "green", font = 'sans-serif')
b.pack()

label_text = Label(text = 'Add')
label_text.place(x=100, y=150)
entry_text = Entry(root, width = '40')
entry_text.place(x=150, y=150)

button_list = Button (root, text='List', width = '20', height = '2', background = "red", font = 'sans-serif')
button_list.place(x=50, y=50)
button_remove = Button (root, text='Remove', width = '10', height = '2', background = "yellow", font = 'sans-serif')
button_remove.place(x=100, y =250)
button_check = Button (root, text='Check', width = '10', height = '2', background = "pink", font = 'sans-serif')
button_check.place(x=100, y=350)

root.mainloop()
