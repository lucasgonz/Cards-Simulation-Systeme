import random


class Croupier:

    signe = ['♠', '♣', '♥', '♦']
    figure = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'Q', 'K', 'A']
    cartes = []
    cleanDeck = []

    def __init__(self):
        self.cleanDeck = self.init_deck()
        self.cartes = list(self.cleanDeck)
        random.shuffle(self.cleanDeck)

    # Random shuffle from module library
    def shuffle(self):
        random.shuffle(self.cartes)

    # print cards in array
    def show_cartes(self):
        return print(self.cartes)

    # Return array of cards from deck . Optional remove
    def pige_carte(self, nb_carte, remove=False):

        cartes_piged=[]
        for i in range(nb_carte):
            index = random.randrange(len(self.cartes))
            cartes_piged.append(self.cartes[index])
            if remove: del self.cartes[index]
        return cartes_piged

    # Return array of Cards : Deck construction from signe and figure array
    def init_deck(self):
        # Clean deck
        cartes = []
        # Deck construction
        for signe in self.signe:
            for figure in self.figure:
                cartes.append(figure + signe)
        return cartes

    # Replace deck with clean one stored in memory
    def new_deck(self):
        self.cartes = list(self.cleanDeck)

    # Return strongest from 2 cards
    def strongest_card(self, card1, card2):
        for rank in self.figure:
            if rank in card1[0]:
                return card1
            if rank in card2[0]:
                return card2

    # Return array of index sorted : compare position in original array
    def rank_cards(self, cards):

        ranked=[]
        for card in cards:
            if '10' in card:
                ranked.append(int(self.figure.index('10')))
            else:
                ranked.append(int(self.figure.index(card[0])))
        ranked.sort()
        return ranked

    # Return Bool subset of 3 in array
    def subset_in_array(self, array):

        limit = 2
        for i in range(len(array) - 1):
            if array[i + 1] == array[i] + 1:
                limit -= 1
            else:
                limit = 2
            if limit == 0: return True

        return False