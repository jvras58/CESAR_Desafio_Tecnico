"""Utils dos Graficos."""
import random
from datetime import datetime, timedelta

import pytz


def generate_colors(n: int) -> list:
    """Gera uma lista de cores aleatórias em formato hexadecimal."""
    colors = []
    for _ in range(n):
        color = f"#{random.randint(0, 0xFFFFFF):06x}"
        colors.append(color)
    return colors

def get_project_ultimo_ano(projects: list) -> list:
    """Filtra projetos realizados no último ano.

    e calcula a rentabilidade líquida.
    """
    utc_now = datetime.now(pytz.utc)
    one_year_ago = utc_now - timedelta(days=365)
    return [
        {
            'nome': project.project_name,
            'Rentabilidade_liquida': project.revenue - project.project_cost,
        }
        for project in projects
        if project.end_date.replace(tzinfo=pytz.utc) >= one_year_ago
    ]
