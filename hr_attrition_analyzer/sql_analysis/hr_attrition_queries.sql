 HR ATTRITION SQL ANALYSIS

 1. Total Employees

SELECT COUNT(*) AS total_employees
FROM employees;

 2. Attrition Rate

SELECT 
    COUNT(CASE WHEN attrition = 'Yes' THEN 1 END) * 100.0 / COUNT(*) 
    AS attrition_rate_percentage
FROM employees;

3. Average Salary by Department
SELECT department, 
       AVG(monthly_income) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

 4. Employees Who Left and Did Overtime
SELECT employee_id, department, monthly_income
FROM employees
WHERE attrition = 'Yes'
AND overtime = 'Yes';

5. Department with Highest Attrition
SELECT department,
       COUNT(*) AS total_left
FROM employees
WHERE attrition = 'Yes'
GROUP BY department
ORDER BY total_left DESC;

6. Employees Earning Below Company Average
SELECT *
FROM employees
WHERE monthly_income < (
    SELECT AVG(monthly_income) FROM employees
);

7. Average Years at Company by Attrition
SELECT attrition,
       AVG(years_at_company) AS avg_years
FROM employees
GROUP BY attrition;