import random

def lancer_de():
    """Simule un lancer de dé et renvoie le résultat."""
    de = random.randint(1, 6)
    print(f"Le dé affiche : {de}")

    if de == 6:
<<<<<<< HEAD
        print("\(°o°)/ Gagné !")
    elif de == 1:
        print("Perdu...")
=======
        print("🎉 Gagné !")
    elif de == 1:
        print("😢 Perdu...")
>>>>>>> 4f08dd5c699ebb82cbf8224c23e952b2c3be6d7b
    else:
        print("Pas de gain, réessaie !")

# Exemple d'appel de la fonction
lancer_de()
