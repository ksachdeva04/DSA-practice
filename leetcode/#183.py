#183 Customers Who Never Order
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    merged = pd.merge(
        customers,
        orders,
        left_on='id',
        right_on='customerId',
        how='left',
        indicator=True
    )

    result = merged[merged['_merge'] == 'left_only']

    return result[['name']].rename(columns={'name': 'Customers'})