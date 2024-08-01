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


- [x] Qual foi a rentabilidade líquida (receita [revenue] - custo [project_cost]) de cada projeto realizado no último ano?

> **Resposta:** 
```sql

SELECT -- 
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

- [x] Quais foram os 5 projetos que geraram mais receita até o final do segundo trimestre de 2024?
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

- [x] Qual foi a porcentagem de projetos que excederam o orçamento inicial a cada semestre nos últimos 2 
anos?
```sql
SELECT
    strftime('%Y', end_date) AS year, -- Extrai o ano da data de término (end_date) dos projetos.
    CASE
        WHEN strftime('%m', end_date) BETWEEN '01' AND '06' THEN '1st Semestre'
        WHEN strftime('%m', end_date) BETWEEN '07' AND '12' THEN '2nd Semestre' -- Usa a função strftime para extrair o mês (%m) da data de término e, com base no mês, atribui o semestre (1º ou 2º).
    END AS Semestre,
    COUNT(*) AS total_projects, -- Faz os calculos de custo final e calculo de porcentagem 
    SUM(CASE WHEN project_cost > initial_budget THEN 1 ELSE 0 END) AS projetos_excedido_orçamento, -- Filtra os projetos cuja data de término (end_date) seja nos últimos dois anos a partir da data atual.
    (SUM(CASE WHEN project_cost > initial_budget THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS porcentagem_excedido_orçamento
FROM Projects
WHERE end_date >= date('now', '-2 years')
GROUP BY year, Semestre -- agrupa por semestre
ORDER BY year, Semestre; -- ordena por semestre
```


> **Nota - 2:** Em seguida, descreva como você apresentaria graficamente os resultados das consultas 
> SQL anteriores para o time de gestão. Justifique suas escolhas de visualização.


- [x] Crie um DOC, PPT ou Canva para montar seu desafio e enviar como resposta para o e-mail


## Atividades Derivadas

- [x] Criar dados fakes para "povoar" essa tabela 
> **Nota:** usando o alembic e o faker para criar e popular a tabela 

- [x] Representar graficamente usando o streamlit
> **Nota:** Estudar mais a fundo uma boa arquitetura de conexão com um banco de dados externo

- [ ] Testes e2e
> **Nota:** usando pytest

- [x] Conteinizar a aplicação  
