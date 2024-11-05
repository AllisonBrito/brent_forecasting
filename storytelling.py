
import streamlit as st
import plotly.express as px
from data import carregar_dados

df = carregar_dados()

def show_storytelling():
    st.title("🛢️ Petróleo Brent: Visão Geral")

    st.write(
    """
    O petróleo Brent é crucial no mercado global de energia, servindo como referência para os preços de aproximadamente
      dois terços do comércio internacional de petróleo. Extraído do Mar do Norte, sua qualidade mais leve 
      e baixa presença de enxofre o tornam ideal para refino. As flutuações no preço do Brent impactam custos de transporte,
        produção de bens e inflação, influenciando economias globais e locais.

    Assim, o Brent não só reflete as condições do mercado de energia, mas também serve como um indicador das condições 
    econômicas e geopolíticas globais.""")

    st.write("## Crise do Petróleo de 2014-2016")

    st.write("Entre 2014 e 2016, o preço do petróleo Brent caiu de mais de USD 100 por barril para menos de USD 30.")

    fig_crise_petroleo = px.line(df[(df['ano'] >= 2014) & (df['ano'] <= 2016)], x="data", y="preco", labels={"data": "", "preco": "Preço por barril em USD"})
    st.plotly_chart(fig_crise_petroleo, use_container_width=True)

    st.write("""
### Principais Impactos:

**Rússia:**
- O rublo russo perdeu mais de 50% de seu valor em relação ao dólar.
- A inflação atingiu 12,9% em 2015.
- O PIB russo contraiu 2,5% em 2015 e 0,2% em 2016.

**Venezuela:**
- A economia entrou em colapso, com hiperinflação atingindo 65.000% em 2018.
- Escassez generalizada de alimentos e medicamentos.
- O PIB contraiu mais de 30% entre 2013 e 2017.

**Noruega:**
- O desemprego aumentou de 3,5% em 2014 para 4,7% em 2016.
- A coroa norueguesa desvalorizou-se em cerca de 30% em relação ao dólar.
- O governo teve que usar parte do seu fundo soberano para equilibrar o orçamento.
""")
    
    st.write("## Choque do Petróleo de 2020 (COVID-19)")

    st.write("""A pandemia de COVID-19 causou uma queda abrupta na demanda por petróleo, 
             levando o preço do Brent a cair para uma mínima histórica de USD 9 por barril em abril de 2020.""")
    
    fig_covid_petroleo = px.line(df[(df['ano'] >= 2019) & (df['ano'] <= 2020)], x="data", y="preco", labels={"data": "", "preco": "Preço por barril em USD"})
    st.plotly_chart(fig_covid_petroleo, use_container_width=True)


    st.write("""
### Principais Impactos:

**Arábia Saudita:**
- O déficit orçamentário atingiu 12% do PIB em 2020.
- O governo triplicou o imposto sobre valor agregado e cortou subsídios.
- O crescimento do PIB foi negativo em 4,1% em 2020.

**Reino Unido:**
- As receitas fiscais do setor de petróleo e gás do Mar do Norte caíram 71% em 2020-2021.
- Milhares de empregos foram perdidos no setor de energia offshore.

**Nigéria:**
- As receitas do governo federal caíram 65% abaixo do orçamentado no primeiro semestre de 2020.
- O governo desvalorizou o naira, a moeda local, duas vezes em 2020.
- A economia entrou em recessão, contraindo 1,8% em 2020.
""")

    st.write("## Alta dos Preços em 2022")

    st.write("""Em 2022 os preços do Brent subiram acima de USD 120 por barril devido à recuperação econômica pós-COVID e à guerra na Ucrânia.""")
    
    fig_2022_petroleo = px.line(df[(df['ano'] >= 2021) & (df['ano'] <= 2022)], x="data", y="preco", labels={"data": "", "preco": "Preço por barril em USD"})
    st.plotly_chart(fig_2022_petroleo, use_container_width=True)


    st.write("""
### Principais Impactos:

**Índia (importador):**
- A inflação atingiu 7,79% em abril de 2022, o nível mais alto em 8 anos.
- O déficit comercial aumentou significativamente.
- O governo reduziu impostos sobre combustíveis para aliviar a pressão sobre os consumidores.


**Brasil:**
- A Petrobras registrou lucros recordes, mas enfrentou pressão política para controlar os preços dos combustíveis.
- O governo implementou medidas para limitar o impacto do aumento dos preços na inflação.


**Alemanha:**
- A inflação atingiu 7,9% em maio de 2022, o nível mais alto em 40 anos.
- O governo implementou pacotes de ajuda para aliviar o impacto dos altos custos de energia nos consumidores.

""")
    

    st.write("""Estes estudos de caso demonstram como as flutuações no preço do petróleo Brent podem ter impactos profundos e variados
              em diferentes economias, afetando desde taxas de câmbio e inflação até políticas fiscais e bem-estar social. 
             É importante notar que os países exportadores de petróleo tendem a se beneficiar de preços altos, enquanto os 
             importadores enfrentam desafios econômicos. No entanto, quedas acentuadas nos preços podem causar instabilidade 
             mesmo em países produtores, especialmente se suas economias forem altamente dependentes das receitas do petróleo """)
