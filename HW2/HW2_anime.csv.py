import pandas as pd

def homework(anime_data_extracted):
    # aquí tu código
    result = anime_data_extracted.groupby("Type")["Score"].mean().sort_values(ascending=False)
    return result

anime_data = pd.read_csv("anime.csv")
anime_data_extracted = anime_data[anime_data["Score"] != "Unknown"].copy()
anime_data_extracted["Score"] = pd.to_numeric(anime_data_extracted["Score"])

print(homework(anime_data_extracted))
