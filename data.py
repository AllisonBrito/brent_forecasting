import pandas as pd


#Extraindo e tratando os dados
def carregar_dados():
    df = pd.read_html("http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view", thousands='.')
    df = df[2]
    df.rename(columns={0: "data", 1: "preco"}, inplace=True)
    df.drop(0, inplace=True)
    # Convertenado a coluna preço para o tipo float
    df['preco'] = df['preco'].replace(",", ".", regex=True).astype(float)
    # Convertenado a coluna data para o tipo datetime
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['ano'] = df['data'].dt.year
    df['ano'] = df['ano'].astype('int32')
    df['ano_mes'] = df['data'].dt.strftime('%b %y').str.capitalize()
    return df

def dados_prophet():
    df = carregar_dados()
    df_prophet = df[['data', 'preco']]
    df_prophet.rename(columns={"data": "ds", "preco": "y"}, inplace=True)
    return df_prophet
