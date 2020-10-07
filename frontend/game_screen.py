from datetime import datetime
import time
import copy
import json

import tkinter as tk

import backend.sudoku_generator as sg
from frontend.other_screens import WinScreen


class GameScreen:
    def __init__(self, master, user):
        
        def _draw_grid(window):
            self.c = tk.Canvas(window)
            self.c.configure(bg="black")
            self.c.place(x=45,y=45,width=470,height=470)

            self.boxes = []
            r = 0
            x_pos = 50
            y_pos = 50
            for i in range(81):
                self.boxes.append(tk.Entry(window,justify='center'))
                self.boxes[i].place(x=x_pos,y=y_pos,width=50,height=50)
                if (i+1)%9 == 0:
                    x_pos = 50
                    y_pos += 50
                    r += 1
                elif (i+1)%3 == 0:
                    x_pos += 55
                else:
                    x_pos += 50
                if r == 3:
                    y_pos += 5
                    r = 0

        self.current_user = user

        self.master = master
        self.master.wm_title("Sudoku!")
        self.master.geometry("730x550")
        _draw_grid(self.master)

        self.button1 = tk.Button(self.master,text='New puzzle',command=self.generate)
        self.button2 = tk.Button(self.master,text="Check",command=self.check)
        self.button3 = tk.Button(self.master,text="Solve it for me!",command=self.solve)
        self.label1 = tk.Label(self.master,text="Select difficulty:")
        self.label2 = tk.Label(self.master,text="Time lapsed:")
        self.label3 = tk.Label(self.master,text="00:00")

        self.difficulty = tk.StringVar(self.master)
        self.difficulty.set("Beginner")
        self.list1 = tk.OptionMenu(self.master,self.difficulty,"Beginner","Intermediate","Advanced")

        self.button1.place(x=520, y=205, width=200, height=50)
        self.button2.place(x=520,y=255,width=200,height=50)
        self.button3.place(x=520,y=305,width=200,height=50)
        self.label1.place(x=570,y=50,width=100,height=25)
        self.label2.place(x=570,y=405,width=100,height=25)
        self.label3.place(x=570,y=425,width=100,height=50)
        self.list1.place(x=565,y=75,width=110,height=25)

    def generate(self):
        try:
            self.master.after_cancel(self.last_job)
        except AttributeError:
            pass

        self.solved = False

        for box in self.boxes:
            box.config(state='normal')
            box.config({'background':'white'})

        if self.difficulty.get() == "Beginner":
            filled = 40
            self.score = 5000
        elif self.difficulty.get() == "Intermediate":
            filled = 35
            self.score = 6000
        elif self.difficulty.get() == "Advanced":
            filled = 28
            self.score = 7000

        self.new_grid = sg.init_grid()
        self.new_grid_frozen = copy.deepcopy(self.new_grid) 
        sg.generate_puzzle(self.new_grid, self.new_grid_frozen, filled)

        self.start_time = datetime.now()
        self.update_clock()

        i = 0
        for box in self.boxes:
            box.delete(0,tk.END)
            num = self.new_grid[i//9][i%9]
            if num is not 0:
                box.insert(tk.END,str(num))
                box.config(state='disabled')
            i += 1

    def check(self):
        try:
            self.solved = True
            i = 0
            for box in self.boxes:
                try:
                    num = self.new_grid_frozen[i//9][i%9]
                    if int(box.get()) == num:
                        box.config(state='disabled')
                    else:
                        box.config({'background':'red'})
                        if self.score > 0:
                            self.score -= 100
                        self.solved = False
                except ValueError:
                    self.solved = False
                i += 1
            if self.solved:
                self.newWindow = tk.Tk()
                WinScreen(self.newWindow,self.score)
                self.master.after_cancel(self.last_job)
                users = json.load(open('users.json'))
                if self.score > users[self.current_user]["high score"]:
                    users[self.current_user]["high score"] = self.score
                file = open('users.json','w')
                json.dump(users,file)
            else:
                if self.score > 0:
                    self.score -= 50
        except AttributeError:
            pass

    def solve(self):
        self.score = 0
        self.solved = True
        try:
            self.master.after_cancel(self.last_job)
            i=0
            for box in self.boxes:
                num = self.new_grid_frozen[i//9][i%9]
                box.delete(0,tk.END)
                box.insert(tk.END,str(num))
                box.config({'background':'white'})
                i += 1
        except AttributeError:
            pass 

    def update_clock(self):
        if self.score > 0:
            self.score -= 5
        time_passed = (datetime.now() - self.start_time).total_seconds()
        self.label3.configure(text=time.strftime('%M:%S',time.gmtime(time_passed)))
        self.last_job = self.master.after(1000, self.update_clock)