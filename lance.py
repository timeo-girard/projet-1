import random

def lancer_de():
    """Simule un lancer de dé et renvoie le résultat."""
    de = random.randint(1, 6)
    print(f"Le dé affiche : {de}")

    if de == 6:
        print("\(°o°)/ Gagné !")
    elif de == 1:
        print("Perdu...")
        print("🎉 Gagné !")
    elif de == 1:
        print("😢 Perdu...")
    else:
        print("Pas de gain, réessaie !")

# Exemple d'appel de la fonction
lancer_de()
