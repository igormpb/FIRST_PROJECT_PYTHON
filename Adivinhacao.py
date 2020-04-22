import random
def jogar():

    print("############################")
    print("############################")

    print("choose a number from 1 to 50")

    print("#############################")
    print("#############################")


    # generate number for game
    random_number = int(random.randrange(1, 100));
    secret_number = random_number
    #

    points = 200;
    tentative = 3;
    for Round in range(1, tentative + 1):
        print('tentative {} '.format(Round));
        option_int = int(input('type it number: '));

        if (option_int == secret_number):
            print("You won, your points are {0} !".format(points));
            break
        else:
            print('You lost!');
            lost_points = abs(secret_number - option_int);
            points -= lost_points;
            continue;

    print('end game');

if(__name__ == '__main__'):
    jogar()