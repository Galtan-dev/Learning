import numpy as np

# nahrání souboru pomocí funkce genfromtext
data = np.genfromtxt('points.csv', delimiter=' ')

# trik je v tom vypočítat si normu pro vzdálenost každého bodu od toho nulového bodu
# no a následně najít bod pro nejmenší normu protože ten je nejblíž
reference_point = np.array([0, 0])
distances = np.linalg.norm(data - reference_point, axis=1)
nearest_point_index = np.argmin(distances)
nearest_point = data[nearest_point_index]

# odpověď
print(f"Answer is: {nearest_point}")
