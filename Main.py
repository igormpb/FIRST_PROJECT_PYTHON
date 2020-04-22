import Adivinhacao
import Forca

jogo = int(input('(1) Divination number (2) Try fruit '))

if(jogo == 1):
    print('wellcome')
    Adivinhacao.jogar()
elif(jogo == 2):
    print('Wellcome!')
    Forca.jogar()
