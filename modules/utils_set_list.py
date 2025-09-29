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



###################################################################################################
# ------------------------------------------ VARIABLES ------------------------------------------ #
###################################################################################################

# Dictionary for renaming the original set list dataframe
columns__rename_set_list = {'baseSetSize'                      : 'BASE_SET_SIZE'
                           ,'code'                             : 'SET_CODE'
                           ,'isFoilOnly'                       : 'FOIL_FLAG'
                           ,'isOnlineOnly'                     : 'ONLINE_FLAG'
                           ,'keyruneCode'                      : 'KEYRUNE_CODE'
                           ,'languages'                        : 'LANGUAGES'
                           ,'name'                             : 'SET_NAME'
                           ,'releaseDate'                      : 'RELEASE_DATE'
                           ,'sealedProduct'                    : 'PRODUCT_INFO'
                           ,'tcgplayerGroupId'                 : 'TCGPG_ID'
                           ,'totalSetSize'                     : 'TOTAL_SET_SIZE'
                           ,'type'                             : 'SET_TYPE'
                           ,'block'                            : 'SET_BLOCK_NAME'
                           ,'isNonFoilOnly'                    : 'NON_FOIL_FLAG'
                           ,'parentCode'                       : 'SET_PARENT_CODE'
                           ,'mcmId'                            : 'CM_ID'
                           ,'mcmName'                          : 'CM_NAME'
                           ,'tokenSetCode'                     : 'SET_TOKEN_CODE'
                           ,'translations.Chinese Simplified'  : 'TRANSLATION_SIMPLIFIED_CHINESE'
                           ,'translations.Chinese Traditional' : 'TRANSLATION_TRADITIONAL_CHINESE'
                           ,'translations.French'              : 'TRANSLATION_FRENCH'
                           ,'translations.German'              : 'TRANSLATION_GERMAN'
                           ,'translations.Italian'             : 'TRANSLATION_ITALIAN'
                           ,'translations.Japanese'            : 'TRANSLATION_JAPANESE'
                           ,'translations.Korean'              : 'TRANSLATION_KOREAN'
                           ,'translations.Portuguese (Brazil)' : 'TRANSLATION_BRAZILIAN_PORTUGESE'
                           ,'translations.Russian'             : 'TRANSLATION_RUSSIAN'
                           ,'translations.Spanish'             : 'TRANSLATION_SPANISH'
                           ,'cardsphereSetId'                  : 'CS_SET_ID'
                           ,'decks'                            : 'SET_DECKS'
                           ,'mcmIdExtras'                      : 'CM_ID_ADD'
                           ,'mtgoCode'                         : 'MTGO_SET_CODE'
                           ,'isPartialPreview'                 : 'PREVIEW_FLAG'
                           ,'isForeignOnly'                    : 'FOREIGN_FLAG'}

# Columns for the main set table
columns__sets_info = ['SET_CODE'
                     ,'SET_NAME'
                     ,'RELEASE_DATE'
                     ,'SET_TYPE'
                     ,'SET_BLOCK_NAME'
                     ,'SET_PARENT_CODE'
                     ,'SET_TOKEN_CODE'
                     ,'BASE_SET_SIZE'
                     ,'TOTAL_SET_SIZE'
                     ,'DECK_COUNT'
                     ,'FOIL_FLAG'
                     ,'NON_FOIL_FLAG'
                     ,'FOREIGN_FLAG'
                     ,'ONLINE_FLAG'
                     ,'PREVIEW_FLAG'
                     ,'CM_ID'
                     ,'CM_ID_ADD'
                     ,'CM_NAME'
                     ,'CS_SET_ID'
                     ,'KEYRUNE_CODE'
                     ,'MTGO_SET_CODE'
                     ,'TCGPG_ID']

# Dictionary for renaming the deck table columns
columns__rename_set_decks = {'code'               : 'SET_CODE'
                            ,'commander'          : 'COMMANDER'
                            ,'displayCommander'   : 'DISPLAY_COMMANDER'
                            ,'mainBoard'          : 'DECK_CARDS'
                            ,'name'               : 'DECK_NAME'
                            ,'planes'             : 'PLANES'
                            ,'releaseDate'        : 'RELEASE_DATE'
                            ,'schemes'            : 'SCHEMES'
                            ,'sealedProductUuids' : 'SEALED_PRODUCT_IDS'
                            ,'sideBoard'          : 'SIDE_BOARD_CARDS'
                            ,'type'               : 'DECK_TYPE'}

