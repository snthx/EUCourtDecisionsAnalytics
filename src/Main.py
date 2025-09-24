def main():
    # Einfache Variablen
    name = "Welt"
    zahl = 42

    # Ausgabe von Text
    print(f"Hallo, {name}!")

    # Mathematische Operationen
    quadrat = zahl ** 2
    print(f"Das Quadrat von {zahl} ist {quadrat}.")

    # Eine einfache Schleife
    print("Die ersten 5 Zahlen sind:")
    for i in range(1, 6):
        print(i)

if __name__ == "__main__":
    main()