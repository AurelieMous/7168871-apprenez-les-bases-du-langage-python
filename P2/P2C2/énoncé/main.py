
def main():
    nombre = input("Liste de nombre entier séparé par des virgules :")
    liste_nombre = nombre.split(", ")
    print(liste_nombre)
    
    resultat = 0
    for addition in liste_nombre:
        resultat += int(addition)
        print(f"Somme des nombres : {resultat}")

    moyenne = resultat / len(liste_nombre)
    print(f'Moyenne des nombres : {moyenne}')

    for addition in liste_nombre:
        supperieur_moyenne = addition >= moyenne
        print(f"Nombre de nombres supérieurs à la moyenne : {supperieur_moyenne}")
   
    
        
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main() 