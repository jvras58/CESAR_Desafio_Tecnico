"""Dashboard do CESAR - Desafio Técnico."""


from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from models.projects import Projects
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Título do dashboard
st.title('Dashboard do CESAR - Desafio Técnico')

engine = create_engine('sqlite:///../database.db')
Session = sessionmaker(bind=engine)
session = Session()


def get_projects(limit:int | None = None) -> list:
    """Retorna uma lista com todos os projetos.

    limitando a quantidade se especificado.
    """
    query = session.query(Projects)
    if limit:
        query = query.limit(limit)
    return query.all()


# Buscar dados dos projetos
projects = get_projects(5)

# Criar listas para os dados
project_names = [project.project_name for project in projects]
initial_budgets = [project.initial_budget for project in projects]
project_costs = [project.project_cost for project in projects]

# Criar gráfico de barras duplas
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(project_names))

plt.bar(index, initial_budgets, bar_width, label='Orçamento Inicial')
plt.bar([i + bar_width for i in index],
        project_costs, bar_width,
        label='Custo do Projeto')

plt.xlabel('Nome do Projeto')
plt.ylabel('Valor (R$)')
plt.title('Comparação de Orçamento Inicial e Custo do Projeto')
plt.xticks([i + bar_width / 2 for i in index], project_names, rotation=45)
plt.legend()

# Mostrar gráfico no Streamlit
st.pyplot(plt)





# Criar gerador de números aleatórios
rng = np.random.default_rng(19680801)

n_bins = 10
x = rng.random((1000, 3))

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

colors = ['red', 'tan', 'lime']
ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
ax0.legend(prop={'size': 10})
ax0.set_title('bars with legend')

ax1.hist(x, n_bins, density=True, histtype='bar', stacked=True)
ax1.set_title('stacked bar')

ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
ax2.set_title('stack step (unfilled)')

# Fazer um histograma múltiplo de conjuntos de dados
# com diferentes comprimentos.
x_multi = [rng.random(n) for n in [10000, 5000, 2000]]
ax3.hist(x_multi, n_bins, histtype='bar')
ax3.set_title('different sample sizes')

fig.tight_layout()

# Mostrar gráfico no Streamlit
st.pyplot(fig)
