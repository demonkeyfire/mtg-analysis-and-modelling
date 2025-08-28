# MTG Analysis Database

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
│
├── data/ # Local or Kaggle datasets (raw + processed)
├── notebooks/ # Jupyter notebooks for exploration and analysis
├── scripts/ # Python scripts for ETL (download, transform, load)
├── sql/ # SQL queries and schema definitions
├── models/ # Machine learning experiments
└── README.md # Project documentation
