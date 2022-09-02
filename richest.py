import pandas as pd
import csv

df = pd.read_csv('TopRichestInWorld.csv')

with open('saida.csv', 'w') as saida:
    writer = csv.writer(saida, delimiter=',')
    df['NetWorth'] = df['NetWorth'].replace('$','')
    df['NetWorth'] = df['NetWorth'].replace('"','')
    writer.writerow(['Name','NetWorth','Age','Country/Territory','Source','Industry'])

    for col in list(df.columns):
        writer.writerow(df[col])