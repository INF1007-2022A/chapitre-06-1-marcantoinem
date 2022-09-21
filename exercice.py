#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = []
        while len(values) < 10:
            print("Entrez une valeur SVP:")
            values.append(input())
    str_value = [float(value) for value in values if value.isdigit()]
    num_value = [value for value in values if not value.isdigit()]
    return sorted(str_value) + sorted(num_value)
    


def anagrams(words: list = None) -> bool:
    if words is None:
        print("Entrez un mot SVP:")
        word1 = input()
        print("Entrez un mot SVP:")
        word2 = input()
        pass

    return sorted(word1) == sorted(word2)


def contains_doubles(items: list) -> bool:
    values = []
    for item in items:
        if item in values:
            return True
        else:
            values.append(item)

    return false


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_average = 0
    best_student = ""
    best_grades = []
    for student, grades in student_grades.items():
        average = sum(grades) / len(grades)
        if average > best_average:
            best_average = average
            best_student = student
            best_grades = grades
    return {best_student: best_grades}




def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    dictionnary = {}
    for letter in sentence:
        if letter in dictionnary:
            dictionnary[letter] += 1
        else:
            dictionnary[letter] = 1
    return dictionnary

def get_recipes():
    print("Nom de votre recette")
    name = input()
    print("Liste des ingrédients de la recette")
    ingredients = list(input().split())
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    return {name: ingredients}


def print_recipe(recipe_book) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    print("Nom de la recette à chercher")
    name = input()
    if name in recipe_book:
        print("Ingrédients:")
        print(*recipe_book[name], sep=" \n")
    else:
        print("Votre livre de recette ne contient pas cette recette.")


def main() -> None:
    #print(f"On essaie d'ordonner les valeurs...")
    #order()

    #print(f"On vérifie les anagrammes...")
    #anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
