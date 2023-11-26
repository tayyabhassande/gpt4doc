import os
from chromadb.config import Settings

CHROMA_SETTINGS= Settings(
    chroma_db_impl='duckdb+parquet',
    persist_directory='db',
    anonymized_telemetry='False'

)



# Define the Chroma settings
CHROMA_SETTINGS = Settings(
        persist_directory='db',
        anonymized_telemetry=False
)