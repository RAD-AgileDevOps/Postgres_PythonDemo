import psycopg2 as pg2

import pandas as pd
import matplotlib as mp
from matplotlib import pyplot as plt
import numpy as np
from tkinter import Tk, BOTH, Entry, Label, NORMAL, Button
from tkinter.ttk import Frame
from PIL import Image, ImageTk
from tkinter import messagebox


class postgres_conn(Frame):
    last_name: Entry

    def __init__(self):
        super().__init__()
        self.last_update = None
        self.initUI()
        self.pg_gui()
        self.conn = pg2.connect("dbname=dvdrental user=postgres password=pEfr8mER")

        if self.conn:
            print("connection successful")

        self.curr = self.conn.cursor()

        # self.savetodb()
        txt = 'A.N.Company Employees Database'
        # self.lbl = Label(self, )
        self.label1 = Label(self, text=txt, state=NORMAL, fg='white', justify='center', bg='#3F3FBF', width=300,
                            font="Verdana 40 bold italic")
        # self.label1.grid()
        self.label1.pack(fill='both', expand=False)

        self.lblactor_id = Label(self, text='Actor ID')
        self.lblactor_id.place(x=10, y=130)
        self.actor_id = Entry(self, width=40)
        self.actor_id.place(x=100, y=130)

        self.lblFName = Label(self, text='First Name')
        self.lblFName.place(x=10, y=160)
        self.first_name = Entry(self, width=40)
        self.first_name.place(x=100, y=160)

        self.lblLName = Label(self, text='Last Name')
        self.lblLName.place(x=10, y=190)
        self.last_name = Entry(self, width=40)
        self.last_name.place(x=100, y=190)

        self.lblast_update = Label(self, text='Last Updated')
        self.lblast_update.place(x=10, y=220)
        self.last_update = Entry(self, width=40)
        self.last_update.place(x=100, y=220)
        self.submit_btn = Button(self, text='New Employee', command=self.submit, height=5, width=20 ,bg="turquoise")
        self.submit_btn.place(x=100, y=450)

    def __del__(self):
        self.conn.close()

    def submit(self):
        self.conn = pg2.connect("dbname=dvdrental user=postgres password=pEfr8mER")

        self.curr = self.conn.cursor()
        # txtName.get() will get the value in the entry box
        # entry_name = self.first_name.get()
        self.curr.execute("INSERT INTO   actor VALUES (%s, %s , %s , %s)",

                          (
                              self.actor_id.get(),
                              self.first_name.get(),
                              self.last_name.get(),
                              self.last_update.get()

                          )
                          )
        self.curr.execute("SELECT first_name from actor")
        print(self.curr.fetchone())
        self.conn.commit()

    def initUI(self):
        self.master.title("RAD Financial System -  Demo GUI")
        self.pack(fill=BOTH, expand=1)

    def pg_gui(self):
        rot_i = Image.open(r"RAFS_Bland_gitHub_v3.jpg")
        rotunda = ImageTk.PhotoImage(rot_i)

        label = Label(image=rotunda)
        label.image = rotunda
        label.place(x=520, y=130)

    # function to be called when button is clicked
    def savetodb(self):
        pass


def main():
    root = Tk()
    root.geometry("1200x300+100+100")
    app = postgres_conn()
    root.mainloop()


if __name__ == '__main__':
    main()
