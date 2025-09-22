
"""
Module principal pour l'affichage des nombres premiers inférieurs à 100.
Contient la fonction isprime et la fonction main.
"""

import math

#### Fonction secondaire


def isprime(p):
    """Teste si p est un nombre premier."""
    if not isinstance(p, int):
        return False
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:  # on calcule une seule fois les nombres pairs
        return False
    limit = math.isqrt(p)
    for i in range(3, limit + 1, 2):  # on teste les diviseurs impairs
        if p % i == 0:
            return False  # p est divisible par i donc n'est pas premier
    return True  # p n'est pas divisble par un autre nombre que 1 et lui-même

#### Fonction principale


def main():
    """Affiche tous les nombres premiers inférieurs à 100 séparés par une virgule."""
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()

#test check : pytest .python
#test de qualité du code : pylint main.py (./check -q fonctionne)