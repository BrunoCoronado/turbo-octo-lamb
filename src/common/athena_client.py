import os
import boto3
import time

# Instanciación a nivel de módulo para reutilizar la conexión HTTP entre invocaciones de la Lambda
_ATHENA_CLIENT = boto3.client('athena')

class AthenaService:
    def __init__(self, client = None, database_name: str = None, output_location: str = None):
        self.client = client or _ATHENA_CLIENT
        print(os.environ)
        self.database_name = database_name or os.environ.get('ATHENA_DATABASE_NAME')
        self.output_location = output_location or os.environ.get('ATHENA_OUTPUT_LOCATION')
        
    def execute_query(self, query: str) -> str:
        """Inicia la consulta SQL en Athena."""
        response = self.client.start_query_execution(
                QueryString=query,
                QueryExecutionContext={'Database': self.database_name},
                ResultConfiguration={'OutputLocation': self.output_location}
        )
        return response['QueryExecutionId']
    
    def poll_status(self, execution_id: str, poll_interval: float = 0.5) -> bool:
        """Espera de forma síncrona a que la consulta finalice."""
        while True:
            response = self.client.get_query_execution(QueryExecutionId=execution_id)
            state = response['QueryExecution']['Status']['State']
            
            if state == 'SUCCEEDED':
                return True
            elif state in ['FAILED', 'CANCELLED']:
                reason = response['QueryExecution']['Status'].get('StateChangeReason', 'Error desconocido')
                raise RuntimeError(f"Consulta de Athena fallida [{state}]: {reason}")
            
            time.sleep(poll_interval)
            
    def fetch_results(self, execution_id: str) -> list:
        """Pagina y mapea los resultados tabulares a una lista de diccionarios Python."""
        paginator = self.client.get_paginator('get_query_results')
        page_iterator = paginator.paginate(QueryExecutionId=execution_id)
        
        parsed_data = []
        headers = []
        
        for page in page_iterator:
            rows = page['ResultSet']['Rows']
            
            if not headers and rows:
                headers = [col.get('VarCharValue', '') for col in rows[0]['Data']]
                rows = rows[1:]  # Omitir fila de encabezados
                
            for row in rows:
                row_data = [col.get('VarCharValue', None) for col in row['Data']]
                parsed_data.append(dict(zip(headers, row_data)))
                
        return parsed_data
    
    def run(self, query: str) -> list:
        """Método orquestador para ejecutar, esperar y parsear."""
        execution_id = self.execute_query(query)
        self.poll_status(execution_id)
        return self.fetch_results(execution_id)