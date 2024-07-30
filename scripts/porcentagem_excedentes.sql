SELECT
    strftime('%Y', end_date) AS year,
    CASE
        WHEN strftime('%m', end_date) BETWEEN '01' AND '06' THEN '1st Semestre'
        WHEN strftime('%m', end_date) BETWEEN '07' AND '12' THEN '2nd Semestre'
    END AS Semestre,
    COUNT(*) AS total_projects,
    SUM(CASE WHEN project_cost > initial_budget THEN 1 ELSE 0 END) AS projetos_excedido_orçamento,
    (SUM(CASE WHEN project_cost > initial_budget THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS porcentagem_excedido_orçamento
FROM Projects
WHERE end_date >= date('now', '-2 years')
GROUP BY year, Semestre
ORDER BY year, Semestre;
