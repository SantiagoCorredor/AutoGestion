from django.shortcuts import render
from google.cloud import bigquery
import pandas as pd
import json
import re
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from .RegexBasic import RegexBasic
from datetime import datetime
from unipath import Path
from google.cloud import storage
import os
from .forms import *
from django.shortcuts import render, redirect

 

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



##Adaptar al código (Sin adaptar)
class SingleInformation():
    def __init__(self,js):
        super().__init__()
        self.campaign_id = js["identificacion"]
        self.campaign_date = js["identificacion_corp"]
        
    def retrieve_campaign(self):
        client = bigquery.Client()
        query = f"""
        SELECT * FROM `driven-atrium-400420.sod_co_bi_reportsmanagement_dev.CLIENTES_DIM`
        """
        response = client.query(query)
        response.result()
        response = response.to_dataframe()  
        return response["nombre"][0]
    
### Adaptar al código (Sin adaptar. )    
class Procedimientos:
    def __init__(self, js):
        # Ajusta el nombre del atributo js a minúsculas para que coincida con las columnas de BigQuery
        self.Identificacion = js.get("Identificacion", None)
        self.Identificacion_corp = js.get("Identificacion_corp", None)
        self.Tipo_doc = js.get("Tipo_doc", None)
        self.NOMBRES = js.get("NOMBRES", None)
        self.APELLIDOS = js.get("APELLIDOS", None)
        self.DIRECCION = js.get("DIRECCION", None)
        self.CIUDAD = js.get("CIUDAD", None)
        self.ESPECIALIDAD = js.get("ESPECIALIDAD", None)
        self.CONTACTABLE_SODIMAC = js.get("CONTACTABLE_SODIMAC", None)
        self.CONTACTABLE_TERCERO = js.get("CONTACTABLE_TERCERO", None)
        self.CANAL_OPTIN = js.get("CANAL_OPTIN", None)
        self.FECHA_AUTORIZACION = js.get("FECHA_AUTORIZACION", None)
        self.PERIODO_SEGMENTACION = js.get("periodo_segmentacion", None)
        self.PERFIL_SEGMENTACION = js.get("perfil_segmentacion", None)
        self.SEGMENTO_NECESIDAD = js.get("segmento_necesidad", None)
        self.SEGMENTO_VALOR = js.get("segmento_valor", None)
        self.CICLO_VIDA = js.get("ciclo_vida", None)
        self.TIENDA_FRECUENTE = js.get("tienda_frecuente", None)
        self.FAMILIA_MAYOR_FRECUENCIA = js.get("familia_mayor_frecuencia", None)
        self.TIPO_SEGMENTO = js.get("tipo_segmento", None)
        self.PIRAMIDE = js.get("piramide", None)
        self.GENERO = js.get("genero", None)
        self.FECHA_NACIMIENTO = js.get("fecha_nacimiento", None)
        self.ESTADO_CES = js.get("estado_ces", None)
        self.PROFESION = js.get("profesion", None)
        self.SEGMENTO_CES = js.get("segmento_ces", None)
        self.FECHA_NIVEL = js.get("fecha_nivel", None)
        self.FECHA_INICIAL_CES = js.get("fecha_inicial_ces", None)
        self.FECHA_FIN_CES = js.get("fecha_fin_ces", None)
        self.CREATED_AT = js.get("created_at", None)
        self.FECHA_INSCRIPCION_CMR = js.get("fecha_inscripcion_cmr", None)
        self.TOTPUNTO = js.get("totpunto", None)
        self.RANGO_PUNTOS = js.get("rango_puntos", None)
        self.PUNTOS_REDIMIDOS_12M = js.get("puntos_redimidos_12m", None)
        self.MARCA_TDC = js.get("marca_tdc", None)
        self.MARCA_TDB = js.get("marca_tdb", None)
        self.CLIENTE_ACTIVO = js.get("cliente_activo", None)
        self.FECHA_ULTIMA_COMPRA = js.get("fecha_ultima_compra", None)
        self.CANAL_VD_ULTIMA_COMPRA = js.get("canal_vd_ultima_compra", None)
        self.TIENDA_DESPACHA_ULTIMA_COMPRA = js.get("tienda_despacha_ultima_compra", None)
        self.MEDIO_PAGO_ULTIMA_COMPRA = js.get("medio_pago_ultima_compra", None)
        self.FLAG_CMR_PUNTOS = js.get("flag_cmr_puntos", None)
        self.FLAG_BANCO = js.get("flag_banco", None)
        self.FLAG_CEC = js.get("flag_cec", None)
        self.FLAG_CLIENTE360 = js.get("flag_cliente360", None)
        self.FLAG_SEGMENTADOS = js.get("flag_segmentados", None)
        self.FLAG_COMPRADORES_ACTIVOS = js.get("flag_compradores_activos", None)
        self.FLAG_COMPRADORES_MES_CORTE = js.get("flag_compradores_mes_corte", None)
        self.FLAG_COMPRADORES_ACUMULADOS = js.get("flag_compradores_acumulados", None)
        self.FLAG_LOYALTY = js.get("flag_loyalty", None)

    def _generar_clausulas_where(self, **campos):
        return [f"{campo} = '{valor}'" for campo, valor in campos.items() if valor is not None and valor not in ('', '*')]

    def _generar_clausulas_select(self, selected_columns):
    # Ajusta los nombres y añade más campos según sea necesario
        select_clauses = [column for column in selected_columns if column != "Seleccionar Todas"]

        return select_clauses
        
    def generar_consulta_BigQuery(self, selected_columns):
        select_clause = ", ".join(self._generar_clausulas_select(selected_columns))
        where_clauses = self._generar_clausulas_where(
            Identificacion=self.Identificacion,
            Identificacion_corp=self.Identificacion_corp,
            Tipo_doc=self.Tipo_doc,
            NOMBRES=self.NOMBRES,
            APELLIDOS=self.APELLIDOS,
            DIRECCION=self.DIRECCION,
            CIUDAD=self.CIUDAD,
            ESPECIALIDAD=self.ESPECIALIDAD,
            CONTACTABLE_SODIMAC=self.CONTACTABLE_SODIMAC,
            CONTACTABLE_TERCERO=self.CONTACTABLE_TERCERO,
            CANAL_OPTIN=self.CANAL_OPTIN,
            FECHA_AUTORIZACION=self.FECHA_AUTORIZACION,
            PERIODO_SEGMENTACION=self.PERIODO_SEGMENTACION,
            PERFIL_SEGMENTACION=self.PERFIL_SEGMENTACION,
            SEGMENTO_NECESIDAD=self.SEGMENTO_NECESIDAD,
            SEGMENTO_VALOR=self.SEGMENTO_VALOR,
            CICLO_VIDA=self.CICLO_VIDA,
            TIENDA_FRECUENTE=self.TIENDA_FRECUENTE,
            FAMILIA_MAYOR_FRECUENCIA=self.FAMILIA_MAYOR_FRECUENCIA,
            TIPO_SEGMENTO=self.TIPO_SEGMENTO,
            PIRAMIDE=self.PIRAMIDE,
            GENERO=self.GENERO,
            FECHA_NACIMIENTO=self.FECHA_NACIMIENTO,
            ESTADO_CES=self.ESTADO_CES,
            PROFESION=self.PROFESION,
            SEGMENTO_CES=self.SEGMENTO_CES,
            FECHA_NIVEL=self.FECHA_NIVEL,
            FECHA_INICIAL_CES=self.FECHA_INICIAL_CES,
            FECHA_FIN_CES=self.FECHA_FIN_CES,
            CREATED_AT=self.CREATED_AT,
            FECHA_INSCRIPCION_CMR=self.FECHA_INSCRIPCION_CMR,
            TOTPUNTO=self.TOTPUNTO,
            RANGO_PUNTOS=self.RANGO_PUNTOS,
            PUNTOS_REDIMIDOS_12M=self.PUNTOS_REDIMIDOS_12M,
            MARCA_TDC=self.MARCA_TDC,
            MARCA_TDB=self.MARCA_TDB,
            CLIENTE_ACTIVO=self.CLIENTE_ACTIVO,
            FECHA_ULTIMA_COMPRA=self.FECHA_ULTIMA_COMPRA,
            CANAL_VD_ULTIMA_COMPRA=self.CANAL_VD_ULTIMA_COMPRA,
            TIENDA_DESPACHA_ULTIMA_COMPRA=self.TIENDA_DESPACHA_ULTIMA_COMPRA,
            MEDIO_PAGO_ULTIMA_COMPRA=self.MEDIO_PAGO_ULTIMA_COMPRA,
            FLAG_CMR_PUNTOS=self.FLAG_CMR_PUNTOS,
            FLAG_BANCO=self.FLAG_BANCO,
            FLAG_CEC=self.FLAG_CEC,
            FLAG_CLIENTE360=self.FLAG_CLIENTE360,
            FLAG_SEGMENTADOS=self.FLAG_SEGMENTADOS,
            FLAG_COMPRADORES_ACTIVOS=self.FLAG_COMPRADORES_ACTIVOS,
            FLAG_COMPRADORES_MES_CORTE=self.FLAG_COMPRADORES_MES_CORTE,
            FLAG_COMPRADORES_ACUMULADOS=self.FLAG_COMPRADORES_ACUMULADOS,
            FLAG_LOYALTY=self.FLAG_LOYALTY,
        )# Construye la consulta SQL
        query = f"SELECT {select_clause} FROM `driven-atrium-400420.sod_co_bi_reportsmanagement_dev.CLIENTES_DIM`"

        # Añade las cláusulas WHERE si existen
        if where_clauses:
            query += " WHERE " + " AND ".join(where_clauses)

        #try:
        #    # Ejecuta la consulta en BigQuery
        #    client = bigquery.Client()
        #    query_job = client.query(query)

            # Obtiene los resultados
        #    results = query_job.result()

            # Retorna los resultados (o ajusta según sea necesario)
        #    return HttpResponse(f"Query ejecutada correctamente. Resultados: {results}")
        #except Exception as e:
            # Maneja cualquier error y retorna una respuesta adecuada
        #    return HttpResponse(f"Error al ejecutar la consulta: {str(e)}")
        return query
    
    
