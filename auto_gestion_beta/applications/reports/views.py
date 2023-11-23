from django.shortcuts import render
from google.cloud import bigquery
import pandas as pd
import json
import re
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def consultar_datos(request, tabla):
    # Crea un cliente de BigQuery
    client = bigquery.Client()

    # Construye la consulta utilizando el nombre de la tabla especificado en la URL
    query = f"SELECT * FROM `driven-atrium-400420.sod_co_bi_reportsmanagement_dev.{tabla}`"

    # Ejecuta la consulta en BigQuery
    query_job = client.query(query)

    # Recupera los resultados
    results = query_job.result()

    # Obtener los nombres de las columnas desde el esquema de BigQuery
    column_names = [field.name for field in results.schema]

    # Convierte los resultados en un DataFrame
    data = [list(row.values()) for row in results]
    df = pd.DataFrame(data, columns=column_names)
    # Definir las palabras clave para buscar en los nombres de las columnas
    palabras_clave = ['VENTA', 'FACTURA', 'TICKET']  # Puedes agregar otras palabras clave

    # Aplicar el formato de dinero a columnas que contengan las palabras clave
    #for palabra in palabras_clave:
    #    patron = re.compile(f'.*{palabra}.*', re.IGNORECASE)
    #   columnas_coincidentes = [col for col in df.columns if patron.match(col)]
    #    for col in columnas_coincidentes:
    #        df[col] = df[col].map('${:,.2f}'.format)

    # Asegúrate de que las fechas estén formateadas correctamente como objetos de fecha
    df['fecha'] = pd.to_datetime(df['fecha'])

    # Convierte las fechas a cadenas de texto
    df['fecha'] = df['fecha'].dt.strftime('%Y-%m-%d %H:%M:%S')
    print(df.dtypes)
    # Convierte el DataFrame a una lista de diccionarios
    data_json = df.to_dict(orient='records')

    # Guarda los datos en un archivo JSON (opcional)
    with open('datos.json', 'w') as json_file:
        json.dump(data_json, json_file)

    return render(request, 'consulta.html', {'data': data_json})


def obtener_info_dataframe():
    """
    Función auxiliar para obtener información sobre el DataFrame.
    Puedes extender esta función según tus necesidades.
    """
    info_dataframe = []

    with open('datos.json', 'r') as json_file:
        data_json = json.load(json_file)

    # Convertir las fechas de texto a objetos de fecha
    for row in data_json:
        row['fecha'] = pd.to_datetime(row['fecha'], format='%Y-%m-%d %H:%M:%S')

    # Crear un nuevo DataFrame con las fechas convertidas
    df = pd.DataFrame(data_json)

    for col, dtype in df.dtypes.iteritems():
        columna_info = {'nombre': col, 'tipo': str(dtype)}

        # Identifica el tipo de filtro según el tipo de datos
        if dtype == 'float64' or dtype == 'int64':
            # Filtro de rango para tipos numéricos
            columna_info['filtro'] = 'rango'
            columna_info['rango'] = {'min': df[col].min(), 'max': df[col].max()}
        elif dtype == 'datetime64[ns]':
            # Filtro de rango para fechas
            columna_info['filtro'] = 'rango_fechas'
            columna_info['rango_fechas'] = {'min': df[col].min(), 'max': df[col].max()}
        elif dtype == 'object' and len(df[col].unique()) <= 5:
            # Filtro de valores exactos para columnas categóricas con 5 o menos opciones
            columna_info['filtro'] = 'valores_exactos'
            columna_info['valores'] = df[col].unique()
        else:
            # No se aplicarán filtros para otros tipos de datos
            columna_info['filtro'] = None

        info_dataframe.append(columna_info)

    return info_dataframe

def filtrar_datos(request):
    # Obtén el DataFrame desde el archivo JSON o donde lo tengas almacenado
    with open('datos.json', 'r') as json_file:
        data_json = json.load(json_file)

    # Convertir las fechas de texto a objetos de fecha
    for row in data_json:
        row['fecha'] = pd.to_datetime(row['fecha'], format='%Y-%m-%d %H:%M:%S')
    # Crear un nuevo DataFrame con las fechas convertidas
    df = pd.DataFrame(data_json)
    # Obtén información sobre el DataFrame
    info_dataframe = obtener_info_dataframe(df)

    # Genera los elementos de filtro según la información del DataFrame
    filtros = []
    for col_info in info_dataframe:
        if col_info['filtro'] == 'rango':
            filtro = {'nombre': col_info['nombre'], 'tipo': 'rango'}
            filtros.append(filtro)
        elif col_info['filtro'] == 'valores_exactos':
            filtro = {'nombre': col_info['nombre'], 'tipo': 'valores_exactos', 'valores': col_info['valores']}
            filtros.append(filtro)

    return render(request, 'filtros.html', {'filtros': filtros})


def aplicar_filtros(request):
    if request.method == 'POST':
        # Obtén los filtros enviados desde la página web
        filtros_str = request.POST.get('filtros', '{}')
        filtros = json.loads(filtros_str)

        # Realiza la lógica de filtrado en tu conjunto de datos (df en este caso)
        # Asume que df es tu DataFrame y aplicas los filtros de alguna manera
        # Reemplaza esto con la lógica de filtrado real según tus necesidades
        df_filtrado = filtrar_dataframe(df, filtros)

        # Convierte el DataFrame filtrado a un diccionario para enviarlo como JSON
        data_json = df_filtrado.to_dict(orient='records')

        # Devuelve los datos filtrados como JSON
        return JsonResponse({'data': data_json})
    else:
        # Devuelve un error si la solicitud no es de tipo POST
        return JsonResponse({'error': 'Método no permitido'}, status=405)

# Función de ejemplo para filtrar un DataFrame
def filtrar_dataframe(df, filtros):
    # Asume que 'filtro_columna' es el nombre de la columna y 'rango_min' y 'rango_max' son los valores del rango
    if 'filtro_columna_min' in filtros and 'filtro_columna_max' in filtros:
        df = df[(df['filtro_columna'] >= filtros['filtro_columna_min']) & (df['filtro_columna'] <= filtros['filtro_columna_max'])]
    
    # Asume que 'filtro_columna' es el nombre de la columna y 'valores' son los valores seleccionados
    if 'filtro_columna' in filtros:
        df = df[df['filtro_columna'].isin(filtros['filtro_columna'])]

    return df

#Agregar gráfica.