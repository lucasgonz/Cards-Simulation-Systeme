from Croupier import Croupier
from Jeux import Jeux
from Joueur import Joueur


# Config variables
ITERATION = 100000

player = Joueur()
croupier = Croupier()
jeux = Jeux(player, croupier)

# Main loop

jeux.jeux_1(ITERATION)
jeux.jeux_2(ITERATION)
jeux.jeux_3(ITERATION)
jeux.jeux_4(ITERATION)
jeux.jeux_5(ITERATION)








