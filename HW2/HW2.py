import pandas as pd

def homework(anime_data_extracted):
    result = anime_data_extracted.groupby("Type")["Score"].mean().sort_values(ascending=False)
    return result

anime_data_extracted = pd.DataFrame({
    "Type": ["TV", "TV", "Movie", "Movie", "OVA"],
    "Score": [8.0, 6.0, 9.0, 7.0, 5.0],
})

print(homework(anime_data_extracted))