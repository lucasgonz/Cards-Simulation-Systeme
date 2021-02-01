import numpy as np


class Jeux:

    # Constructor
    def __init__(self, player, croupier):
        self.player = player
        self.croupier = croupier
        # Create new deck
        self.croupier.new_deck()
        # Shuffle deck randomly
        self.croupier.shuffle()

    # Pige 1 carte : if As => win +10 $
    def jeux_1(self, times):

        self.player.clear()
        for i in range(times):
            # Pige 1 card
            cartes = self.croupier.pige_carte(1)
            # Si As return win
            win = True if 'A' in cartes[0] else False
            # Update Player Gain
            self.player.update_win_loss(win, 1, 10)

        # Output and refresh for next game
        self.result(times)
        self.clear_Game()

    # Pige 2 carte avec remise : if same => +50 $
    def jeux_2(self, times):
        # Clear player gain from previous games
        self.player.clear()

        for i in range(times):
            # Pige two cards sans remise
            cartes = np.array(self.croupier.pige_carte(2))
            # win bool True si identique else false
            win = np.all(cartes == cartes[0])
            # Update Player gain
            self.player.update_win_loss(win, 1, 50)

        # Output and refresh for next game
        self.result(times)
        self.clear_Game()

    # Pige 2 carte sans remise : if 2nd carte > 1 carte => + 2 $

    def jeux_3(self, times):
        # Clear player gain from previous games
        self.player.clear()
        # Reverse figure pour algo strongest Card
        self.croupier.figure.reverse()

        for i in range(times):
            # Pige deux carte
            first_c = self.croupier.pige_carte(1, remove=True)
            second_c = self.croupier.pige_carte(1, remove=True)
            # Check strongest
            strongest = self.croupier.strongest_card(first_c, second_c)
            # Win if second is strongest
            win = True if second_c == strongest else False
            self.player.update_win_loss(win, 1, 2)
            # Refresh cards
            self.clear_Game()

        self.result(times)

    # Pige 3 cartes sans remise : if n-coeur is > 1 coeur : win n-coeur $
    def jeux_4(self, times):
        # Clear player gain from previous games
        self.player.clear()

        for i in range(times):
            # Pige 3 cartes sans remise
            cards = self.croupier.pige_carte(3, remove=True)
            # Count nb of hearts
            heart = sum('♥' in s for s in cards)
            # Si superior a 1 win
            win = True if heart > 0 else False
            # Update Gain / Loss
            self.player.update_win_loss(win, 1, heart)
            self.clear_Game()

        self.result(times)

    # Pige 5 Carte sans remise : if (sous ensemble serie consecutive de 3 (5-6-7) ) win 5 $ else loose
    def jeux_5(self, times):
        # Clear player gain from previous games
        self.player.clear()

        for i in range(times):
            # Pige 5 cards without remise
            cartes = self.croupier.pige_carte(5, remove=True)
            # Get index rank in reference list and order them
            ranked = self.croupier.rank_cards(cartes)
            # If 3 consecutive number in sorted array return subset true
            subsetInCards = self.croupier.subset_in_array(ranked)
            win = True if subsetInCards else False
            # Update player gain / loss
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

    # New deck dans shuffle
    def clear_Game(self):
        self.croupier.new_deck()
        self.croupier.shuffle()

