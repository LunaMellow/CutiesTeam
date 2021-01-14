# Hi, this is our first project.
# So far we do not have any plans or ongoing projects,
# so if you have a good concept idea, put it in "ideas.txt"
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("Scripty script GUI")
        self.pack(fill = BOTH, expand = 1)

        menu = Menu(self.master)
        self.master.config(menu = menu)

        file = Menu(menu)
        file.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label = "File", menu = file)

        edit = Menu(menu)
        edit.add_command(label = "Show Message", command = self.showTxt)
        menu.add_cascade(label = "Edit", menu = edit)

    def showTxt(self):
        text = Label(self, text = "You're a nonce lmeow")
        text.pack()
    
    def client_exit(self):
        exit()

root = Tk()
root.geometry("300x30")
app = Window(root)
root.mainloop()
