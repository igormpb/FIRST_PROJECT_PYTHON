import random

def fruits():
    fruits = open('fruits.txt', 'r')
    fruits_list = []

    for line in fruits:
        line = line.strip()
        line = line.lower()
        fruits_list.append(line)

    return fruits_list

def generated_fruit(fruits_list):
    # shows the secret fruit
    fruits_all = len(fruits_list)
    random_number = random.randrange(0, fruits_all);
    fruit = fruits_list[random_number]
    return fruit

def fruit_line_genarated(fruit):

    # responsible for creating the word size on the screen
    lettrs_list = ["_" for letters in fruit]
    print(lettrs_list)
    return lettrs_list

def game_screen(lettrs_list, fruit):

    hanged = False
    hit = False
    erros = 6

    while (not hanged and not hit):
        str_option = str(input('Try to hit the fruit: '))
        str_option = str_option.strip()
        index = 0
        if (str_option in fruit):
            for Char in fruit:
                if (str_option.lower() == Char.lower()):
                    lettrs_list[index] = Char
                index += 1
        else:
            print("you have {} chance".format(erros))
            erros -= 1
        hanged = erros == 0
        hit = "_" not in lettrs_list
        print(lettrs_list)
        if(hanged):
            print('You lost, secret fruit is {}'.format(fruit))
        elif(hit):
            print('You won')

    print("End game")

def jogar():

    ("############################")
    print("############################")

    print("hit a fruit")

    print("#############################")
    print("#############################")

    fruits_list = fruits()
    fruit = generated_fruit(fruits_list)
    lettrs_list = fruit_line_genarated(fruit)

    game_screen(lettrs_list,fruit)


if (__name__ == '__main__'):
    jogar()