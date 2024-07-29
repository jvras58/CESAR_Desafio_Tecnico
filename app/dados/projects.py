"""Dados de Projetos."""

import random

from faker import Faker

fake = Faker()

# Função para gerar dados dos projetos
def generate_project_data(num_projects):
    projects = []

    for _ in range(num_projects):
        project_id = _
        project_name = fake.catch_phrase()
        start_date = fake.date_between(start_date='-4y', end_date='-1y')  # Entre 2020 e 2022
        end_date = fake.date_between(start_date=start_date, end_date='today')  # End date depois de start date
        initial_budget = round(random.uniform(5000, 1000000), 2)
        project_cost = round(random.uniform(5000, initial_budget), 2)
        revenue = round(random.uniform(project_cost, project_cost * 1.5), 2)

        projects.append((project_id, project_name, start_date, end_date, initial_budget, project_cost, revenue))

    return projects

# Gerar os dados dos projetos
project_data = generate_project_data(50)

# Criar os comandos SQL de inserção
insert_statements = []
for project in project_data:
    insert_statement = f"""
    INSERT INTO Projects (project_id, project_name, start_date, end_date, initial_budget, project_cost, revenue)
    VALUES ({project[0]}, '{project[1]}', '{project[2]}', '{project[3]}', {project[4]}, {project[5]}, {project[6]});
    """
    insert_statements.append(insert_statement)

# Escrever os comandos SQL em um arquivo
with open('insert_projects.sql', 'w') as file:
    file.write('\n'.join(insert_statements))

print("Arquivo SQL criado com sucesso!")