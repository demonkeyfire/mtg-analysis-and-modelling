###################################################################################################
# -------------------------------------- PYTHON LIBRARIES --------------------------------------- #
###################################################################################################

# Data libraries
import pandas as pd



###################################################################################################
# ------------------------------------------ FUNCTIONS ------------------------------------------ #
###################################################################################################

# Function for showing the hierarchy of a dictionary or the schema of a single level
def print_dict_structure(data, max_depth=None, _indent=0):

    """
    Recursively prints the hierarchical structure of a dictionary or list,
    including the length of each element where applicable.
    
    If max_depth=1, returns a DataFrame with columns: KEY_NAME, DATA_TYPE, LENGTH.
    
    Args:
        data: The dictionary or list to explore.
        max_depth: Limit how deep to traverse (None for full depth).
    
    Returns:
        pd.DataFrame if max_depth=1, otherwise None (prints output).
    """
    
    # Check if we are at the top level and max_depth=1 to return DataFrame instead of printing
    if max_depth == 1 and _indent == 0:
        # Initialize list to collect rows for the DataFrame
        rows = []

        # If data is a dictionary, iterate over its keys and values
        if isinstance(data, dict):
            for key, value in data.items():
                # Determine length if possible, otherwise set to 0
                length = len(value) if hasattr(value, "__len__") and not isinstance(value, (str, bytes)) else 0
                # Append a tuple of key name, data type, and length to rows
                rows.append((key, type(value).__name__, length))

        # If data is a list, take the first element (assumed dict) and do the same
        elif isinstance(data, list) and data:
            for key, value in data[0].items():
                # Determine length if possible, otherwise set to 0
                length = len(value) if hasattr(value, "__len__") and not isinstance(value, (str, bytes)) else 0
                # Append a tuple of key name, data type, and length to rows
                rows.append((key, type(value).__name__, length))

        # Convert collected rows into a DataFrame with specific column names
        return pd.DataFrame(rows, columns=["KEY_NAME", "DATA_TYPE", "LENGTH"])
    
    # Create a prefix for indentation when printing nested structures
    prefix = "  " * _indent

    # If data is a dictionary, iterate recursively
    if isinstance(data, dict):
        for key, value in data.items():
            # Prepare a string showing type and length for printing
            length_info = f", len={len(value)}" if hasattr(value, "__len__") and not isinstance(value, (str, bytes)) else ""
            # Print the key name, type, and length with proper indentation
            print(f"{prefix}{key} ({type(value).__name__}{length_info})")
            # Recurse into value if max_depth is not reached
            if max_depth is None or _indent < max_depth - 1:
                print_dict_structure(value, max_depth, _indent + 1)

    # If data is a list, recurse into the first element (assuming homogeneous elements)
    elif isinstance(data, list):
        if data and (max_depth is None or _indent < max_depth - 1):
            print_dict_structure(data[0], max_depth, _indent + 1)

    # For non-dict and non-list elements, print their type and length
    else:
        # Prepare a string showing type and length for printing
        length_info = f", len={len(data)}" if hasattr(data, "__len__") and not isinstance(data, (str, bytes)) else ""
        # Print the type and length with proper indentation
        print(f"{prefix}{type(data).__name__}{length_info}")