"""Script de execução para inserir dados no banco de dados."""

from app.dados.inserir import project_50

if __name__ == "__main__":
    projects = project_50()
    print(f"Inseridos {len(projects)} projetos.")
