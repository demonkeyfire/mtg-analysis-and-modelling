###################################################################################################
# -------------------------------------- PYTHON LIBRARIES --------------------------------------- #
###################################################################################################

# Data libraries
import numpy  as np
import pandas as pd



###################################################################################################
# ------------------------------------------ FUNCTIONS ------------------------------------------ #
###################################################################################################

# Function for extracting the purchase URLs of set products
def extract_purchase_urls(cell):
    """
    Extracts purchase URLs for 'cardKingdom' and 'tcgplayer' from a given cell.

    The function handles cases where the input cell is either:
    - A single dictionary containing one key-value pair (e.g. {'tcgplayer': 'url'}),
    - A list of dictionaries, each with one key-value pair (e.g. [{'cardKingdom': 'url'}, {'tcgplayer': 'url'}]),
    - Or other types (which return NaN values).

    Parameters
    ----------
    cell : dict, list, or other
        The input cell containing purchase location and URL information.

    Returns
    -------
    pandas.Series
        A Series with two columns:
        - 'CARD_KINGDOM_URL': URL if available, otherwise NaN.
        - 'TCG_PLAYER_URL': URL if available, otherwise NaN.
    """

    # Default output with NaN values
    result = {'CARD_KINGDOM_URL': np.nan, 'TCG_PLAYER_URL': np.nan}
    
    # Case 1: If the cell is a dictionary
    if isinstance(cell, dict):
        key, value = next(iter(cell.items()), (None, None))  # Get the first key-value pair safely
        if key == 'cardKingdom':
            result['CARD_KINGDOM_URL'] = value
        elif key == 'tcgplayer':
            result['TCG_PLAYER_URL'] = value

    # Case 2: If the cell is a list of dictionaries
    elif isinstance(cell, list):
        for d in cell:
            if isinstance(d, dict):
                key, value = next(iter(d.items()), (None, None))  # Get the first key-value pair safely
                if key == 'cardKingdom':
                    result['CARD_KINGDOM_URL'] = value
                elif key == 'tcgplayer':
                    result['TCG_PLAYER_URL'] = value

    # Return as a Pandas Series so it can be easily joined to a DataFrame
    return pd.Series(result)
