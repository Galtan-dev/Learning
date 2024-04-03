import matplotlib.pyplot as plt

"""
Výpočet chvíli trvá, je to ale pod 2 minuty
"""

def collatz_steps(n):
    numbers = [0]
    steps = 0
    # smička co dělí číslo pokud je sudé a násobí třemi pokud je liché a zaznamená vá každý krok
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        # časový krok
        steps += 1
        # list všech čísel přes které funkce iterovala
        numbers.append(n)
    # největší číslo, které během iterace vzniklo
    max_value = max(numbers)
    # vrací počet kroků a myx číslo
    return steps, max_value

def main():
    max_number = 10**6

    # Histogram s počtem kroků
    steps_histogram = [collatz_steps(i)[0] for i in range(1, max_number + 1)]
    plt.hist(steps_histogram, bins=50, edgecolor='black')
    plt.title('Histogram počtu kroků pro čísla od 1 do 10^6')
    plt.xlabel('Počet kroků')
    plt.ylabel('Počet čísel')
    plt.show()

    # Nejvyšší dosažená hodnota pro každé číslo
    max_values = [collatz_steps(i)[1] for i in range(1, max_number + 1)]
    plt.plot(range(1, max_number + 1), max_values)
    plt.title('Nejvyšší dosažená hodnota pro každé číslo')
    plt.xlabel('Číslo')
    plt.ylabel('Nejvyšší dosažená hodnota')
    plt.show()

if __name__ == "__main__":
    main()