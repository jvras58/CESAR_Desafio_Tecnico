"""Dashboard do CESAR - Desafio Técnico."""

import streamlit as st
from models.projects import Projects
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Título do dashboard
st.title('Dashboard do CESAR - Desafio Técnico')

engine = create_engine('sqlite:///../database.db')
Session = sessionmaker(bind=engine)
session = Session()


def get_projects()-> list:
    """Retorna uma lista com todos os projetos."""
    return session.query(Projects).all()

projects = get_projects()
project_names = [project.project_name for project in projects]
selected_project = st.selectbox('Selecione um projeto', project_names)
st.write(f'Você selecionou: {selected_project}')


