"""Gera dados fictícios para os projetos."""
import random

from faker import Faker

fake = Faker()

# Função para gerar dados dos projetos
def generate_project_data(num_projects: int) -> list:
    """Gera dados fictícios para os projetos."""
    projects = []

    for _ in range(num_projects):
        name = fake.catch_phrase()

        # Entre 2020 e 2022
        start_date = fake.date_between(start_date='-4y', end_date='-1y')

        # End date depois de start date
        end_date = fake.date_between(start_date=start_date, end_date='today')

        custo_inicial = round(random.uniform(5000, 1000000), 2)

        custo_final = round(random.uniform(5000, custo_inicial), 2)

        receita = round(random.uniform(custo_final, custo_final * 1.5), 2)

        projects.append({
            'name': name,
            'start_date': start_date,
            'end_date': end_date,
            'custo_inicial': custo_inicial,
            'custo_final': custo_final,
            'receita': receita,
        })

    return projects