# Columns included in the master table for set decks
columns__set_deck_info = ['SET_CODE'
                         ,'SET_NAME'
                         ,'DECK_NAME'
                         ,'RELEASE_DATE'
                         ,'DECK_TYPE'
                         ,'COMMANDER'
                         ,'SEALED_PRODUCT_IDS']

## Relational table list
columns__relational_columns = ['DECK_CARDS'
                              ,'SIDE_BOARD_CARDS'
                              ,'DISPLAY_COMMANDER'
                              ,'PLANES'
                              ,'SCHEMES']

# Columns to be in the display commanders lookup table
columns__display_commanders = ['SET_CODE'
                              ,'SET_NAME'
                              ,'DECK_NAME'
                              ,'DISPLAY_COMMANDER']

# Columns for building the deck cards
columns__set_decks_cards = ['SET_CODE'
                           ,'SET_NAME'
                           ,'DECK_NAME'
                           ,'DECK_CARDS']

# Columns for building the side deck dataframe
columns__set_decks_side_board = ['SET_CODE'
                                ,'SET_NAME'
                                ,'DECK_NAME'
                                ,'SIDE_BOARD_CARDS']

# Columns for building the planes dataframe
columns__set_decks_planes = ['SET_CODE'
                            ,'SET_NAME'
                            ,'DECK_NAME'
                            ,'PLANES']

# Columns for building the schemes table
columns__set_decks_schemes = ['SET_CODE'
                             ,'SET_NAME'
                             ,'DECK_NAME'
                             ,'SCHEMES']

# Product info table column renaming dictionary
columns__rename_product_info = {'category'           : 'CATEGORY'
                               ,'identifiers'        : 'IDENTIFIERS'
                               ,'name'               : 'PRODUCT_NAME'
                               ,'purchaseUrls'       : 'PURCHASE_URL'
                               ,'subtype'            : 'SUBTYPE'
                               ,'uuid'               : 'PRODUCT_UUID'
                               ,'cardCount'          : 'PRODUCT_CARD_COUNT'
                               ,'releaseDate'        : 'PRODUCT_RELEASE_DATE'
                               ,'language'           : 'PRODUCT_LANGUAGE'
                               ,'abuId'              : 'ABU_GAMES_ID'
                               ,'cardtraderId'       : 'CARD_TRADER_ID'
                               ,'mcmId'              : 'CARD_MARKET_ID'
                               ,'tcgplayerProductId' : 'TCG_PLAYER_ID'
                               ,'tntId'              : 'TOAD_AND_TROLL_ID'
                               ,'cardKingdomId'      : 'CARD_KINGDOM_ID'
                               ,'scgId'              : 'STAR_CITY_GAMES_ID'
                               ,'csiId'              : 'COOL_STUFF_INC_ID'
                               ,'miniaturemarketId'  : 'MINIATURE_MARKET_ID'
                               ,'mvpId'              : 'MVP_GAMES_ID'
                               ,'contents_count'     : 'CONTENTS_COUNT'
                               ,'contents_name'      : 'CONTENTS_NAME'
                               ,'contents_uuid'      : 'CONTENTS_UUID'
                               ,'contents_code'      : 'CONTENTS_CODE'
                               ,'contents_number'    : 'CONTENTS_CARD_NUMBER'} 

# List of columns for reorganising the product info table
columns__set_product_info = ['SET_CODE'
                            ,'SET_NAME'
                            ,'PRODUCT_NAME'
                            ,'CATEGORY'
                            ,'SUBTYPE'
                            ,'PRODUCT_RELEASE_DATE'
                            ,'PRODUCT_CARD_COUNT'
                            ,'PRODUCT_UUID'
                            ,'PRODUCT_LANGUAGE'
                            ,'CONTENTS_NAME'
                            ,'CONTENTS_TYPE'
                            ,'CONTENTS_CODE'
                            ,'CONTENTS_COUNT'
                            ,'CONTENTS_UUID'
                            ,'CONTENTS_CARD_NUMBER'
                            ,'PURCHASE_URL_CARD_KINGDOM'
                            ,'PURCHASE_URL_TCG_PLAYER'
                            ,'ABU_GAMES_ID'
                            ,'CARD_KINGDOM_ID'
                            ,'CARD_MARKET_ID'
                            ,'CARD_TRADER_ID'
                            ,'COOL_STUFF_INC_ID'
                            ,'MINIATURE_MARKET_ID'
                            ,'MVP_GAMES_ID'
                            ,'STAR_CITY_GAMES_ID'
                            ,'TCG_PLAYER_ID'
                            ,'TOAD_AND_TROLL_ID']