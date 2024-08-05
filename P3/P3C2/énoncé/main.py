# Écrivez votre code ici !
from bs4 import BeautifulSoup

with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

#Titre
titre = soup.title.string

#balise
balise_h1 = soup.h1.string

# Extraction des noms et des prix des produits dans la liste
products = soup.find_all("li")
products_liste = []
for product in products:
    name = product.h2.string
    price = product.find('p', string = lambda s: 'Prix' in s).string
    products_liste.append((name, price))

description_liste = []
for product in products:
    description = product.find('p', string = lambda s: 'Description' in s).string
    description_liste.append(description)

# Étape 2 : Affichage des informations extraites
print("Titre de la page :", titre)
print("Texte de la balise h1 :", balise_h1)
print("Liste des produits :", products_liste)
print("Liste des descriptions de produits :", description_liste)

# Étape 3 : Conversion des prix en dollars
for i, (name, price) in enumerate(products_liste):
    # Supprimer les caractères non numériques de la chaîne de prix
    euro_price_str = ''.join(filter(str.isdigit, price.split()[2]))
    euro_price = int(euro_price_str)
    dollar_price = euro_price * 1.2
    products_liste[i] = (name, f"{dollar_price}$")

# Étape 4 : Affichage de la nouvelle liste avec les prix en dollars
print("Liste des produits :", products_liste)