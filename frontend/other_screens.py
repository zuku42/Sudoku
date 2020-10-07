import json

import tkinter as tk


class WinScreen():
    def __init__(self,master,score):
        self.score = score
        self.master = master
        self.master.geometry('200x100')

        self.label1 = tk.Label(self.master,text="Congratulations!")
        self.label2 = tk.Label(self.master,text=f"Your score: {self.score}")

        self.label1.place(x=50,y=30,width=100,height=20)
        self.label2.place(x=50,y=50,width=100,height=20)


class LeaderboardScreen():
    def __init__(self,master):
        self.master = master
        self.user_scores = json.load(open('users.json'))
        scores = [(self.user_scores[key]['high score'], key) for key in self.user_scores.keys()]
        scores.sort()
        self.labels = []
        i = 0
        for item in reversed(scores):
            self.labels.append(tk.Label(self.master,text=str(i+1)+"."+str(item[1])+" "+str(item[0])))
            self.labels[i].place(x=50,y=20*i,width=100,height=20)
            i += 1