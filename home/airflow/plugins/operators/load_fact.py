from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):
    
    
    """This function is used to Load data into fact table from staging tables.
    
    Parameters:
    redshift_conn_id: Connection Id of the Airflow to redshift database
    table: destination fact table to store the fact data
    sql_statement: The statement which enables us to fill the data from staging tables
    
    Returns: None
    """

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 table="",
                 sql_statement="",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.table= table
        self.redshift_conn_id= redshift_conn_id
        self.sql_statement= sql_statement
    def execute(self, context):
        self.log.info('LoadFactOperator implementation to be started')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        insert_query = 'INSERT INTO {} ({})'.format(self.table, self.sql_statement)
        redshift.run(insert_query)
