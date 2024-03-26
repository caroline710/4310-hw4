import pandas as pd

df = pd.read_csv("./transformed_babynames.csv")

total_births = df.drop('year', axis=1).sum()

top_male_names = total_births.filter(like='M_').sort_values(ascending=False).head(20)
top_female_names = total_births.filter(like='F_').sort_values(ascending=False).head(20)

top_names = pd.concat([top_male_names, top_female_names]).index.to_list()
top_names.append('year')

df_top_names = df[top_names]

df_top_names.to_csv("top_20_babynames.csv", index=False)