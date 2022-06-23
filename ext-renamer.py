#!/usr/bin/env python3

import os

path = input("Dans quel path executer le code ?\n")

current_ext = input("Quelle extension cherchez-vous à modifier ? (ex .jpeg, .jfif, ...) \n")
new_ext = input("Quelle nouvelle extension mettre à la place ? (ex .jpeg, .jfif, ...) \n")

i = 0

for dossier, sous_dossiers, fichiers in os.walk(path):
    for fichier in fichiers:
        if fichier.endswith(current_ext):
            base = os.path.splitext(fichier)[0]
            new_name = base + new_ext
            os.rename(dossier + '/' + fichier, dossier + '/' + new_name)
            print(' Ancien nom : ' + fichier + '\n Nouveau nom : ' + new_name)
            print('###')
            i += 1
if i <= 1:
    print(str(i) + ' fichier a été modifié')
elif i > 1:
    print(str(i) + ' fichiers ont été modifiés')
