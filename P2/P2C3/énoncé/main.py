# Ecrivez vos fonctions ici
def salaire_mensuel(salaire_annuel):
    salaire_mensuel = salaire_annuel/12
    return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = salaire_mensuel/4
    return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
    return salaire_horaire

def main():
    salaire_annuel = input("Entrez votre salaire annuel : ")
    heures_travaillees = input("Entrez votre nombre d'heures travaillées par semaine : ")
    #calculer salaire horraire correspondant

    salaire_m = salaire_mensuel(int(salaire_annuel))
    salaire_s = salaire_hebdomadaire(salaire_m)
    salaire_heure = salaire_horaire(salaire_s, int(heures_travaillees))
    print(salaire_heure)


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()