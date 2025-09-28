###################################################################################################
# -------------------------------------- PYTHON LIBRARIES --------------------------------------- #
###################################################################################################

# Data libraries
import sys
import pandas as pd



###################################################################################################
# ------------------------------------------ FUNCTIONS ------------------------------------------ #
###################################################################################################

# Function for variable and memory management
def list_variables_memory(globals_dict=None, sort_by_size=True):

    """
    List all variables in the given globals() or any dictionary of variables,
    returning a DataFrame with variable name, type, and size in KB.

    Parameters:
        globals_dict (dict): Dictionary of variables, defaults to globals().
        sort_by_size (bool): Whether to sort the resulting DataFrame by Size_KB descending.

    Returns:
        pd.DataFrame: DataFrame with columns ["Variable", "Type", "Size_KB"].
    """

    # Creating a dictionary of the variables
    if globals_dict is None:
        globals_dict = globals()

    # Empty list for storing the variable info
    var_info = []

    # Looping through the variables and appending to the empty list
    for name, val in list(globals_dict.items()):  # snapshot to avoid RuntimeError
        try:
            size_kb = sys.getsizeof(val) / 1024
        except Exception:
            size_kb = None
        var_info.append({"Variable": name, "Type": type(val).__name__, "Size_KB": size_kb})

    # Converting the variable list to a dataframe
    df_vars = pd.DataFrame(var_info)

    # Sorting the variables by KB size
    if sort_by_size:
        df_vars = df_vars.sort_values("Size_KB", ascending=False).reset_index(drop=True)

    # Returning the dataframe
    return df_vars