import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = customers.merge(orders ,how = 'left', left_on ='id' ,right_on = 'customerId')
    merged_df.rename(columns={'name':'Customers'},inplace = True)
    return merged_df.loc[merged_df['id_y'].isnull(),['Customers']]
