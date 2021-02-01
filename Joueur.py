

class Joueur:

    def __init__(self, win=[], loss=[], monney = 100):
        self.win = win
        self.loss = loss
        self.monney = monney

    def update_win_loss(self, win, cost, gain):

        self.monney -= cost

        if win:
            self.win.append(win)
            self.monney += gain
        else:
            self.loss.append(win)

    def win_rate(self):
        nb_games = len(self.win)+len(self.loss)
        return (len(self.win) / nb_games) * 100

    def clear(self):
        self.monney = 100
        self.win = []
        self.loss = []