def columnas_view(request):
    request.session.clear()
    selected_columns = request.session.get('selected_columns', [])
    if request.method == 'POST':
        form = FiltrosForm(request.POST, selected_columns=selected_columns)
        if form.is_valid():
            # Obtén los datos del formulario
            data = form.cleaned_data
            print(data)
            # Ajusta la lógica según tus necesidades
            selected_columns = data.pop('columnas_seleccionadas', [])
            print(selected_columns)

            # Ajusta la lógica según tus necesidades
            procedimientos = Procedimientos(data)
            
            # Pasa las columnas seleccionadas al método generar_consulta_BigQuery
            query = procedimientos.generar_consulta_BigQuery(selected_columns)
            # Puedes hacer algo con la consulta, por ejemplo, imprimirla en la consola
            print(query)

            # Aquí puedes redirigir a una nueva página con los resultados o hacer lo que necesites
            # return render(request, 'resultados.html', {'query': query, 'data': data})
    else:
        form = FiltrosForm(selected_columns=selected_columns)

    return render(request, 'filtros.html', {'form': form})


## ESTO ES SÓLO VALIDO PARA GOOGLECLOUD, HAY QUE HACER PRUEBAS CON EL BUCKET LOCAL 


## Diseño: 
def filtro_view(request):
    # Obtiene las columnas seleccionadas de la sesión
    selected_columns = request.session.get('selected_columns', [])

    if request.method == 'POST':
        # Crea una instancia del formulario y pásale las columnas seleccionadas
        form = FiltrosForm(request.POST, selected_columns=selected_columns)

        if form.is_valid():
            # Realiza las acciones deseadas con los datos del formulario
            data = form.cleaned_data
            procedimientos = Procedimientos(data)
            query = procedimientos.generar_consulta()
            print(query)
            # Después de realizar la acción deseada, limpiar la sesión
            request.session.clear()
            # Redirige o renderiza según sea necesario
            # return render(request, 'resultados.html', {'query': query, 'data': data})

    else:
        # Si no es una solicitud POST, crea el formulario con las columnas seleccionadas
        form = FiltrosForm(selected_columns=selected_columns)

    return render(request, 'filtros.html', {'form': form})


