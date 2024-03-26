import pandas as pd

babynames_df = pd.read_csv('./babynames.csv')

babynames_df['sex_name'] = babynames_df['sex'] + '_' + babynames_df['name']
aggregated = babynames_df.groupby(['year', 'sex_name'])['n'].sum().reset_index()
pivoted = aggregated.pivot(index='year', columns='sex_name', values='n').fillna(0)

final_df = pivoted.reset_index()

transformed_file_path = 'transformed_babynames.csv'
final_df.to_csv(transformed_file_path, index=False)