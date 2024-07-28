def count_columns_and_extract_years(df):
  """
  Counts the number of columns in a DataFrame and extracts the year from date columns.

  Args:
    df: A pandas DataFrame.

  Returns:
    A tuple containing:
      - The number of columns in the DataFrame.
      - A list of years extracted from the date columns.
  """

  num_columns = len(df.columns)
  years = []
  for col in df.columns:
    try:
      # Attempt to convert the column name to a datetime object
      year = pd.to_datetime(col).year
      years.append(year)
    except ValueError:
      # If conversion fails, it's not a date column
      pass

  return num_columns, years
