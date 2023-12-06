import logging

# try:
#     # code we want to execute
#     print(x)
# except Exception as ex:
#     # code is execute if there is error in try block
#     print("Something went wrong")
#     print(f"{ex.__class__.name}")
#     print(ex)

##############################################

# x = 3
# y = 0
# try:
#     # code we want to execute
#     print(x / y)
# except ZeroDivisionError as ex:
#     # code is execute if there is error in try block
#     print(f"Zero division error encountered: {ex}")
#     print(x/(y+1e-100))     # pokud by došlo k dělení nulou ale chci znat stejne vysledek tak si pridam regularozacni konstantu
# except TypeError as ex:
#     print(f"Could not divides: {ex}")
#     raise      # vyvolá poslední vzinklou vyjímku, přidámli Exception tak mužu takhle vyvolat jakoukoiv vyjímku
# except Exception as ex:     # pokud by došlo k něčemu nečekanému, dává se vždy nakonec protože pokud se jeden trigne tak se ostatnní už nevyhodnotí
#     print(f"Something unexpected happend: {ex}")

############################################
#
# try:
#     # code we want to execute
#     if type(to_cypher) is str
#         encrypted_stuff = cypher(to_cypher)
# except ZeroDivisionError as ex:
#     print("Nothing to cypher")
#     raise       # pokud by to tu spadlo tak ty nezašifrovaná data tady zustanou v paměti, bezpečnostní riziko
# finally:
#     del to_cypher   # tímhle způsobem se to vymaže, blok finally ikdyž je nakonci se vždy vyhodnotí

############################################
#
# msg_format = "%(levelname)s - %(asctime)s - %(message)s"    # ty klíčová slova jsou definovaná v tom modulu...
# logging.basicConfig(filename="error_log.log",
#                     filemode="a",
#                     format=msg_format,
#                     level=logging.INFO)   # takhle ukladam vše co ma prioritu info a viš
# logger = logging.getLogger()    # defacto zařízení co zaznamenáva co chci
# logger.error("Error occured")   # zaznam o chybě
# logger.info("Data were saved")  # zaznam o informacích
#
# def dummy_function(dummy_argument):     # zapíše se mi to logu a vim okamžitě všechny chyby co se vyskytnout
#     try:
#         123/dummy_argument
#     except TypeError:
#         logger.error(f"TypeError occured in dummy function with dummy argument {dummy_argument}")
#     else:
#         logger.info(f"dummy function evaluated succesfully.")
#
# dummy_function(1)
# dummy_function("asdf")

############################################
# definování vlastních vyjímek
class TemperatureOutOfRange(Exception):
    def __init__(self, temperature, message="Temperature lower than 0 K"):
        self.temperature = temperature
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.temperature}: {self.message}"

temperature = int(input("Enter temperature in Kelvins: "))
if temperature < 0:
    raise TemperatureOutOfRange(temperature, "Oooops")

############################################
# testování kodu
# obecně zkoušíme jestli nějaká funkce nebo metoda pro konkrétn argumenty vrátí výstup
    # např se ukaž že to sice funguje ale trvá to dlouho, přepíšu to a je velká šance že tam udělám cyhbu
    # kontroluju pro sadu metod a parametrů jestli se vrací požadované výsledky
# modul unitest - automatizace
# prezentace