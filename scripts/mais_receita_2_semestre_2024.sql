SELECT 
    project_id,
    end_date,
    project_name,
    revenue
FROM 
    Projects
WHERE 
    end_date <= '2024-06-30'
ORDER BY 
    revenue 
DESC
LIMIT 5;
