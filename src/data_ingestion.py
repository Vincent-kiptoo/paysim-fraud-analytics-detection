"""
Data ingestion module for the PaySim pipeline.

Handles MySQL database connections and query execution.
Provides utilities for loading the PaySim dataset into pandas DataFrames.
"""

import pandas as pd
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from src.config import engine
from src.logging_config import get_logger

logger = get_logger(__name__)


def test_connection() -> None:
    """
    Test the database connection.
    """
    logger.info("Testing database connection...")

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        logger.info("Database connection successful.")

    except SQLAlchemyError as e:
        logger.error(f"Database connection failed: {e}")
        raise


def load_paysim(limit: int | None = None) -> pd.DataFrame:
    """
    Load the PaySim dataset from the MySQL database.
    
    Args:
        limit: Optional number of rows to load.
    
    Returns:
        A pandas DataFrame containing the queried data.
    """
    logger.info("Loading PaySim dataset from MySQL...")
    
    query = "SELECT * FROM paysim"
    if limit is not None:
        query += f" LIMIT {limit}"
    
    try:
        # Load in chunks to prevent memory crash
        chunk_size = 100000
        chunks = []
        
        for chunk in pd.read_sql(query, engine, chunksize=chunk_size):
            chunks.append(chunk)
            logger.info(f"Loaded {len(chunks) * chunk_size:,} rows so far...")
        
        paysim = pd.concat(chunks, ignore_index=True)
        
        logger.info(f"Loaded {len(paysim):,} rows successfully.")
        return paysim
        
    except SQLAlchemyError as e:
        logger.error(f"Failed to load PaySim dataset: {e}")
        raise


if __name__ == "__main__":
    test_connection()
    df = load_paysim()
    print(df.head())