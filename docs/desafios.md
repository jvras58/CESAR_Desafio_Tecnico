# Lista de Atividades 

## Atividades Pendentes

### Considerando que a tabela foi construída a partir do SQL

```sql
CREATE TABLE Projects (
   project_id INT PRIMARY KEY,
   project_name VARCHAR(150) NOT NULL,
   start_date DATE NOT NULL,
   end_date DATE NOT NULL,
   initial_budget DECIMAL(12, 2) NOT NULL,
   project_cost DECIMAL(12, 2) NOT NULL,
   revenue DECIMAL(12, 2) NOT NULL
);

```

> **Nota - 1:** Escreva uma consulta SQL para cada um dos itens acima e justifique sua resposta, 
> explicando o raciocínio para construir cada query;


- [ ] Qual foi a rentabilidade líquida (receita [revenue] - custo [project_cost]) de cada projeto realizado no último ano?
- [ ] Quais foram os 5 projetos que geraram mais receita até o final do segundo trimestre de 2024?
- [ ] Qual foi a porcentagem de projetos que excederam o orçamento inicial a cada semestre nos últimos 2 
anos?

> **Nota - 2:** Em seguida, descreva como você apresentaria graficamente os resultados das consultas 
> SQL anteriores para o time de gestão. Justifique suas escolhas de visualização.


- [ ] Crie um DOC, PPT ou Canva para montar seu desafio e enviar como resposta para o e-mail


## Atividades Derivadas

- [v] Criar dados fakes para "povoar" essa tabela 
> **Nota:** usando o alembic e o faker para criar e popular a tabela 

- [ ] Representar graficamente usando o streamlit
> **Nota:** Estudar mais a fundo uma boa arquitetura para isso

- [ ] Testes e2e

- [v] Conteinizar a aplicação  
