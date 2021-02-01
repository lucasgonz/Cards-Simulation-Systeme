

class Joueur:

    # Default start win 0 Winn - 0 Loss - 100 $
    def __init__(self, win=[], loss=[], monney = 100):
        self.win = win
        self.loss = loss
        self.monney = monney

    # Remove cost from money : if win add potential gain
    def update_win_loss(self, win, cost, gain):
        self.monney -= cost

        if win:
            self.win.append(win)
            self.monney += gain
        else:
            self.loss.append(win)

    # Return float win rate given nbWin and nbLoss
    def win_rate(self):
        nb_games = len(self.win)+len(self.loss)
        return (len(self.win) / nb_games) * 100

    # Refresh player variables
    def clear(self):
        self.monney = 100
        self.win = []
        self.loss = []


