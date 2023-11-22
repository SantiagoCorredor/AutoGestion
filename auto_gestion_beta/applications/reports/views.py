from django.shortcuts import render
from google.cloud import bigquery
import pandas as pd
import json
import re
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import pandas as pd
from google.cloud import bigquery

def consultar_datos(request):
    # Conectarse a BigQuery y obtener los datos
    client = bigquery.Client()
    query = "SELECT * FROM `driven-atrium-400420.sod_co_bi_reportsmanagement_dev.CLIENTES_DIM` limit 1000"
    query_job = client.query(query)
    results = query_job.result()

    # Convertir los resultados a un DataFrame de Pandas
    data = pd.DataFrame([dict(row.items()) for row in results])

    # Almacenar el DataFrame en la sesión para su posterior uso
    request.session['data'] = data.to_json(orient='records')

    # Renderizar la plantilla con los datos en formato JSON
    return render(request, 'consulta.html', {'data_json': data.to_json(orient='records')})

def aplicar_filtro(request):
    # Obtener el DataFrame desde la sesión
    data = pd.read_json(request.session['data'], orient='records')

    # Aplicar filtros u operaciones en el DataFrame
    # Por ejemplo, si se envía un filtro de nombre "filtro_columna" con valor "valor_filtro"
    if 'filtro_columna' in request.GET:
        valor_filtro = request.GET['filtro_columna']
        data = data[data['columna'] == valor_filtro]

    # Renderizar la plantilla con los datos filtrados
    return render(request, 'consulta.html', {'data': data})
