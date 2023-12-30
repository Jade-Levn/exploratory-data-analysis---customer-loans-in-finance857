from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import text
import yaml
import psycopg2
import pandas as pd


with open('credentials.yaml', 'r') as cred_file:
    db_connector = yaml.safe_load(cred_file)
class RDSDatabaseConnector:
    def __init__(self, db_connector):
        self.db_connector = db_connector
    
    def init_engine(self):
        engine = create_engine(f"postgresql://{self.db_connector['RDS_USER']}:{self.db_connector['RDS_PASSWORD']}@{self.db_connector['RDS_HOST']}:{self.db_connector['RDS_PORT']}/{self.db_connector['RDS_DATABASE']}")
        return engine
    
    def extract_data(self):
        db_engine = self.init_engine()
        db_engine.execution_options(isolation_level='AUTOCOMMIT').connect()

        sql_query = '''SELECT * FROM loan_payments'''

        self.loan_df = pd.read_sql_query(sql_query, con=db_engine)
            
    
    def df_to_csv(self):
        self.loan_df.to_csv("loans.csv")


rds_database_connector = RDSDatabaseConnector(db_connector)
rds_database_connector.extract_data()
rds_database_connector.df_to_csv()