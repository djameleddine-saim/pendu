import random
import pygame

# Initialiser la librairie Pygame
pygame.init()

# Créer la fenêtre du jeu et Définir le titre de la fenêtre
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pendu")

# le nombre de tentatives incorrectes
errors = 0

# Fonction pour choisir un mot dans le fichier texte
def choose_the_word():
    word = open("words.txt", "r")
    word = word.readlines()
    return word

# Récupérer la liste des mots du fichier texte
word = choose_the_word()

# Obtenir le nombre de mots dans la liste
list_count = len(word) - 1
# Choisissez un mot au hasard dans la liste
num = random.randint(0, list_count)
res = ''.join(word[num].splitlines())

# Liste pour garder les lettres correctement choisies
founded_letters = []
# Liste pour garder les lettres mal choisies
errors_letter = []

# dessine des éléments du jeu du pendu en fonction du nombre de coups ratés (num) de (0 à 9)
# par rapport aux niveaux facile
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

# dessine des éléments du jeu du pendu en fonction du nombre de coups ratés (num) de (0 à 7)
# par rapport aux niveaux moyen
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

# dessine des éléments du jeu du pendu en fonction du nombre de coups ratés (num) de (0 à 4)
# par rapport aux niveaux difficile
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

# Initialisation des variables win count et win list
win_count = 0
win_list = []

# Initialisation d'un compteur de boucle
i = 0

# Boucle while pour parcourir la liste res et ajouter les mots gagnants à la liste win_list
while i < len(res):
    # Si le mot apparaît une seule fois dans la liste res
    if res.count(res[i]) == 1:
        # Si le mot n'est pas encore dans la liste win_list
        if win_list.count(res[i]) == 0:
            # Ajout du mot à la liste win_list et incrémentation de win_count
            win_list.append(res[i])
            win_count += 1
            i += 1
        else:
            i += 1
    # Si le mot apparaît plus d'une fois dans la liste res
    elif res.count(res[i]) >= 1:
        # Si le mot n'est pas encore dans la liste win_list
        if win_list.count(res[i]) == 0:
            # Ajout du mot à la liste win_list et incrémentation de win_count
            win_list.append(res[i])
            win_count += 1
            i += 1
        else:
            i += 1

# Initialisation de la variable running pour déterminer si la boucle while suivante est en cours d'exécution
running = True
# Initialisation de la variable menu pour déterminer la page affiché à l'utilisateur
menu = 1

