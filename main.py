from math import sqrt

#### Fonction secondaire


def isprime(p):
    if p != int(p):
        return False
    if p<2:
        return False
    for i in range(2,p-1):
        n = p%i 
        if n ==0: #p est divisible par i
            return False #donc il n'est pas premier
    return True

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
