"""
    8.	Write a Python function that takes a dictionary of data and converts it into a Pandas DataFrame.
         Perform operations like adding a new column and filtering rows based on a condition. (4 Marks)
"""

import pandas as pd

def process_data(data_dict):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(data_dict)
    print("Original DataFrame:")
    print(df)
    
    # Add a new column
    df['Total'] = df['Math'] + df['Science']
    print("\nAfter adding Total column:")
    print(df)
    
    # Filter rows where Math > 50
    filtered_df = df[df['Math'] > 50]
    print("\nFiltered DataFrame (Math > 50):")
    print(filtered_df)
    
    return df, filtered_df

# Test the function
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Math': [85, 45, 78, 92],
    'Science': [90, 55, 82, 88]
}

original_df, result_df = process_data(data)