# Boucle while principale pour gérer l'affichage du jeu
while running:

    # Définition de la vitesse d'actualisation de la fenêtre à 20 images par seconde
    pygame.time.Clock().tick(20)
    # Boucle for pour parcourir les événements de pygame
    for event in pygame.event.get():
        # Si l'utilisateur clique sur la croix pour quitter le jeu
        if event.type == pygame.QUIT:
            running = False
        # Si l'utilisateur appuie sur une touche alphabétique
        if event.type == pygame.KEYDOWN and ((event.unicode >= 'a' and event.unicode <= 'z') or (event.unicode >= 'A' and event.unicode <= 'Z')):
            # Stockage de la lettre appuyée
            letter = event.unicode
            # Si la lettre appuyée est dans la liste des mots gagnants
            if letter in win_list:
                # Si la lettre n'a pas encore été trouvée
                if founded_letters.count(letter) == 0:
                    # Ajout de la lettre à la liste founded_letters et incrémentation
                    founded_letters.append(letter)
                    win += 1
                else:
                    # Si la lettre a déjà été trouvée, ne rien faire
                    pass
            else:
                # Si la lettre n'est pas dans les mots gagnants
                # Ajouter la lettre aux erreurs
                errors_letter.append(letter)
                # Incrémenter le nombre d'erreurs
                errors += 1
        else:
            # Si l'utilisateur n'a pas appuyé sur une touche alphabétique, ne rien faire
            pass
    # remplir le fond de couleur blanche
    window.fill((255, 255, 255))
    # initialise les variables print_word et new_word
    printed_word = ""
    new_word = []

    # si le menu est dans le premier état (menu == 1)
    if menu == 1:
        # Afficher le titre "Bienvenue !!!"
        title = pygame.font.Font(None, 80).render("Bienvenue !!!", True, (255, 0, 0))
        window.blit(title, (200, 50))
        # Afficher le titre "Nouveau jeu"
        play = pygame.font.Font(None, 40).render("Nouveau jeu", True, (0, 0, 0), (255, 0, 0))
        window.blit(play, (165, 200))
        # Afficher le titre "Ajouter un mot"
        add_word = pygame.font.Font(None, 40).render("Ajouter un mot", True, (0, 0, 0), (255, 0, 0))
        window.blit(add_word, (165, 250))

        # obtenir la position actuelle de la souris
        x, y = pygame.mouse.get_pos()
        # si le bouton gauche de la souris est enfoncé et que la souris est sur le texte "Nouveau jeu"
        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 165 and y > 200 and x < 340 and y < 220):
            # passe le menu au deuxième état
            menu = 2
        # si le bouton gauche de la souris est enfoncé et que la souris est sur le texte "Ajouter un mot"
        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 165 and y > 250 and x < 370 and y < 270):
            # démarrer la boucle interne (running2)
            running2 = True
            word_added = False
            while running2:
                # gérer les événements
                for event in pygame.event.get():
                    # obtenir la position actuelle de la souris
                    x, y = pygame.mouse.get_pos()
                    # si le type d'événement est QUIT (c'est-à-dire que l'utilisateur ferme la fenêtre)
                    if event.type == pygame.QUIT:
                        # terminer les boucles intérieures et extérieures
                        running2 = False
                        running = False
                    # si le bouton gauche de la souris est enfoncé et que la souris est sur le texte "valider"
                    if pygame.mouse.get_pressed()[0] and (x > 195 and y > 500 and x < 300 and y < 520):
                        # si le mot n'a pas encore été ajouté au fichier
                        if not word_added:
                            # ouvrez le fichier words.txt en mode ajout et ajoutez le nouveau mot
                            with open('words.txt', 'a') as file:
                                file.write(''.join(new_word) + '\n')
                        # Mise à jour de l'état du programme pour indiquer que le mot a été ajouté
                        word_added = True
                        running2 = False

                    # Gestion des événements de touche
                    if event.type == pygame.KEYDOWN:
                        # Si l'utilisateur tape une lettre, elle est ajoutée au nouveau mot
                        if (event.unicode >= 'a' and event.unicode <= 'z') or (
                                event.unicode >= 'A' and event.unicode <= 'Z'):
                            letter = event.unicode
                            new_word.append(letter)
                        # Si l'utilisateur tape la touche backspace, la dernière lettre du nouveau mot est supprimée
                        elif event.key == pygame.K_BACKSPACE:
                            if len(new_word) > 0:
                                new_word = new_word[:-1]
                            else:
                                pass

                window.fill((255, 255, 255))

                title = pygame.font.Font(None, 80).render("Bienvenue !!!", True, (255, 0, 0))
                window.blit(title, (200, 50))

                # Afficher le titre "Tapez le mot"
                add_word = pygame.font.Font(None, 40).render("Tapez le mot", True, (0, 0, 0), (255, 0, 0))
                window.blit(add_word, (190, 250))
                # Afficher le nouveau mot
                printed_new_word = pygame.font.Font(None, 40).render(''.join(new_word), True, (0, 0, 0), )
                window.blit(printed_new_word, (150, 400))

                # Dessiner un rectangle rouge autour du nouveau mot
                rect = pygame.Rect(20, 390, 700, 50)
                pygame.draw.rect(window, (255, 0, 0), rect, 2)

                # créer le titre "valider"
                validate = pygame.font.Font(None, 40).render("valider", True, (0, 0, 0), (255, 0, 0))
                window.blit(validate, (200, 500))

                # Mettre à jour l'affichage de la fenêtre de jeu
                pygame.display.flip()

    # Si le menu est sélectionné à 2 afficher les options de niveau de difficulté
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

                                        #____________________________________________________________________________#
                                            # Si le menu est sélectionné à 3 commence a jouer sur le niveaux facile

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

        # la condition qui vérifie si vous avez perdu
        if win == win_count:
            easy(errors)
            you_win = pygame.font.Font(None, 36).render("Bravo Vous Avez Gagnez !", True, (0, 255, 0))
            window.blit(you_win, (190, 250))
            check = 1
            event = pygame.event.wait()

        # la condition qui vérifie si vous avez gagné
        if errors >= 10:
            easy(errors)
            game_over = pygame.font.Font(None, 36).render("Vous Avez Perdu !", True, (219, 32, 2))
            window.blit(game_over, (190, 250))
            check = 1
            event = pygame.event.wait()
        # Afficher le titre "niveaux facile : 10 essaye"
        try_levels = pygame.font.Font(None, 30).render("niveaux facile : 10 essaye", True, (0, 0, 0), (255, 0, 0))
        window.blit(try_levels, (500, 50))

        # Afficher le titre "Rejouer"
        replay = pygame.font.Font(None, 40).render("Rejouer", True, (0, 0, 0), (255, 0, 0))
        window.blit(replay, (365, 500))
        x, y = pygame.mouse.get_pos()
        # si le bouton gauche de la souris est enfoncé et que la souris est sur le texte "Rejouer"
        if pygame.mouse.get_pressed() == (1, 0, 0) and (x > 365 and y > 500 and x < 440 and y < 520):
            # en revient au menu 1 et réinitialiser tout les element de jeux
            menu = 1
            founded_letters = []
            errors_letter = []
            errors = 0
            win = 0
            # réinitialiser le mot
            word = choose_the_word()
            list_count = len(word) - 1
            num = random.randint(0, list_count)
            res = ''.join(word[num].splitlines())

                                             # ____________________________________________________________________________#
                                                # Si le menu est sélectionné à 4 commence a jouer sur le niveaux moyen


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

                                 # ____________________________________________________________________________#
                                    # Si le menu est sélectionné à 4 commence a jouer sur le niveaux difficile

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
