#177 Nth Highest Salary

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    col = f'getNthHighestSalary({N})'

    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if N > len(salaries) or N <= 0:
        return pd.DataFrame({col: [None]})

    return pd.DataFrame({
        col: [salaries.iloc[N-1]]
    })