def fibonacci_generator():
    # Inicializace prvních dvou čísel Fibonacciho posloupnosti
    a, b = 0, 1
    # Nekonečná smyčka, která generuje čísla Fibonacciho posloupnosti
    while True:
        # Vrátí aktuální hodnotu Fibonacciho posloupnosti
        yield a
        # Aktualizuje hodnoty a b na následující čísla Fibonacciho posloupnosti
        a, b = b, a + b

# Vytvoření instance generátoru Fibonacciho posloupnosti
fib = fibonacci_generator()
# Iterace přes prvních 10 čísel Fibonacciho posloupnosti
for _ in range(10):
    # Získání další hodnoty z generátoru a výpis na výstup
    print(next(fib))

#Používání yield v definici funkce umožňuje funkci fungovat jako generátor, který je schopen uchovávat svůj stav
# mezi voláními a generovat hodnoty postupně podle potřeby.
# Tímto způsobem je možné efektivně generovat velké posloupnosti nebo
# se vyhýbat ukládání velkého množství dat do paměti.