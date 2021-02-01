import numpy as np


class Jeux:

    # Constructor

    def __init__(self, player, croupier):
        self.player = player
        self.croupier = croupier
        self.croupier.new_deck()
        self.croupier.shuffle()

    # Pioche 1 carte si As => win +10 $

    def jeux_1(self, times):

        self.player.clear()

        for i in range(times):
            cartes = self.croupier.pige_carte(1)
            win = True if 'A' in cartes[0] else False
            # (bool , cost, potential gain)
            self.player.update_win_loss(win, 1, 10)
        self.result(times)
        self.clear_Game()

    # Pioche 2 carte si identique => +50 (avec remise)$

    def jeux_2(self, times):

        self.player.clear()

        for i in range(times):
            cartes = np.array(self.croupier.pige_carte(2))
            win = np.all(cartes == cartes[0])
            self.player.update_win_loss(win,1,50)

        self.result(times)
        self.clear_Game()

    # Pioche 2 carte : Si 2ie carte > 1 carte => + 2 $ (sans remise)

    def jeux_3(self, times):

        self.player.clear()
        self.croupier.figure.reverse()

        for i in range(times):
            first_c = self.croupier.pige_carte(1, remove=True)
            second_c = self.croupier.pige_carte(1, remove=True)
            strongest = self.croupier.strongest_card(first_c, second_c)
            win = True if second_c == strongest else False
            self.player.update_win_loss(win,1,2)
            self.clear_Game()

        self.result(times)

    def jeux_4(self, times):

        self.player.clear()

        for i in range(times):
            cards = self.croupier.pige_carte(3, remove=True)
            heart = sum('♥' in s for s in cards)
            win = True if heart > 0 else False
            self.player.update_win_loss(win, 1, heart)
            self.clear_Game()

        self.result(times)

    def jeux_5(self, times):

        self.player.clear()

        for i in range(times):
            cartes = self.croupier.pige_carte(5, remove=True)
            ranked = self.croupier.rank_cards(cartes)
            subsetInCards = self.croupier.subset_in_array(ranked)
            win = True if subsetInCards else False
            self.player.update_win_loss(win, 1, 5)
            self.clear_Game()

        self.result(times)

    # function print final result of game

    def result(self, ITERATION):

        print("\n> For " + str(ITERATION) + " games played " +
              ": WIN : " + str(len(self.player.win)) +
              " , LOSS : " + str(len(self.player.loss)) +
              " , WINRATE : " + str(self.player.win_rate()) +
              " , MONNEY : " + str(self.player.monney) + ' $')

    def clear_Game(self):
        self.croupier.new_deck()
        self.croupier.shuffle()

