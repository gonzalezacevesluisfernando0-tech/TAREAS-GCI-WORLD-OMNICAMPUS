import pandas as pd

df = pd.DataFrame({
    "Materia": ["Mate", "Mate", "Inglés", "Inglés", "Historia"],
    "Calif":   [8, 6, 9, 7, 5],
})

print(df.groupby("Materia")["Calif"].max())

'''
def homework(anime_data_extracted):
    # aquí tu código
    result = ...
    return result

case_2_data = pd.DataFrame({
    "Type": ["TV", "TV", "Movie", "Movie", "OVA"],
    "Score": [8.0, 6.0, 9.0, 7.0, 5.0],
})
print(homework(case_2_data))
'''