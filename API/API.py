import pandas as pd
from sodapy import Socrata

API = "www.datos.gov.co"
API_TOKEN = "gt2j-8ykr"

def Get_data (limite_registros , nombre_departamento ):
    client = Socrata(API, None)
    results = client.get(API_TOKEN, limit=limite_registros, departamento_nom=nombre_departamento )
    results_df = pd.DataFrame.from_records(results)
    return results_df


