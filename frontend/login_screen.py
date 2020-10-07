import json

import tkinter as tk

from frontend.game_screen import GameScreen
from frontend.other_screens import LeaderboardScreen


class LoginScreen:
    def __init__(self, master):
        self.master = master
        self.master.wm_title("Sudoku!")
        self.master.geometry("460x100")

        self.label1 = tk.Label(self.master,text="Create a new player:")
        self.label2 = tk.Label(self.master,text="Select an existing player:")
        self.entry1 = tk.Entry(self.master)
        self.button1 = tk.Button(self.master,text="Play",command=self.game_window)
        self.button2 = tk.Button(self.master,text="Submit",command=self.add_user)
        self.button3 = tk.Button(self.master,text="Leaderboard",command=self.leaderboard_window)

        self.user_options = list(json.load(open("users.json")))
        self.users = tk.StringVar(self.master)
        self.users.trace_add('write', lambda *args: self.users.get())
        self.users.set(self.user_options[-1])
        self.list1 = tk.OptionMenu(self.master,self.users,*self.user_options)

        self.label1.place(x=10, y=10, width=150, height=20)
        self.label2.place(x=10,y=40,width=150,height=20)
        self.entry1.place(x=160, y=10, width=150, height=20)
        self.button1.place(x=330,y=40,width=80,height=20)
        self.button2.place(x=330, y=10, width=80, height=20)
        self.button3.place(x=160,y=70,width=150,height=20)
        self.list1.place(x=160,y=40,width=150,height=20)

    def game_window(self):
        GameScreen(tk.Tk(),self.users.get())
        self.master.destroy()

    def leaderboard_window(self):
        LeaderboardScreen(tk.Tk())

    def add_user(self):
        if not (self.entry1.get() == "" or self.entry1.get().isspace()):
            username = self.entry1.get()
            self.user_options.append(username)
            users = json.load(open("users.json"))
            users[username] = {"username":username,"high score": 0}
            file = open("users.json","w")
            json.dump(users,file)
            file.close
            self.list1['menu'].delete(0,'end')
            self.users.set(self.user_options[-1])
            for option in self.user_options:
                self.list1['menu'].add_command(label=option, command=tk._setit(self.users, option))