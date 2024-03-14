import pandas as pd

def imputar_datos(df):
    for index, row in df.iterrows():
        if pd.isnull(row['tipo_recuperacion']):
            df.at[index, 'tipo_recuperacion'] = 'Tiempo'
        if pd.isnull(row['estado']):
            df.at[index, 'estado'] = 'Leve'
        if pd.isnull(row['edad']):

            df.at[index, 'edad'] = df['edad'].mean()
    return df
