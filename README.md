# MTG Analysis and Modelling

A unified pipeline for working with Magic: The Gathering data.  
This project downloads JSON data from [MTGJSON](https://mtgjson.com) (and potentially [Scryfall](https://scryfall.com) in the future), processes the files into structured tables, and enables analysis and machine learning on MTG card data.


## Features

- 📥 **Data ingestion**: Download and manage raw JSON files (e.g. AllPrintings, SetList).
- 🔄 **Processing & transformation**: Normalize nested JSON into pandas DataFrames or SQL tables.
- 🗄️ **Database integration**: Store and query structured MTG data with SQL.
- 📊 **Analysis**: Explore trends, card attributes, and relationships across sets.
- 🤖 **Machine learning**: Build and evaluate models using MTG card data (e.g., price forecasting, rarity classification).


## Project Structure
mtg-data-pipeline/
<br>│
<br>├── data/      --> Local or Kaggle datasets (raw + processed)
<br>├── notebooks/ --> Jupyter notebooks for exploration and analysis
<br>├── scripts/   --> Python scripts for ETL (download, transform, load)
<br>├── sql/       --> SQL queries and schema definitions
<br>├── models/    --> Machine learning experiments
<br>└── README.md  --> Project documentation


## Getting Started

### Prerequests

- Python 3.10+
- pandas
- SQLAlchemy
- requests
- lzma (for .xz decompression)

### Downloading Data

Download data from MTGJSON and/or Scryfall directly, for example:
- mtgjson_url = "https://mtgjson.com/api/v5/AllPrintings.json.xz"

### Processing Data

1. Flatten and normalise JSON data into Pandas dataframes.
2. Store processed data in SQL database

### Analysis and Machine Learning

!! TDB !!
- Exploratory data analysis
- Feature Engineering
- Machine Learning modelling
