

import streamlit as st
import plotly.express as px
from data import carregar_dados
import pandas as pd



df = carregar_dados()

def formatar_dolar(valor):
    return f"${valor:,.2f}"

# Função para exibir o dashboard
def show_dashboard():
    st.title("📊 Análise dos Preços do Petróleo Brent")

    # Converter para objetos datetime do Python
    min_date = df["data"].min()
    max_date = df["data"].max()

    coluna1, coluna2 = st.columns(2)

    with coluna1:
        option = st.selectbox(
    "Selecione o tipo da visualização:",
    ("Preço Histórico", "Média Mensal", "Média Anual"))
        
    with coluna2:
        # Slider para selecionar intervalo de datas
        data_inicio, data_fim = st.slider(
        "Selecione o intervalo de datas:",
        min_value=min_date,
        max_value=max_date,
        value=(min_date, max_date), format="DD/MM/YYYY")
    
    df_filtrado = df[(df["ano"] >= data_inicio) & (df["ano"] <= data_fim)]

    df_ano = df_filtrado[['ano', 'preco']].groupby(['ano']).mean().round(2)
    # Fazer o groupby e ordenar cronologicamente usando a data original
    df_mes = df_filtrado.groupby(['ano_mes', df_filtrado['data'].dt.to_period('M')])['preco'].mean().round(2).reset_index()
    # Ordenar pelo período de data e remover a coluna auxiliar para exibição final
    df_mes = df_mes.sort_values(by='data').drop(columns=['data']).reset_index(drop=True)
    

    # Função para criar gráficos com título centralizado
    def titulo_centralizado(fig):
        fig.update_layout(title={'x': 0.5, 'xanchor': 'center'})
        return fig

    ## Cartões

    mean = formatar_dolar(df_filtrado['preco'].mean().round(2))
    std = formatar_dolar(df_filtrado['preco'].std().round(2))
    min = formatar_dolar(df_filtrado['preco'].min().round(2))
    max = formatar_dolar(df_filtrado['preco'].max().round(2))
    median = formatar_dolar(df_filtrado['preco'].median().round(2))

    ## Gráficos
    fig_historico = titulo_centralizado(px.line(df_filtrado, x="data", y="preco", title='Evolução dos Preços do Petróleo Brent ao Longo do Tempo', labels={"data": "", "preco": "Preço por Barril em USD"}))
    fig_ano = titulo_centralizado(px.line(df_ano, y="preco", title='Preço Médio do Pétroleo Brent por Ano', labels={"ano": "", "preco": "Preço por Barril em USD"}))
    fig_mes = titulo_centralizado(px.line(df_mes,x='ano_mes' ,y="preco", title='Preço Médio do Pétroleo Brent por Mês', labels={"ano_mes": "", "preco": "Preço por Barril em USD"}))
    box_plot = titulo_centralizado(px.box(df_filtrado, y='preco', labels={"preco": "Preço por Barril em USD"}, title='Distribuição de Preços do Petróleo Brent'))
    hist_plot = titulo_centralizado(px.histogram(df_filtrado, x='preco', labels={"preco": "Preço por Barril em USD"}, title='Frequência dos Preços do Petróleo Brent'))
    box_plot_ano = titulo_centralizado(px.box(df_ano, y='preco', labels={"preco": "Preço por Barril em USD"}, title='Distribuição de Preços Médios Anuais do Petróleo Brent'))
    box_plot_mes = titulo_centralizado(px.box(df_mes, y='preco', labels={"preco": "Preço por Barril em USD"}, title='Distribuição de Preços Médios Mensais do Petróleo Brent'))
    hist_plot_ano = titulo_centralizado(px.histogram(df_ano, x='preco', labels={"preco": "Preço por Barril em USD"}, title='Frequência dos Preços Médios Anuais do Petróleo Brent'))
    hist_plot_mes = titulo_centralizado(px.histogram(df_mes, x='preco', labels={"preco": "Preço por Barril em USD"}, title='Frequência dos Preços Médios Mensais do Petróleo Brent'))
    
    
    card1, card2, card3, card4, card5 = st.columns(5)
    
    card1.metric(label='Média', value= mean)
    card2.metric(label='Desvio Padrão', value= std)
    card3.metric(label='Mediana', value= median)
    card4.metric(label='Mínimo', value= min)
    card5.metric(label='Máximo', value= max)

    col1, = st.columns(1)
    col2, col3 = st.columns(2)

    if option == 'Preço Histórico':
        col1.plotly_chart(fig_historico, use_container_width=True)
        col2.plotly_chart(box_plot, use_container_width=True)
        col3.plotly_chart(hist_plot, use_container_width=True)
    elif option == "Média Anual":
        col1.plotly_chart(fig_ano, use_container_width=True)
        col2.plotly_chart(box_plot_ano, use_container_width=True)
        col3.plotly_chart(hist_plot_ano, use_container_width=True)
    else:
        col1.plotly_chart(fig_mes, use_container_width=True)
        col2.plotly_chart(box_plot_mes, use_container_width=True)
        col3.plotly_chart(hist_plot_mes, use_container_width=True)
