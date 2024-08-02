"""Gera dados fictícios para os projetos."""
import random

from faker import Faker

fake = Faker()

def generate_project_data(num_projects: int) -> list:
    """Gera dados fictícios para os projetos."""
    projects = []

    for _ in range(num_projects):
        project_name = fake.catch_phrase()

        # Entre 2020 e 2022
        start_date = fake.date_between(start_date='-4y', end_date='-1y')

        # End date depois de start date
        end_date = fake.date_between(start_date=start_date, end_date='today')

        initial_budget = round(random.uniform(5000, 1000000), 2)

        # Aleatoriamente decidir se o project_cost deve exceder o initial_budget
        if random.choice([True, False]):
            project_cost = round(random.uniform(initial_budget,
                                                initial_budget * 1.5), 2)
        else:
            project_cost = round(random.uniform(5000, initial_budget), 2)

        revenue = round(random.uniform(project_cost, project_cost * 1.5), 2)

        projects.append({
            'project_name': project_name,
            'start_date': start_date,
            'end_date': end_date,
            'initial_budget': initial_budget,
            'project_cost': project_cost,
            'revenue': revenue,
        })

    return projects
