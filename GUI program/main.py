from tkinter import *

window = Tk()
window.title("First tkinter")
window.wm_minsize(width=600, height=400)

my_label = Label(text="It's my label", font=("Arial", 16, "bold"))
my_label.pack()


def button_click():
    new_text = input.get()
    my_label["text"] = new_text




my_button = Button(text="click me", command=button_click)
my_button.pack()

input = Entry(width= 10)
input.pack()

window.mainloop()
