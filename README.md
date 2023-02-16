# pendu

Ce code est un jeu de pendu en Python utilisant la bibliothèque Pygame pour créer une interface graphique. Le jeu choisit un mot aléatoire à partir d'un fichier texte, puis le joueur doit deviner le mot en entrant une lettre à la fois. Pour chaque lettre incorrecte, une partie du dessin d'un pendu est dessinée, jusqu'à ce que le dessin soit complet ou que le joueur ait deviné correctement le mot.

La fonction "choose_the_word" ouvre un fichier texte "words.txt" et retourne une liste de mots. La fonction "easy" dessine des éléments du pendu en fonction du nombre de coups ratés (stockés dans la variable "num"). Le jeu est conçu pour être facile, car il ne dessine que 10 éléments au maximum (pour chaque tentative incorrecte). Les lettres correctement choisies sont stockées dans une liste appelée "founded_letters", et les lettres incorrectes sont stockées dans une liste appelée "errors_letter".
