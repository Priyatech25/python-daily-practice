import pandas as pd


df = pd.read_csv("C:/Users/K.PRIYA DARSHINI/python-daily-practice/hr_attrition_analyzer/data/WA_Fn-UseC_-HR-Employee-Attrition.csv")


dept_attrition = df.groupby(['Department','Attrition']).size().reset_index(name='count')
print("--- Department-wise Attrition ---")
print(dept_attrition)


avg_salary = df.groupby('Attrition')['MonthlyIncome'].mean().reset_index()
print("\n--- Average Salary by Attrition ---")
print(avg_salary)


job_role_attrition = df.groupby('JobRole').apply(
    lambda x: pd.Series({
        'total_employees': len(x),
        'attrition_count': sum(x['Attrition']=='Yes'),
        'attrition_rate': round(sum(x['Attrition']=='Yes')*100/len(x),2)
    })
).reset_index()

print("\n--- Job Role Attrition Rate ---")
print(job_role_attrition)