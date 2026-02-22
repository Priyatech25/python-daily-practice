# Rank employees by salary within each department
SELECT 
    employee_id,
    department,
    monthly_income,
    RANK() OVER (
        PARTITION BY department 
        ORDER BY monthly_income DESC
    ) AS salary_rank
FROM employees;

# Running average salary by department
SELECT 
    employee_id,
    department,
    monthly_income,
    AVG(monthly_income) OVER (
        PARTITION BY department
        ORDER BY employee_id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_avg_salary
FROM employees;

# Compare employee salary to department average
SELECT 
    employee_id,
    department,
    monthly_income,
    AVG(monthly_income) OVER (PARTITION BY department) AS dept_avg_salary,
    monthly_income - AVG(monthly_income) OVER (PARTITION BY department) 
        AS salary_difference
FROM employees;

# Identify Top 3 Highest Paid per Department

SELECT *
FROM (
    SELECT 
        employee_id,
        department,
        monthly_income,
        DENSE_RANK() OVER (
            PARTITION BY department 
            ORDER BY monthly_income DESC
        ) AS rank_in_dept
    FROM employees
) ranked
WHERE rank_in_dept <= 3;