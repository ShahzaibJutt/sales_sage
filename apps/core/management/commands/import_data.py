import json
import logging
import sqlite3
from pathlib import Path

import pandas as pd
from decouple import config
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Import data from a CSV or JSON file into an SQLite database using paths defined in environment variables.'

    def handle(self, *args, **options):
        logger = logging.getLogger('sales_sage')

        data_file_path = config('DATA_FILE_PATH')
        db_url = config('DATABASE_URL')

        if not Path(data_file_path).exists():
            logger.error(f"Data file {data_file_path} does not exist")
            raise CommandError(f"Data file {data_file_path} does not exist")

        try:
            conn = sqlite3.connect(db_url)
            logger.info('Successfully connected to the database.')
        except Exception as e:
            logger.error(f"Failed to connect to the database: {e}")
            raise

        try:
            if data_file_path.endswith('.csv'):
                df = pd.read_csv(data_file_path)
                df.to_sql('SalesData', conn, if_exists='replace', index=False)
                logger.info('CSV data successfully loaded into the database.')
            elif data_file_path.endswith('.json'):
                with open(data_file_path, 'r') as file:
                    data = json.load(file)
                    df = pd.DataFrame(data)
                    df.to_sql('SalesData', conn, if_exists='replace', index=False)
                logger.info('JSON data successfully loaded into the database.')
            else:
                logger.error('Unsupported file type. Please provide a .csv or .json file.')
                raise CommandError('Unsupported file type. Please provide a .csv or .json file.')
        except Exception as e:
            logger.error(f"Error during file processing: {e}")
            raise
        finally:
            conn.close()
            logger.info('Database connection closed.')
