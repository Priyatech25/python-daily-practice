-- 1. Department-wise attrition count
SELECT Department, Attrition, COUNT(*) AS count
FROM employees
GROUP BY Department, Attrition;

-- 2. Average salary by attrition
SELECT Attrition, AVG(MonthlyIncome) AS avg_salary
FROM employees
GROUP BY Attrition;

-- 3. Job role-wise attrition rate
SELECT JobRole, 
       COUNT(*) AS total_employees,
       SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_count,
       ROUND(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS attrition_rate
FROM employees
GROUP BY JobRole;