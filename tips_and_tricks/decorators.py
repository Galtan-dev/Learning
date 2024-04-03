def my_decorator(func):
    # Definice vnitřní funkce wrapper, která rozšiřuje chování původní funkce
    def wrapper():
        print("Před voláním funkce")  # Výpis před voláním funkce
        func()  # Volání původní funkce
        print("Po volání funkce")  # Výpis po volání funkce
    return wrapper

# Definice funkce, která bude používat dekorátor
@my_decorator
def say_hello():
    print("Hello!")  # Tělo původní funkce

# Volání funkce s aplikovaným dekorátorem
say_hello()



# Tento kód definuje dekorátor my_decorator, který přijímá jednu funkci jako argument.
# Vnitřní funkce wrapper rozšiřuje chování původní funkce tím, že přidá výpisy před a po volání funkce.
# Symbol @my_decorator nad definicí funkce say_hello označuje, že tato funkce bude používat dekorátor my_decorator.
# Nakonec je volána funkce say_hello, která má aplikovaný dekorátor.