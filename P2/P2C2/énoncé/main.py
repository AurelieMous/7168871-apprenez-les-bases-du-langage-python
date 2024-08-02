
def main():
    liste_nombre= input("Liste de nombre entier séparé par des virgules :")
    liste_nombre = liste_nombre.split(",")
    print(liste_nombre)
    
    somme = 0
    for nombre in liste_nombre:
        somme += int(nombre)
        print(f"Somme des nombres : {somme}")

    moyenne = somme / len(liste_nombre)
    print(f'Moyenne des nombres : {moyenne}')

    #le résultat doit compter Pour chaque nombre de la liste plus grand que la moyenne de la liste

    nombre_supperieur = 0
    for nombre in liste_nombre:
        if int(nombre) >= moyenne:
            nombre_supperieur += 1
    print(f"Nombre de nombres supérieurs à la moyenne : {nombre_supperieur}")

    pair = 0
    for nombre in liste_nombre:
        if (int(nombre) %2) ==0:
            pair += 1
    print(f"Nombre de nombres pairs : {pair}")

   
    
        
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main() 