###################################################################################################
# -------------------------------------- PYTHON LIBRARIES --------------------------------------- #
###################################################################################################

# Data libraries
import pandas     as     pd

# PostGreSQL communication libraries
from   sqlalchemy                     import MetaData, Table, Column, Text, Date
from   sqlalchemy.dialects.postgresql import insert



###################################################################################################
# ------------------------------------------ FUNCTIONS ------------------------------------------ #
###################################################################################################

# Function for showing the data and version of the MTGJSON data
def data_recency_check(data, json_type):

    """
    Extract and display the version and date metadata from an MTGJSON dataset,
    and return this information as a DataFrame along with the JSON type.

    Parameters
    ----------
    data : dict
        MTGJSON data loaded from a JSON file, expected to contain a 'meta' key
        with 'date' and 'version' fields.

    json_type : str
        A string indicating the type or name of the JSON dataset being processed.
        This will be included in the output DataFrame.

    Returns
    -------
    pd.DataFrame
        A DataFrame with a single row and columns:
        - 'json_type': The provided JSON dataset type/name.
        - 'latest_date': The date the MTGJSON data was last updated.
        - 'latest_version': The MTGJSON model version.
    """

    # Create a DataFrame for the output
    df = pd.DataFrame({'json_type'      : [json_type]
                      ,'latest_date'    : [data['meta']['date']]
                      ,'latest_version' : [data['meta']['version']]})

    # Returning the values directly
    return(df)



# Function for uploading the recency check

def recency_check_upload(schema_name, table_name, dataframe, engine):
    
    """
    Uploads recency check data from a Pandas DataFrame into a PostgreSQL table 
    with upsert (insert or update) logic.

    Each row from the DataFrame is inserted into the target table. If a row with the 
    same `json_type` (primary key) already exists, the corresponding `latest_date` 
    and `latest_version` values are updated instead.

    Parameters
    ----------
    schema_name : str
        Name of the PostgreSQL schema where the table resides.
    table_name : str
        Name of the PostgreSQL table to update or insert into.
    dataframe : pandas.DataFrame
        DataFrame containing the recency check data with columns:
        - 'json_type' (str): Identifier for the JSON file type.
        - 'latest_date' (datetime.date): Date of the latest file.
        - 'latest_version' (str): Version string of the latest file.

    Notes
    -----
    - Requires a global SQLAlchemy `engine` object to be defined.
    - Uses PostgreSQL's ON CONFLICT clause for upsert behavior.
    """

    # Create a MetaData object
    metadata = MetaData(schema=schema_name)
    
    # Define the Table object matching your PostgreSQL table
    json_recency_table = Table(table_name
                              ,metadata
                              ,Column('json_type' ,Text ,primary_key = True)
                              ,Column('latest_date' ,Date)
                              ,Column('latest_version' ,Text))
    
    # Upsert each row from your DataFrame
    with engine.begin() as conn:
        
        # Iterate through rows of the DataFrame
        for _, row in dataframe.iterrows():
            
            # Create an insert statement for the current row
            stmt = insert(json_recency_table).values(json_type      = row['json_type']
                                                    ,latest_date    = row['latest_date']
                                                    ,latest_version = row['latest_version'])
            
            # Add upsert logic to update on conflict
            stmt = stmt.on_conflict_do_update(index_elements = ['json_type']
                                             ,set_           = {'latest_date'    : row['latest_date']
                                                               ,'latest_version' : row['latest_version']})
            
            # Execute the statement
            conn.execute(stmt)