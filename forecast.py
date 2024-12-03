
import streamlit as st
import plotly.express as px
from prophet import Prophet
from data import dados_prophet
import matplotlib.pyplot as plt
from prophet.diagnostics import cross_validation, performance_metrics




# Função para exibir o modelo de previsão

def show_forecasting():
    tab1, tab2 = st.tabs(["Forecasting", "Performance do Modelo"])

    with tab1:

        st.title("🔮 Petróleo Brent Forecasting")
        
        # Entrada para número de dias para prever
        periods_input = st.number_input('Quantos dias você quer prever?', min_value=1, max_value=30, value=7)
        
        df_prophet = dados_prophet()
        

        # Parametros do modelo
        model = Prophet(
        seasonality_mode='multiplicative',
        changepoint_prior_scale=0.4,
        seasonality_prior_scale=5,
        yearly_seasonality=True,
        weekly_seasonality=False,  
        daily_seasonality=False
        )
        
        # capturar padrões de dias úteis
        model.add_seasonality(
        name='workday',
        period=5,  # 5 dias úteis
        fourier_order=5
        
        )
        model.fit(df_prophet)
        
        # Criar dataframe para previsão futura
        future = model.make_future_dataframe(periods=periods_input, freq="D")
        forecast = model.predict(future)
        
        # Exibir previsão
        st.write("### Previsão para os próximos {} dias".format(periods_input))

        fig_forecast = px.line(forecast[['ds', 'yhat']].tail(periods_input), x='ds', y='yhat', labels={"ds": "","yhat": "Preço por barril em USD" })
        st.plotly_chart(fig_forecast, use_container_width=True)



    with tab2:
        st.title("🚀 Performance e Componentes do Modelo")

        # Gráfico da previsão
        st.write("### Forecast")
        fig1 = model.plot(forecast)
        st.pyplot(fig1)
        st.write("### Componentes do Modelo")
        plt.figure(figsize=(15, 10))
        fig_componentes = model.plot_components(forecast)
        plt.tight_layout()
        st.pyplot(fig_componentes)

        st.write("### Validação Cruzada")

        st.write("""Ao realizar a validação cruzada para diferentes horizontes de previsão, de 3 a 30 dias, 
                    obtivemos um MAPE que varia entre aproximadamente 21.8% e 25.2%  """)

        df_cv = cross_validation(model, initial='8000 days', period='365 days', horizon='30 days')
        # Calculando as métricas de desempenho
        df_p = performance_metrics(df_cv)
        st.dataframe(df_p[['horizon', 'mape']].set_index('horizon'))

        
        
        
