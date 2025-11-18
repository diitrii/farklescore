import tkinter as t
from tkinter import Frame
import createnewplayer as p


class App:
    # initialization inside class
    def __init__(s, r):
        s.r = r
        # define player array
        s.players = []
        # entry widget for typing name
        t.Label(r, text="Enter player name: ").pack()
        s.e = t.Entry(r)
        s.e.pack()
        # frame to pack plus and minus
        f = Frame(r)
        f.pack()
        # button for player creation
        s.b1 = t.Button(f, text=" + ", command=s.createplayer)
        s.b1.pack(side="left", padx=5)
        # button to remove last created player
        s.b2 = t.Button(f, text=" - ", command=s.removeplayer)
        s.b2.pack(side="right", padx=5)
        # output area
        s.o = t.Label(r, text="", justify="left")
        s.o.pack()

    def createplayer(s):
        typedname = s.e.get().strip()
        # reject if no name entry
        if typedname == "":
            s.o.config(text="Please enter name.")
            return
        # create instance of player
        player = p.Player(typedname)
        s.players.append(player)
        # delete entry box
        s.e.delete(0, t.END)
        # show player list
        s.o.config(text="\n".join(str(p) for p in s.players))

    def removeplayer(s):
        if (s.players == []):
            s.o.config(text="No players to remove.")
            return
        s.players.pop(-1)
        s.o.config(text="\n".join(str(p) for p in s.players))


r = t.Tk()
r.geometry("500x500")
app = App(r)
r.mainloop()
