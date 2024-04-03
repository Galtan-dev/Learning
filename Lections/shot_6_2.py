# mohu si naimportovat vlastní funkci
import shot_6_1 as dm

# mužu pak používat funkce z dummy modulu
dm.dummy_function()
# pro jmeno modulu
print(dm.__name__)
# když importuju modul tak se spustí, takže mamli tam nejaky prikaz a ne funkci tak se spusti
# mužu i přistupovat k promeným z modulu
print(dm.A)
# je nutno mít ty moduly ve stejném adresáři
