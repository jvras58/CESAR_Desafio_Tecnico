
# Dashboard do CESAR - Desafio Técnico

<div align="center">
  <img src="https://www.cesar.org.br/_next/image?url=%2Flogo.png&w=128&q=75" alt="Logo da Cesar" width="120px" height="120px"/>
</div>
<h2 align="center">Gestão de dados financeiros de projetos</h2>



## 📖 Sobre o Projeto

Este é um projeto que visa contemplar o processo seletivo de estagio na cesar

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
| Taskipy                       | v1.12.x   |

### Organização do projeto
```
/
├─📁 .devcontainer   ->  [Configurações do devcontainer]
├─📁 .vscode         ->  [Definições de ambiente para o VSCode]
├─📁 docs            ->  [artefatos para documentação do repo]
├─📁 app             ->  [Implementação]
│   ├─🐍 app.py     ->  [Entrypoint da aplicação]
│   ├─📁 config     ->  [Modulo de configuração]
    │     └─🐍Settings.py  ->  [configuração de variaveis]
│   ├─📁 dados     ->  [Modulo de preenchimento de dados fake]
    │     └─🐍projects.py  ->  [dados fake]
│   ├─📁 database     ->  [None]
    │     └─🐍session.py  ->  [Mone]
│   │   ...
│   └─📁 
├─📁 tests           ->  [Testes da aplicação]
│   ├─📁 e2e        ->  [Implementações de testes automatizados em pytest]
│   │                     
├─📄 .env_sample     ->  [exemplo de .env]
├─📄 .gitignore
├─📄 Makefile        ->  [Automações para o ambiente]
├─📄 pyproject.toml  ->  [Definições para o projeto]
├─📄 README.md
└─📄 ruff.toml       ->  [Regras de linter e formarter]
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

### Principais comandos

#### Levantar serviço
```
$> make start
```
#### Executar testes 
```
$> make test_all
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

- [Leia](docs/CESAR_Desafio.pdf)

- [Planilha](docs/desafios.md)
> **Nota:** Este documento será atualizado conforme o progresso das tarefas e a resolução.