def consulta_view(request):
    form = FiltrosForm()
    print(form)
    if request.method == 'POST':
        print("ok")
        return JsonResponse({'message': 'Datos POST recibidos correctamente'})
    else:
        form = FiltrosForm()
        print("se cargó la página       ")
        return render(request, 'filtros.html', {'form': form})



class UpdateBucket(Procedimientos):

    def Update_Json(self):
        client_storage = storage.Client(project="sod-co-bi-sandbox")
        self.bucket1 = client_storage.get_bucket(self.bucket1)
        norm = RegexBasic()
        self.fecha_envio = self.fecha_envio.replace("-","")
        self.name_camp = norm.Normalize(self.name_camp)
        x = datetime.now()
        x= x.strftime("%Y%m%d")
        nombre_archivocsv = self.fecha_envio + "_" + self.name_camp + "-" + x +".csv"
        print(f"Nombre Archivo: {nombre_archivocsv}")

        if self.canal == "EMAIL":
            blob = self.bucket1.blob("cfg_sp_one_shot_audiencia_sod_sku_test.json")
            json_string = blob.download_as_text()
            json_data = json.loads(json_string)
            _Canal = "Email"
            _Campo = "email"
            for index in json_data:    
                if index == "SrcDataSetId":
                    json_data[index] = "test_camp_os_app"
                if index == "LdgSftpAccount":
                    if self.marca == "HC":
                        json_data[index] = "6235045"    
                    else:
                        json_data[index] = "6235046"
                if index == "LdgYamlDecryptCol":
                    json_data[index] = ["Cedula",""+_Canal+""]            
                    #json_data[index] = ["Cedula"]
                if index == "LdgSendableAtt":
                    json_data[index] = ""+_Canal+""            
                if index == "LdgMailAlerts":
                    json_data[index] = self.Email
                if index == "LdgFileNamesCsv":
                    json_data[index] = [self.fecha_envio + "_" + self.name_camp ]
                if index == "LdgFileNamesYml":
                    json_data[index] = [self.fecha_envio + "_" + self.name_camp ]
                if index == "SrcBQueryBase":
                    if self.Camp == "None":
                        json_data[index] = "SELECT tt1.no_cedula as Cedula, tt1."+_Campo+" as "+_Canal+" FROM `{0}.{1}.{2}` tt1 WHERE tt1.PARTITIONTIME = TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(),DAY) AND flag_grupocontrol = 'GT:GRUPOTRATAMIENTO';"    
                    else:
                        camp_name = norm.Normalize(self.Camp)
                        camp_value = norm.Normalize(self.CampValue)
                        json_data[index] = "SELECT tt1.no_cedula as Cedula, tt1."+_Campo+" as "+_Canal+", '"+camp_value+"' "+camp_name +" FROM `{0}.{1}.{2}` tt1 WHERE tt1.PARTITIONTIME = TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(),DAY) AND flag_grupocontrol = 'GT:GRUPOTRATAMIENTO';"  

            modified_json_string = json.dumps(json_data)
            blob.upload_from_string(modified_json_string)     
        else:
            blob = self.bucket1.blob("cfg_sp_one_shot_sms_audiencia_test.json")
            json_string = blob.download_as_text()
            json_data = json.loads(json_string)
            for index in json_data:
                if index == "LdgFileNamesCsv":
                    json_data[index] = [self.fecha_envio + "_" + self.name_camp]
                if index == "LdgFileNamesYml":
                    json_data[index] = [self.fecha_envio + "_" + self.name_camp]

            modified_json_string = json.dumps(json_data)
            blob.upload_from_string(modified_json_string)
