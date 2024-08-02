"""Arquivo principal do aplicativo para executar o aplicativo Streamlit."""
import streamlit as st
from graphs.graph_orcamento_excedido import orcamento_excedido_page
from graphs.graph_rentabilidade import rentabilidade_liquida_page
from graphs.graph_top5_receitas import top5_receitas_page
from streamlit_option_menu import option_menu

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        "Menu",
        [
            "Home",
            "Rentabilidade Líquida",
            "Top 5 Receitas",
            "Orçamento Excedido",
        ],
        icons=["house", "bar-chart-line", "graph-up-arrow", "cash-stack"],
        menu_icon="cast",
        default_index=0,
    )

# Conteúdo para cada seleção de menu
if selected == "Rentabilidade Líquida":
    rentabilidade_liquida_page()
elif selected == "Top 5 Receitas":
    top5_receitas_page()
elif selected == "Orçamento Excedido":
    orcamento_excedido_page()
else:
    st.title("Dashboard do CESAR - Desafio Técnico")

    st.header("Bem-vindo ao Dashboard do CESAR!")
    st.write("Este dashboard é projetado para avaliação de Estagio.")

    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <img src="https://www.cesar.org.br/_next/image?url=%2Flogo.png&w=128&q=75" alt="Logo">
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Sobre o Dashboard")
    st.write(
        "Utilize o menu lateral para navegar pelas diferentes visualizações de dados. "
        "Cada seção do dashboard oferece uma análise específica dos dados dos projetos.",
    )

    st.subheader("Funcionalidades Principais")
    st.markdown(
    """
    - **Rentabilidade Líquida**: Avalie o desempenho financeiro dos projetos.
    - **Top 5 Receitas**: Descubra quais projetos estão gerando mais receita.
    - **Orçamento Excedido**: Identifique projetos que ultrapassaram o orçamento.
    """,
    )

    st.info(
        "Os gráficos são gerados a partir de dados fictícios carregados de um banco de dados SQLite "
        "e visualizados com a biblioteca Plotly.",
    )

    if st.button("Saiba Mais"):
        st.write("Para mais informações, entre em contato [Linkedin](https://www.linkedin.com/in/-jonathasvinicius/).")
