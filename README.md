
# Dashboard do CESAR - Desafio Técnico

<div align="center">
  <img src="https://www.cesar.org.br/_next/image?url=%2Flogo.png&w=128&q=75" alt="Logo da Cesar" width="120px" height="120px"/>
</div>
<h2 align="center">Gestão de dados financeiros de projetos</h2>



## 📖 Sobre o Projeto

Este é um projeto que visa contemplar o processo seletivo de estagio na cesar - [Leia](docs/CESAR_Desafio.pdf)

## 🚀 Tecnologias e Ferramentas

A aplicação é uma solução web que inclui um dashboard interativo usando o streamlit desenvolvida em Python.



## Stack do projeto

Este projeto é uma applicação web usando uma Biblioteca para criação de aplicações web interativas streamlit.

Essas e outras libs e tecnologias usadas neste projeto são:
|  Lib      | Versão    |
|-----------|-----------|
| **Runtime**           |
| Python    | v3.12.x   |
| streamlit | v1.36.x   |
| **Devtime**           |
| Ruff                          | v0.4.x    |
| Pytest                        | v8.2.x    |
| Pytest Coverage (pytest-cov)  | v5.0.x    |
| Docker Engine                 | vx.x.x    |
| Taskipy                       | v1.12.x   |

### Organização do projeto
```
/
├─📁 .devcontainer     ->  Configurações do devcontainer
├─📁 .vscode           ->  Definições de ambiente para o VSCode
├─📁 docs              ->  Artefatos para documentação do repo
├─📁 app               ->  Implementação
│   ├─🐍 app.py         ->  Entrypoint da aplicação Streamlit
│   ├─📁 config        ->  Módulo de configuração
│   │   └─🐍 settings.py ->  Configuração de variáveis
│   ├─📁 data         ->  Módulo de preenchimento de dados fake e controllador do streamlit
│   │   └─🐍 projects_factory.py ->  Dados fake usando o Faker e o Factory
│   │   └─🐍 inserir.py ->  Inserção de dados no banco de dados
│   │    ...
│   ├─📁 database      ->  Módulo de conexão com SQLAlchemy
│   │   └─🐍 session.py ->  Sessão de conexão
│   ├─📁 models        ->  Módulo de modelos do banco de dados
│   │   └─🐍 projects.py ->  Model de projects
│   │   └─ ...          ->  Outros modelos
├─📁 migrations        ->  Migrations da aplicação usando o Alembic
│   └─ ...             ->  Arquivos padrão do Alembic
├─📁 scripts           ->  scripts bases transformados em sqlalchemy orm
│       └─🛢 grentabilidade_liquida.sql ->  Script SQL puro (sqlite)
│       └─🛢 porcentagem_excedentes.sql ->  Script SQL puro (sqlite)
│       └─🛢 mais_receita_2_semestre_2024.sql ->  Script SQL puro (sqlite)
│       ...             
├─📁 tests             ->  Testes da aplicação
│   ├─📁 e2e           ->  Implementações de testes automatizados em pytest
│   └─ ...             ->  Outros testes
|─🐍 generate_projects.py ->  Script de execução para inserir dados fakes
├─📄 .env_sample       ->  Exemplo de .env
├─📄 .gitignore
├─📄 Makefile          ->  Automações para o ambiente
├─📄 pyproject.toml    ->  Definições para o projeto
├─📄 README.md
└─📄 ruff.toml         ->  Regras de linter e formatter

```

## Montando o ambiente

Este repositório esta organizando em um devcontainer.
E para instacia-lo no VSCODE é recomendado as seguintes configurações:

#### Extenções recomendadas

- Name: Remote Development
- Id: ms-vscode-remote.vscode-remote-extensionpack
- Description: An extension pack that lets you open any folder in a container, on a remote machine, or in WSL and take advantage of VS Code's full feature set.
- Version: 0.25.0
- Publisher: Microsoft
- VSCode Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack

#### Docker Engine

É obrigatório ter o Docker Engine já instalado e cunfigurado. Para mais informações de como instalar o Docker Engine em seu SO, ver em:

- Instruções para instalação do Docker Engine: [Ver o link](https://docs.docker.com/engine/install/)

#### Procedimento para instanciar o projeto no VSCODE
1. Com o pack de extenções instalado,
1. Realize o clone/fork deste repositório,
1. Abra o diretorio deste repositorio no VSCODE como um projeto,
1. Use o Comando _Dev Containers: Reopen in Container_ da paleta de comandos do VSCODE. _(F1, Ctrl+Shift+P)_.

Depois da compilação do container o VSCode abrirá o repositório em um ambiente encapsulado e executando diretamente de dentro do container como configurado nas definições do **/.devconainer**.

#### Procedimento para iniciar
1. inicie o ambiente virtual do poetry
```
$> poetry shell
```
2. instale as dependencias definidas no pyproject.toml
```
$> poetry shell
```
- Pronto agora voce esta pronto para começar a usar!

### Principais comandos

#### Levantar dados fakes com o Faker
```
$> make up
```

#### Levantar o dashboard
```
$> make start
```

#### Adcionar novas dependencias
```
# Adicionar uma nova lib para o runtime do projeto
$> poetry add <<nome_da_lib>>

# Adicionar uma nova lib para o ambiente de desenvolvimento
$> poetry add <<nome_da_lib>> --group dev
```
#### Operar o alembic
```
# Criar um novo arquivo de migração
$> alembic revision --autogenerete -m "nome_da_migracao"

# Atualizar o banco de dados
$> alembic upgrade head
```

#### Desafio:

- [Planilha](docs/desafios.md)
