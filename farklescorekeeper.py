import tkinter as t
from tkinter import Frame
import createnewplayer as p


class App:
    # initialization inside class
    def __init__(s, r):
        # s = standard
        # r = root
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
        # start game button
        s.startgame = t.Button(f, text="Start Game", command=s.startgamewindow)
        s.startgame.pack(side="top", pady=5)

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
    # function to open new window

    def startgamewindow(s):
        gamewindow = t.Toplevel()  # create a new window
        gamewindow.title("FarkleScore.exe")
        gamewindow.geometry("500x500")
        statusframe = Frame(gamewindow)
        statusframe.pack()
        t.Label(statusframe, text="Game Status").pack()
        # printing list of players
        t.Label(statusframe, text="\n".join(str(p)
                for p in s.players)).pack()
        entryframe = Frame(gamewindow)
        entryframe.pack(side="top")
        fframe = Frame(gamewindow)
        fframe.pack(side="top")
        sframe = Frame(gamewindow)
        sframe.pack(side="top")
        tframe = Frame(gamewindow)
        tframe.pack(side="top")
        s.PointEntry = t.Entry(entryframe)
        s.Erase = t.Button(entryframe, text="C")
        s.Bank = t.Button(entryframe, text="Bank", bg="green")
        s.Farkle = t.Button(entryframe, text="Farkle", bg="red")
        s.PointEntry.pack(side="left")
        s.Bank.pack(side="right")
        s.Farkle.pack(side="right")
        s.Erase.pack(side="right", ipadx=5)
        s.Ones = t.Button(fframe, text="Ones")
        s.Fives = t.Button(fframe, text="Fives")
        s.ThreeOnes = t.Button(sframe, text="3Ones")
        s.ThreeTwos = t.Button(sframe, text="3Twos")
        s.ThreeThrees = t.Button(sframe, text="3Threes")
        s.ThreeFours = t.Button(sframe, text="3Fours")
        s.ThreeFives = t.Button(sframe, text="3Fives")
        s.ThreeSixes = t.Button(sframe, text="3Sixes")
        s.FourofaKind = t.Button(tframe, text="4Kind")
        s.FiveofaKind = t.Button(tframe, text="5Kind")
        s.SixofaKind = t.Button(tframe, text="6Kind")
        s.ThreePair = t.Button(tframe, text="3Pair")
        s.TwoTriplet = t.Button(tframe, text="2Triple")
        s.Straight = t.Button(tframe, text="Straight")
        s.Ones.pack(side="left")
        s.Fives.pack(side="left")
        s.ThreeOnes.pack(side="left")
        s.ThreeTwos.pack(side="left")
        s.ThreeThrees.pack(side="left")
        s.ThreeFours.pack(side="left")
        s.ThreeFives.pack(side="left")
        s.ThreeSixes.pack(side="left")
        s.FourofaKind.pack(side="left")
        s.FiveofaKind.pack(side="left")
        s.SixofaKind.pack(side="left")
        s.ThreePair.pack(side="left")
        s.TwoTriplet.pack(side="left")
        s.Straight.pack(side="left")


r = t.Tk()
r.geometry("500x500")
r.title('Farkle Score Keeper')
app = App(r)
r.mainloop()
