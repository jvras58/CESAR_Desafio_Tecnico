SELECT 
    project_name,
    end_date,
    (revenue - project_cost) AS rentabilidade_liquida_ultimo_ano
FROM 
    Projects
WHERE
    end_date BETWEEN DATE('now', '-1 year') AND DATE('now');
