import yaml
from sqlalchemy import create_engine
import psycopg2
import pandas as pd


with open('credentials.yaml', 'r') as cred_file:
    db_connector = yaml.safe_load(cred_file)
class RDSDatabaseConnector:
    def __init__(self, db_connector):
        self.db_connector = db_connector
        #print(self.db_connector['RDS_HOST'])
    
    def init_engine(self):
        #self.db_connector
        #DATABASE_TYPE = 'postgresql'
        #DBAPI = 'psycopg2'
        engine = create_engine(f"postgresql://{self.db_connector['RDS_USER']}:{self.db_connector['RDS_PASSWORD']}@{self.db_connector['RDS_HOST']}:{self.db_connector['RDS_PORT']}/{self.db_connector['RDS_DATABASE']}")
        #engine.execution_options(isolation_level='AUTOCOMMIT').connect()

        #return engine
        return engine.execution_options(isolation_level='AUTOCOMMIT').connect()
    
    def extract_data(self):
        self.conn = self.init_engine()
        
        #self.conn = psycopg2.connect(   #figure out how to use init_engine here
            #host=self.db_connector['RDS_HOST'],
            #port=self.db_connector['RDS_PORT'],
            #database=self.db_connector['RDS_DATABASE'],
            #user=self.db_connector['RDS_USER'],
            #password=self.db_connector['RDS_PASSWORD']
        #)
        cursor = self.conn.cursor()

        select_query = "SELECT * FROM loan_payments"

        cursor.execute(select_query)
        rows = cursor.fetchall()

        self.column_names = self.conn.execute(select_query)
        print(self.column_names)

        #for row in rows:
            #print(row)

        cursor.close()
        self.conn.close()
    
    def to_df(self):
        #pass
        loan_data = self.extract_data()
        loan_data

        #loan_df = pd.DataFrame(loan_data, columns)
        

rds_database_connector = RDSDatabaseConnector(db_connector)
engine_initialised = rds_database_connector.init_engine()
rds_database_connector.extract_data()
#print(engine_initialised)
#print(db_connector)