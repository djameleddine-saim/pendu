import random
import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pendu")

errors = 0
pressed_key = []

def choose_the_word():
    word = open("words.txt", "r")
    word = word.readlines()
    return word
word = choose_the_word()

list_count = len(word) - 1
num = random.randint(0, list_count)

res = ''.join(word[num].splitlines())

founded_letters = []
errors_letter = []
win = 0


def easy(num):
    global win
    global win_count

    if errors < 10 or win != win_count:
        if num == 1:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
        if num == 2:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
        if num == 3:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
        if num == 4:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
        if num == 5:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
        if num == 6:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
        if num == 7:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 270), (175, 230), 8)
        if num == 8:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 270), (175, 230), 8)
            pygame.draw.line(window, (0, 0, 0), (150, 270), (175, 230), 8)
        if num == 9:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 270), (175, 230), 8)
            pygame.draw.line(window, (0, 0, 0), (150, 270), (175, 230), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 370), (175, 320), 8)

def medium(num):
    global win
    global win_count

    if errors < 7 or win != win_count:
        if num == 1:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
        if num == 2:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
        if num == 3:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
        if num == 4:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
        if num == 5:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 270), (175, 230), 8)
        if num == 6:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 270), (175, 230), 8)
            pygame.draw.line(window, (0, 0, 0), (150, 270), (175, 230), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 370), (175, 320), 8)


def hard(num):
    global win
    global win_count

    if errors < 5 or win != win_count:
        if num == 1:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
        if num == 2:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
        if num == 3:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 270), (175, 230), 8)
        if num == 4:
            pygame.draw.line(window, (0, 0, 0), (10, 500), (300, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (50, 150), (50, 500), 8)
            pygame.draw.line(window, (0, 0, 0), (40, 150), (350, 150), 8)
            pygame.draw.line(window, (0, 0, 0), (175, 150), (175, 180), 8)
            pygame.draw.circle(window, (0, 0, 0), (175, 200), 25, 8)
            pygame.draw.line(window, (0, 0, 0), (175, 225), (175, 325), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 270), (175, 230), 8)
            pygame.draw.line(window, (0, 0, 0), (150, 270), (175, 230), 8)
            pygame.draw.line(window, (0, 0, 0), (200, 370), (175, 320), 8)
win_count = 0

win_list = []

i = 0

while i < len(res):
    if res.count(res[i]) == 1:
        if win_list.count(res[i]) == 0:
            win_list.append(res[i])
            win_count += 1
            i += 1
        else:
            i += 1
    elif res.count(res[i]) >= 1:
        if win_list.count(res[i]) == 0:
            win_list.append(res[i])
            win_count += 1
            i += 1
        else:
            i += 1

running = True

menu = 1

