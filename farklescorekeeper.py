import tkinter as t
from tkinter import Frame
import createnewplayer as p


class App:
    # initialization inside class
    def __init__(s, r):
        # s = standard
        # r = root
        s.unbankedscore = t.IntVar()
        s.undopoints = 0
        s.r = r
        # define player array
        s.players = []
        # track amount players
        s.currentplayerindex = 0
        # entry widget for typing name
        t.Label(r, text="Enter player name: ").pack()
        s.e = t.Entry(r)
        s.e.pack()
        # frame to pack plus and minus
        f = Frame(r)
        f.pack()
        f1 = Frame(f)
        f1.pack()
        f2 = Frame(f)
        f2.pack()
        # button for player creation
        s.b1 = t.Button(f1, text=" + ", command=s.createplayer)
        s.b1.pack(side="left", padx=5)
        # button to remove last created player
        s.b2 = t.Button(f1, text=" - ", command=s.removeplayer)
        s.b2.pack(side="right", padx=5)
        # output area
        s.o = t.Label(r, text="", justify="left")
        s.o.pack()
        # start game button
        s.startgame = t.Button(f2, text="Start Game",
                               command=s.startgamewindow)
        s.startgame.pack(side="top", pady=5)

    # creating a new player
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

    # remove last created player
    def removeplayer(s):
        if (s.players == []):
            s.o.config(text="No players to remove.")
            return
        s.players.pop(-1)
        s.o.config(text="\n".join(str(p) for p in s.players))

    # erase text entry in scoring state
    def eraseentry(s):
        s.PointEntry.delete(0, 'end')
        s.unbankedscore.set(value=0)

    # update status of player scores
    def updatestatus(s):
        # creates display of players, has marker to selected player
        display = []
        for i, player in enumerate(s.players):
            marker = " <-" if i == s.currentplayerindex else ""
            display.append(f"{player}{marker}")
        s.statuslabel.config(text="\n".join(display))

    def undobutton(s):
        # go back one player
        s.currentplayerindex = (s.currentplayerindex - 1) % len(s.players)
        prev_player = s.players[s.currentplayerindex]
        if prev_player.Points > 0:
            prev_player.Points -= s.undopoints
        s.updatestatus()
        # bank points from players

    def bankpoints(s):
        # check if no players
        if not s.players:
            s.o.config(text="No players in game.")
            return
        # get entered points
        points_str = s.PointEntry.get().strip()

        if not points_str.isdigit():
            s.o.config(text="Enter a valid number.")
            return

        points = int(points_str)

        # bank points to current player
        current_player = s.players[s.currentplayerindex]
        current_player.Points += points
        s.undopoints = current_player.Points

        # clear entry
        s.eraseentry()

        # move to next player (wrap around)
        s.currentplayerindex = (s.currentplayerindex + 1) % len(s.players)

        # update player status
        s.updatestatus()

    # function to switch players in the case of a Farkle
    def switchturn(s):
        # move to next player
        s.currentplayerindex = (s.currentplayerindex + 1) % len(s.players)
        s.eraseentry()
        # update player status
        s.updatestatus()

    # add 100 to score (ones)
    def addones(s):
        s.unbankedscore.set(s.unbankedscore.get()+100)

    # add 50 to score (fives)
    def addfives(s):
        s.unbankedscore.set(s.unbankedscore.get()+50)

    # add 300 to score (3 ones, 3 threes)
    def addthreehundred(s):
        s.unbankedscore.set(s.unbankedscore.get()+300)

    # add 200 to score (3 twos)
    def addtwohundred(s):
        s.unbankedscore.set(s.unbankedscore.get()+200)

    # add 400 to score (3 fours)
    def addfourhundred(s):
        s.unbankedscore.set(s.unbankedscore.get()+400)

    # add 500 to score (3 fives)
    def addfivehundred(s):
        s.unbankedscore.set(s.unbankedscore.get()+500)

    # add 600 to score (3 sixes)
    def addsixhundred(s):
        s.unbankedscore.set(s.unbankedscore.get()+600)

    # add 1000 to score (4 of a kind)
    def fourkind(s):
        s.unbankedscore.set(s.unbankedscore.get()+1000)

    # add 2000 to score (5 of a kind)
    def fivekind(s):
        s.unbankedscore.set(s.unbankedscore.get()+2000)

    # add 3000 to score (6 of a kind)
    def sixkind(s):
        s.unbankedscore.set(s.unbankedscore.get()+3000)

    # add 1500 to score (3 pairs or straight)
    def addfifteenhundred(s):
        s.unbankedscore.set(s.unbankedscore.get()+1500)

    # add 2500 to score (2 triplets)
    def addtwentyfivehundred(s):
        s.unbankedscore.set(s.unbankedscore.get()+2500)

    # function to open new window
    def startgamewindow(s):
        # create a new window
        gamewindow = t.Toplevel()
        gamewindow.title("FarkleScore.exe")
        gamewindow.geometry("500x500")
        # frame inside window for score state
        statusframe = Frame(gamewindow)
        statusframe.pack()
        t.Label(statusframe, text="Game Status").pack()
        # printing list of players that updates
        s.statuslabel = t.Label(statusframe, text="")
        s.statuslabel.pack()
        s.updatestatus()
        # frame for entry
        entryframe = Frame(gamewindow)
        entryframe.pack(side="top")
        # fancy frame
        fframe = Frame(gamewindow)
        fframe.pack(side="top")
        # fancy frame
        sframe = Frame(gamewindow)
        sframe.pack(side="top")
        # fancy frame
        tframe = Frame(gamewindow)
        tframe.pack(side="top")
        s.PointEntry = t.Entry(entryframe, textvariable=s.unbankedscore)
        s.PointEntry.pack()
        # button that deletes anything entered into the entry command
        s.Erase = t.Button(
            fframe, text="C", command=s.eraseentry, width=50, height=50)
        s.Erase.pack(side="left")
        # button that banks points from the entry command into a player's points
        s.Bank = t.Button(fframe, text="Bank",
                          command=s.bankpoints, bg='#37cc3e')
        s.Bank.pack(side="left")
        # button to switch players in the case of a Farkle
        s.Farkle = t.Button(fframe, text="Farkled",
                            command=s.switchturn, bg='#ce0d0d')
        s.Farkle.pack(side="left")
        s.Ones = t.Button(sframe, text="One", command=s.addones)
        s.Ones.pack(side="left")
        s.Fives = t.Button(sframe, text="Five", command=s.addfives)
        s.Fives.pack(side="left")
        s.ThreeOnes = t.Button(sframe, text="3Ones", command=s.addthreehundred)
        s.ThreeOnes.pack(side="left")
        s.ThreeTwos = t.Button(sframe, text="3Twos", command=s.addtwohundred)
        s.ThreeTwos.pack(side="left")
        s.ThreeThrees = t.Button(
            sframe, text="3Three", command=s.addthreehundred)
        s.ThreeThrees.pack(side="left")
        s.ThreeFours = t.Button(sframe, text="3Fours",
                                command=s.addfourhundred)
        s.ThreeFours.pack(side="left")
        s.ThreeFives = t.Button(sframe, text="3Fives",
                                command=s.addfivehundred)
        s.ThreeFives.pack(side="left")
        s.ThreeSixes = t.Button(sframe, text="3Sixes", command=s.addsixhundred)
        s.ThreeSixes.pack(side="left")
        s.FourKind = t.Button(tframe, text="4Kind", command=s.fourkind)
        s.FourKind.pack(side="left")
        s.FiveKind = t.Button(tframe, text="5Kind", command=s.fivekind)
        s.FiveKind.pack(side="left")
        s.SixKind = t.Button(tframe, text="6Kind", command=s.sixkind)
        s.SixKind.pack(side="left")
        s.Straight = t.Button(tframe, text="Straight 1-6",
                              command=s.addfifteenhundred)
        s.Straight.pack(side="left")
        s.ThreePairs = t.Button(
            tframe, text="3Pairs", command=s.addfifteenhundred)
        s.ThreePairs.pack(side="left")
        s.TwoTriplets = t.Button(
            tframe, text="2Triplets", command=s.addtwentyfivehundred)
        s.TwoTriplets.pack(side="left")
        s.FourKindAndPair = t.Button(
            tframe, text="4Kind + Pair", command=s.addfifteenhundred)
        s.FourKindAndPair.pack(side="left")
        s.Undo = t.Button(fframe, text="Undo", command=s.undobutton)
        s.Undo.pack(side="left")


r = t.Tk()
r.geometry("500x500")
r.title('Farkle Score Keeper')
app = App(r)
r.mainloop()
