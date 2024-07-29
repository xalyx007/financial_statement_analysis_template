import pandas as pd

def read_income_stmt(tikr):
    """
    Reads and processes the income statement and cash flow data from the provided ticker object.

    Parameters:
    tikr (object): An object with 'income_stmt' and 'cashflow' attributes that provide income statement and cash flow data.

    Returns:
    pd.DataFrame: Combined processed income statement and cash flow data.
    """
    # Read income statement data and convert to millions
    try:
        df1 = tikr.income_stmt / 1e6
    except AttributeError:
        raise ValueError("The provided ticker object does not have an 'income_stmt' attribute.")
    
    # Reverse columns for chronological order (if needed)
    df1 = df1[df1.columns[::-1]]
    
    # Define the rows to extract from the income statement
    rows_df1 = [
        'Total Revenue', 'EBIT', 'EBITDA', 'Interest Expense', 'Interest Income', 
        'Tax Provision', 'Minority Interests', 'Diluted Average Shares'
        ]
    
    # Filter out rows that are in the DataFrame
    valid_rows_df1 = df1.loc[df1.index.intersection(rows_df1)]
    
    # Create a DataFrame filled with zeros for missing rows
    df1_zero_filled = pd.DataFrame(0, index=rows_df1, columns=df1.columns)
    
    # Fill the zero-filled DataFrame with valid rows
    df1_zero_filled.loc[valid_rows_df1.index] = valid_rows_df1.astype(float)
    
    # Read cash flow data (for Depreciation & Amortization) and convert to millions
    try:
        df2 = tikr.cashflow / 1e6
    except AttributeError:
        raise ValueError("The provided ticker object does not have a 'cashflow' attribute.")
    
    # Reverse columns for chronological order (if needed)
    df2 = df2[df2.columns[::-1]]
    
    # Define the rows to extract from the cash flow statement
    rows_df2 = ['Depreciation And Amortization']
    
    # Create a DataFrame filled with zeros for missing rows, ensuring dtype is float64
    df2_zero_filled = pd.DataFrame(0.0, index=rows_df2, columns=df2.columns)
    
    # Filter out rows that are in the DataFrame
    valid_rows_df2 = df2.loc[df2.index.intersection(rows_df2)]
    
    # Fill the zero-filled DataFrame with valid rows
    df2_zero_filled.loc[valid_rows_df2.index] = valid_rows_df2.astype(float)
    
    # Combine both dataframes and return
    combined_df = pd.concat([df1_zero_filled, df2_zero_filled], axis=0)

    # Define the desired row order
    desired_order = [
        'Total Revenue', 'EBITDA', 'Depreciation And Amortization', 'EBIT', 
        'Interest Expense', 'Interest Income', 'Tax Provision', 
        'Minority Interests', 'Diluted Average Shares'
    ]
    
    # Reindex the combined dataframe to match the desired order
    combined_df = combined_df.reindex(desired_order)
    
    return combined_df


def read_cashflow(tikr):
    """
    Reads and processes the cash flow data from the provided ticker object.

    Parameters:
    tikr (object): An object with a 'cashflow' attribute that provides cash flow data.

    Returns:
    pd.DataFrame: Processed cash flow data.
    """
    # Read cash flow data and convert to millions
    try:
        df1 = tikr.cashflow / 1e6
    except AttributeError:
        raise ValueError("The provided ticker object does not have a 'cashflow' attribute.")
    
    # Reverse columns for chronological order (if needed)
    df1 = df1[df1.columns[::-1]]
    
    # Define the rows to extract
    rows_df1 = [
        'Capital Expenditure', 'Change In Working Capital', 'Free Cash Flow'
    ]

    # Create a DataFrame filled with zeros for missing rows, ensuring dtype is float64
    df1_zero_filled = pd.DataFrame(0.0, index=rows_df1, columns=df1.columns)
    
    # Filter out rows that are in the DataFrame
    valid_rows_df1 = df1.loc[df1.index.intersection(rows_df1)]
    
    # Fill the zero-filled DataFrame with valid rows
    df1_zero_filled.loc[valid_rows_df1.index] = valid_rows_df1.astype(float)
    
    return df1_zero_filled


def read_balance_sheet(tikr):
    """
    Reads and processes the balance sheet from the provided ticker object.

    Parameters:
    tikr (object): An object with a 'balance_sheet' attribute that provides balance sheet data.

    Returns:
    pd.DataFrame: Processed balance sheet data.
    """
    
    # Read balance sheet data and convert to millions
    try:
        df1 = tikr.balance_sheet / 1e6
    except AttributeError:
        raise ValueError("The provided ticker object does not have a 'balance_sheet' attribute.")
    
    # Reverse columns for chronological order (if needed)
    df1 = df1[df1.columns[::-1]]
    
    # Define the rows to extract
    rows_df1 = [
        'Cash And Cash Equivalents', 'Current Debt', 'Long Term Debt', 
        'Capital Lease Obligations', 'Goodwill', 'Common Stock Equity', 'Total Debt'
    ]
    
    # Create a DataFrame filled with zeros for missing rows, ensuring dtype is float64
    df1_zero_filled = pd.DataFrame(0.0, index=rows_df1, columns=df1.columns)
    
    # Filter out rows that are in the DataFrame
    valid_rows_df1 = df1.loc[df1.index.intersection(rows_df1)]
    
    # Fill the zero-filled DataFrame with valid rows
    df1_zero_filled.loc[valid_rows_df1.index] = valid_rows_df1.astype(float)
    
    # Compute 'Financial Debt'
    if 'Current Debt' in df1_zero_filled.index and 'Long Term Debt' in df1_zero_filled.index:
        df1_zero_filled.loc['Financial Debt'] = df1_zero_filled.loc['Current Debt'] + df1_zero_filled.loc['Long Term Debt']
    else:
        df1_zero_filled.loc['Financial Debt'] = pd.NA  # Or handle the missing data in another appropriate way
    
    return df1_zero_filled.loc[['Cash And Cash Equivalents', 'Financial Debt', 
                                'Capital Lease Obligations', 'Goodwill', 'Common Stock Equity', 'Total Debt']]