while running:

    pygame.time.Clock().tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and ((event.unicode >= 'a' and event.unicode <= 'z') or (
                event.unicode >= 'A' and event.unicode <= 'Z')):
            letter = event.unicode
            if letter in win_list:
                if founded_letters.count(letter) == 0:
                    founded_letters.append(letter)
                    win += 1
                else:
                    pass
            else:
                errors_letter.append(letter)
                errors += 1
        else:
            pass

    window.fill((255, 255, 255))
    printed_word = ""
    new_word = []

    if menu == 1:
        title = pygame.font.Font(None, 80).render("Bienvenue !!!", True, (255, 0, 0))
        window.blit(title, (200, 50))

        play = pygame.font.Font(None, 40).render("Nouveau jeu", True, (0, 0, 0), (255, 0, 0))
        window.blit(play, (165, 200))

        add_word = pygame.font.Font(None, 40).render("Ajouter un mot", True, (0, 0, 0), (255, 0, 0))
        window.blit(add_word, (165, 250))

        x, y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 165 and y > 200 and x < 340 and y < 220):
            menu = 2

        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 165 and y > 250 and x < 370 and y < 270):
            running2 = True
            word_added = False
            while running2:

                for event in pygame.event.get():

                    x, y = pygame.mouse.get_pos()

                    if event.type == pygame.QUIT:
                        running2 = False
                        running = False
                    if pygame.mouse.get_pressed()[0] and (x > 195 and y > 500 and x < 300 and y < 520):
                        if not word_added:
                            with open('words.txt', 'a') as file:
                                file.write(''.join(new_word) + '\n')
                        word_added = True
                        running2 = False

                    if event.type == pygame.KEYDOWN:
                        if (event.unicode >= 'a' and event.unicode <= 'z') or (
                                event.unicode >= 'A' and event.unicode <= 'Z'):
                            letter = event.unicode
                            new_word.append(letter)

                        elif event.key == pygame.K_BACKSPACE:
                            if len(new_word) > 0:
                                new_word = new_word[:-1]
                            else:
                                pass

                window.fill((255, 255, 255))

                title = pygame.font.Font(None, 80).render("Bienvenue !!!", True, (255, 0, 0))
                window.blit(title, (200, 50))

                add_word = pygame.font.Font(None, 40).render("Tapez le mot", True, (0, 0, 0), (255, 0, 0))
                window.blit(add_word, (190, 250))

                printed_new_word = pygame.font.Font(None, 40).render(''.join(new_word), True, (0, 0, 0), )
                window.blit(printed_new_word, (150, 400))

                rect = pygame.Rect(20, 390, 700, 50)
                pygame.draw.rect(window, (255, 0, 0), rect, 2)

                validate = pygame.font.Font(None, 40).render("valider", True, (0, 0, 0), (255, 0, 0))
                window.blit(validate, (200, 500))

                pygame.display.flip()

    if menu == 2:

        play_easy = pygame.font.Font(None, 40).render("facile", True, (0, 0, 0), (255, 0, 0))
        window.blit(play_easy, (465, 200))
        play_medium = pygame.font.Font(None, 40).render("moyen", True, (0, 0, 0), (255, 0, 0))
        window.blit(play_medium, (465, 300))
        play_hard = pygame.font.Font(None, 40).render("difficile", True, (0, 0, 0), (255, 0, 0))
        window.blit(play_hard, (465, 400))

        x, y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 465 and y > 200 and x < 540 and y < 220):
            menu = 3
        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 465 and y > 300 and x < 540 and y < 320):
            menu = 4
        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 465 and y > 400 and x < 540 and y < 420):
            menu = 5

                                        #__________________________________________________________________________#

    if (errors < 10 or win != win_count) and menu == 3:
        for letter in res:
            if letter in founded_letters:
                printed_word += letter + " "
            else:
                printed_word += "_ "

            if errors < 10 and win < win_count:
                easy(errors)
            word_text = pygame.font.Font(None, 36).render(printed_word, True, (0, 0, 0))
            window.blit(word_text, (50, 50))

            errors_text = pygame.font.Font(None, 36).render("Mauvaises lettres : " + ' '.join(errors_letter), True,
                                                            (0, 0, 0))
            window.blit(errors_text, (50, 100))

        if win == win_count:
            easy(errors)
            you_win = pygame.font.Font(None, 36).render("Bravo Vous Avez Gagnez !", True, (0, 255, 0))
            window.blit(you_win, (190, 250))
            check = 1
            event = pygame.event.wait()

        if errors >= 10:
            easy(errors)
            game_over = pygame.font.Font(None, 36).render("Vous Avez Perdu !", True, (219, 32, 2))
            window.blit(game_over, (190, 250))
            check = 1
            event = pygame.event.wait()

        try_levels = pygame.font.Font(None, 30).render("niveaux facile : 10 essaye", True, (0, 0, 0), (255, 0, 0))
        window.blit(try_levels, (500, 50))

        replay = pygame.font.Font(None, 40).render("Rejouer", True, (0, 0, 0), (255, 0, 0))
        window.blit(replay, (365, 500))
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 365 and y > 500 and x < 440 and y < 520):
            menu = 1
            founded_letters = []
            errors_letter = []
            errors = 0
            win = 0

            word = choose_the_word()
            list_count = len(word) - 1
            num = random.randint(0, list_count)
            res = ''.join(word[num].splitlines())

        #_______________________________________________________________________________________________________________________#


    elif (errors < 7 or win != win_count) and menu == 4:
        for letter in res:
            if letter in founded_letters:
                printed_word += letter + " "
            else:
                printed_word += "_ "
            if errors < 7 and win < win_count:
                medium(errors)
            word_text = pygame.font.Font(None, 36).render(printed_word, True, (0, 0, 0))
            window.blit(word_text, (50, 50))

            errors_text = pygame.font.Font(None, 36).render("Mauvaises lettres : " + ' '.join(errors_letter), True,
                                                            (0, 0, 0))
            window.blit(errors_text, (50, 100))

        if win == win_count:
            medium(errors)
            you_win = pygame.font.Font(None, 36).render("Bravo Vous Avez Gagnez !", True, (0, 255, 0))
            window.blit(you_win, (190, 250))
            check = 1
            event = pygame.event.wait()

        if errors >= 7:
            medium(errors)
            game_over = pygame.font.Font(None, 36).render("Vous Avez Perdu !", True, (219, 32, 2))
            window.blit(game_over, (190, 250))
            check = 1
            event = pygame.event.wait()

        try_levels = pygame.font.Font(None, 30).render("niveaux moyen : 7 essaye", True, (0, 0, 0), (255, 0, 0))
        window.blit(try_levels, (500, 50))

        replay = pygame.font.Font(None, 40).render("Rejouer", True, (0, 0, 0), (255, 0, 0))
        window.blit(replay, (365, 500))
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 365 and y > 500 and x < 440 and y < 520):
            menu = 1
            founded_letters = []
            errors_letter = []
            errors = 0
            win = 0

            word = choose_the_word()
            list_count = len(word) - 1
            num = random.randint(0, list_count)
            res = ''.join(word[num].splitlines())

                                #_____________________________________________________________________________________#
            
    elif (errors < 5 or win != win_count) and menu == 5:
        for letter in res:
            if letter in founded_letters:
                printed_word += letter + " "
            else:
                printed_word += "_ "
            if errors < 5 and win < win_count:
                hard(errors)
            word_text = pygame.font.Font(None, 36).render(printed_word, True, (0, 0, 0))
            window.blit(word_text, (50, 50))

            errors_text = pygame.font.Font(None, 36).render("Mauvaises lettres : " + ' '.join(errors_letter), True,
                                                            (0, 0, 0))
            window.blit(errors_text, (50, 100))

        if win == win_count:
            hard(errors)
            you_win = pygame.font.Font(None, 36).render("Bravo Vous Avez Gagnez !", True, (0, 255, 0))
            window.blit(you_win, (190, 250))
            check = 1
            event = pygame.event.wait()

        if errors >= 5:
            hard(errors)
            game_over = pygame.font.Font(None, 36).render("Vous Avez Perdu !", True, (219, 32, 2))
            window.blit(game_over, (190, 250))
            check = 1
            event = pygame.event.wait()

        try_levels = pygame.font.Font(None, 30).render("niveaux difficile : 5 essaye", True, (0, 0, 0), (255, 0, 0))
        window.blit(try_levels, (500, 50))

        replay = pygame.font.Font(None, 40).render("Rejouer", True, (0, 0, 0), (255, 0, 0))
        window.blit(replay, (365, 500))
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 365 and y > 500 and x < 440 and y < 520):
            menu = 1
            founded_letters = []
            errors_letter = []
            errors = 0
            win = 0

            word = choose_the_word()
            list_count = len(word) - 1
            num = random.randint(0, list_count)
            res = ''.join(word[num].splitlines())


    pygame.display.update()

pygame.quit()