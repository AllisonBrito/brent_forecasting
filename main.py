import streamlit as st
from storytelling import show_storytelling
from dashboard import show_dashboard
from forecast import show_forecasting

def main():
    # Configura o título do app
    st.set_page_config(page_title="App de Previsão de Petróleo", layout="wide")

    # Sidebar para navegação entre as páginas
    st.sidebar.title("Navegação")
    page = st.sidebar.radio("Ir para", ["Storytelling", "Dashboard", "Forecasting"])

    # Renderização das páginas com base na seleção do usuário
    if page == "Storytelling":
        show_storytelling()
    elif page == "Dashboard":
        show_dashboard()
    elif page == "Forecasting":
        show_forecasting()


if __name__ == "__main__":
    main()