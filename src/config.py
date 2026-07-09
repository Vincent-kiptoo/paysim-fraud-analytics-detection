"""
Configuration module for the paysim data pipeline.

This module centralizes database credentials and connection settings.
It loads environment variables from .env file and provides a configured
database engine for other modules to use.
"""

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database credentials
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'fraud_analysis')
DB_PORT = os.getenv('DB_PORT', '3306')

# Create engine
engine = create_engine(
    f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)