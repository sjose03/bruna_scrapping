from pytrends.request import TrendReq
import pandas as pd
pytrends = TrendReq(hl='pt-PT', tz=360)

years = ['2018', '2019', '2020', '2021', '2022']

dfs = []
for year in years:
    print(year)
    pytrends.build_payload(geo='BR', kw_list=['sarampo'], timeframe=[
        f'{year}-01-01 {year}-12-31'])
    df = pytrends.interest_over_time()
    dfs.append(df)
df_concat = pd.concat(dfs)

df_concat.to_csv(f'dados_trends.csv', header=True, index=True)
