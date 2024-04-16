from tkinter import *
from tkinter.ttk import Combobox 
import jinja2
import sys

window = Tk()
window.frame()
window.geometry("250x100")
window.resizable(False, False)

frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)

class pp:

    def __init__(self, values: str) -> None:
        self.values = {}
        for i in values.split("\n"):

            if i == "":
                continue

            self.values[i.split("=")[0]] = i.split("=")[1]

        self.tt = "PProp"
        self.tb = []
        self.nw_values = self.values.copy()

    def textbox(self, pos, arg):

        textbox = Entry(frame)
        textbox.insert(0, arg)
        textbox.config(state=DISABLED)

        def click(event):
            textbox.config(state=NORMAL)
            textbox.delete(0, END)

        textbox.bind("<Button-1>", click)

        textbox.grid(column=pos[0], row=pos[1])
        self.tb.append([textbox, arg])

    def submit(self, pos, text="submit"):

        def event_submit(event):
            for i in self.tb:
                if i[1] != i[0].get():
                    self.nw_values[i[1]] = i[0].get()
                else:
                    self.nw_values[i[1]] = ""

            prop = open("property.pprop", "r", encoding="utf-8")
            v = prop.read()

            for i in self.values:
                if self.nw_values[i] != "":
                    v = v.replace(f"{i}={self.values[i]}", f"{i}={self.nw_values[i]}")

            prop.close()
            prop = open("property.pprop", "w", encoding="utf-8")
            prop.write(v)
            prop.close()
            sys.exit(0)
                
        bt = Button(frame, text=text)
        bt.grid(column=pos[0], row=pos[1])
        bt.bind("<Button-1>", event_submit)

    def title(self, text="Pprop"):
        self.tt = text

    def label(self, pos, text):
        lb = Label(frame, text=text)
        lb.grid(column=pos[0], row=pos[1])

    def icon(self, path):
        window.iconbitmap(path)

    def geometry(self, geometry):
        window.geometry(geometry)

    def combobox(self, pos, arguments, var):
        combobox = Combobox(frame, values=arguments, state="readonly")
        combobox.grid(column=pos[0], row=pos[1])

        self.tb.append([combobox, var])


with open("property.pprop", "r", encoding="utf-8") as prop:
    jv = prop.read().split("prettyproperty;")
    ts = pp(jv[0])
    jinja2.Template(jv[1]).render(pp=ts)

    cc = ts
    window.title(cc.tt)

window.mainloop()
