import pandas as pd #para ler, visualizar e printar infos do df
import numpy as np #numpy porque é sempre bom importar numpy né 
import csv

df = pd.read_csv('TopRichestInWorld.csv')

with open('saida.csv', 'w') as saida:
    writer = csv.writer(saida)
    df['NetWorth'] = df['NetWorth'].replace('$','')
    df['NetWorth'] = df['NetWorth'].replace('"','')
    writer.writerow(['Name','NetWorth','Age','Country/Territory','Source','Industry'])

    for col in list(df.columns):
        writer.writerow(df[col])