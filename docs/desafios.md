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

> **Resposta:** 
```sql

SELECT -- selecione as colunas que devem ser vistas
    project_name,
    end_date,
    (revenue - project_cost) AS rentabilidade_liquida_ultimo_ano -- ainda é as que devem ser vistas mais tem um calculo..
FROM  -- de que tabela
    Projects 
WHERE -- Filtrar
    end_date BETWEEN DATE('now', '-1 year') AND DATE('now'); -- Filtra os projetos cuja data de término (end_date) está entre[BETWEEN] um ano atrás e a data atual (incluindo o ano corrente).

--	strftime('%Y', end_date) = strftime('%Y', DATE('now', '-1 year')); -- sem o ano corrente (strftime extrai diretamente das colunas)
```

> **Nota:** Estou usando o sqlite mas para o postgresql por exemplo so mudaria o tratamento pelas datas:
```sql
WHERE
   EXTRACT(YEAR FROM end_date) = EXTRACT(YEAR FROM CURRENT_DATE) - 1;
```

- [ ] Quais foram os 5 projetos que geraram mais receita até o final do segundo trimestre de 2024?
> **Resposta:** 
```sql
SELECT 
	project_id,
	project_name,
	revenue
FROM 
	Projects
WHERE 
	end_date <= '2024-06-30' -- até o final do segundo trimestre de 2024
ORDER BY -- ordena por
	revenue 
	DESC -- em ordem decrescente 
LIMIT 5; --limita em 5
```

- [ ] Qual foi a porcentagem de projetos que excederam o orçamento inicial a cada semestre nos últimos 2 
anos?
```sql
SELECT 
FROM
WHERE
```


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
