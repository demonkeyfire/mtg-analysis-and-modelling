###################################################################################################
# -------------------------------------- PYTHON LIBRARIES --------------------------------------- #
###################################################################################################

# Data libraries
import pandas as pd



###################################################################################################
# ------------------------------------------ FUNCTIONS ------------------------------------------ #
###################################################################################################

# Function for identifying difference empty value types in a dataframe per column
def empty_value_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate a detailed summary of empty values across all columns in a DataFrame.

    This function counts each type of "empty" value separately:
      - Python `None`
      - `NaN` (float NaN specifically)
      - Explicit `pd.NA`

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame to analyze.

    Returns
    -------
    pd.DataFrame
        A summary DataFrame with one row per column in the input,
        containing counts of each type of empty value:
        - "column": column name
        - "None_count": number of Python `None` values
        - "NaN_count": number of float `NaN` values
        - "pd.NA_count": number of explicit `pd.NA` values
    """
    summary = []

    for col in df.columns:
        # Count explicit Python None values
        none_count = (df[col].map(lambda x: x is None)).sum()
        
        # Count explicit pd.NA values
        pdna_count = (df[col].map(lambda x: x is pd.NA)).sum()
        
        # Count NaN values (exclude None and pd.NA)
        nan_count = df[col].apply(lambda x: isinstance(x, float) and pd.isna(x)).sum()

        summary.append({
            "column": col,
            "None_count": none_count,
            "NaN_count": nan_count,
            "pd.NA_count": pdna_count
        })

    return pd.DataFrame(summary)