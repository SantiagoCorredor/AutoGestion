from django import forms
from .models import FormBasic
#from daterangefilter.fields import DateRangeField

class FiltrosForm(forms.ModelForm):
    
    def __init__(self, *args, selected_columns=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Ajusta la lógica para obtener los campos dinámicamente según las columnas seleccionadas
        for column in selected_columns:
            # Puedes ajustar el tipo de campo según tus necesidades
            self.fields[column].required = False
            
            
    #### OPCIONES DE LOS WIDGETS
    TIPO_DOC_CHOICES = [
        ('*',''),
        ('INF', 'INF'),
        ('CE', 'CE'),
        ('NI', 'NI'),
        ('TM', 'TM'),
        ('PAS', 'PAS'),
        ('TI', 'TI'),
        ('EM', 'EM'),
        ('P', 'P'),
        ('CVE', 'CVE'),
        ('CC', 'CC'),
    ]
    
    CIUDAD_CHOICES = [
        ('*', ''),
        ('PELAYO', 'PELAYO'),
        ('PANDI', 'PANDI'),
        ('AGUAS CLARAS', 'AGUAS CLARAS'),
        ('MITU', 'MITU'),
        ('SAANBERNARDO', 'SAANBERNARDO'),
        ('EL GUAMO', 'EL GUAMO'),
        ('PIEDRAS', 'PIEDRAS'),
        ('TENZA', 'TENZA'),
        ('CERRITO', 'CERRITO'),
        ('NATAGAIMA', 'NATAGAIMA'),
        ('LOS PALMITOS', 'LOS PALMITOS'),
        ('ULLOA', 'ULLOA'),
        ('VILLAPINZON', 'VILLAPINZON'),
        ('MANIZALES', 'MANIZALES'),
        ('POPULAR', 'POPULAR'),
        ('PIVIHAY', 'PIVIHAY'),
        ('EL CARMEN DE CHUCURI', 'EL CARMEN DE CHUCURI'),
        ('MARULANDA', 'MARULANDA'),
        ('PALOCAIBLIDO', 'PALOCAIBLIDO'),
        ('SUTAMARCHAN', 'SUTAMARCHAN'),
        ('ACANDI', 'ACANDI'),
        ('SUPIA', 'SUPIA'),
        ('ZERAQUIRA', 'ZERAQUIRA'),
        ('TAME', 'TAME'),
        ('HIERBABUENA', 'HIERBABUENA'),
        ('CAIMITO', 'CAIMITO'),
        ('BARZOLASA', 'BARZOLASA'),
        ('LA MINA CARREJON', 'LA MINA CARREJON'),
        ('QUIPILE', 'QUIPILE'),
        ('LA PRIMAVERA', 'LA PRIMAVERA'),
        ('BETULIA', 'BETULIA'),
        ('PESCA', 'PESCA'),
        ('SABANAGRANDE', 'SABANAGRANDE'),
        ('VEREDANAZARETH', 'VEREDANAZARETH'),
        ('SILOS', 'SILOS'),
        ('PRADERA', 'PRADERA'),
        ('CHINU', 'CHINU'),
        ('TOLEMAIDA', 'TOLEMAIDA'),
        ('POMPEYA', 'POMPEYA'),
        ('CHAMEZA', 'CHAMEZA'),
        ('EL COCUY', 'EL COCUY'),
        ('RUITOQUE', 'RUITOQUE'),
        ('PUERTO SANTANDER', 'PUERTO SANTANDER'),
        ('CUCAITA', 'CUCAITA'),
        ('BELLO', 'BELLO'),
        ('DAIREN', 'DAIREN'),
        ('VIOTA', 'VIOTA'),
        ('PUERTO CARREÑO', 'PUERTO CARREÑO'),
        ('ARMENIA', 'ARMENIA'),
    ]
    
    ESPECIALIDAD_CHOICES = [
        ('*', ''),
        ('PISOS Y PAREDES', 'PISOS Y PAREDES'),
        ('PLOMERIA / HIDRAULICA', 'PLOMERIA / HIDRAULICA'),
        ('INSTALACIONES DE GAS', 'INSTALACIONES DE GAS'),
        ('OBRA NEGRA / CONSTRUCCION', 'OBRA NEGRA / CONSTRUCCION'),
        ('BAÑOS Y COCINAS', 'BAÑOS Y COCINAS'),
        ('ORNAMENTACION / CERRAJERIA', 'ORNAMENTACION / CERRAJERIA'),
        ('IMPERMEABILIZACION', 'IMPERMEABILIZACION'),
        ('COMERCIANTE DE MATERIALES CONSTRUCCION', 'COMERCIANTE DE MATERIALES CONSTRUCCION'),
        ('PINTURAS', 'PINTURAS'),
        ('ELECTRICIDAD / ILUMINACION', 'ELECTRICIDAD / ILUMINACION'),
        ('CARPINTERIA / EBANISTERIA', 'CARPINTERIA / EBANISTERIA'),
        ('DRY WALL', 'DRY WALL'),
        
    ]
    
    BOOLEAN_CHOICES = [
        ('*', ''),
        ('SI', 'SI'),
        ('NO', 'NO'),
    ]
    
    CANAL_OPTIN_CHOICES = [
        ('*', ''),
        ('OHMYFI', 'OHMYFI'),
        ('PQRS CLIENTES', 'PQRS CLIENTES'),
        ('REGISTROS DE MENORES DE EDAD', 'REGISTROS DE MENORES DE EDAD'),
        ('CIRCULO DE ESPECIALISTAS PISO DE VENTA', 'CIRCULO DE ESPECIALISTAS PISO DE VENTA'),
        ('FORMULARIO WEB ATG SISTEMA POSTVENTA (DEV-SERVICIO TECNICO)', 'FORMULARIO WEB ATG SISTEMA POSTVENTA (DEV-SERVICIO TECNICO)'),
        ('APP HOMECENTER', 'APP HOMECENTER'),
        ('ARARA', 'ARARA'),
        ('OTP DEV', 'OTP DEV'),
        ('FORMULARIO WEB FACTURA ELECTRONICA', 'FORMULARIO WEB FACTURA ELECTRONICA'),
        ('ATG- FORMULARIO REGISTRO PERSONAS', 'ATG- FORMULARIO REGISTRO PERSONAS'),
        ('DEVOLUCIONES', 'DEVOLUCIONES'),
        ('AVISO DE PRENSA', 'AVISO DE PRENSA'),
        ('SALES FINANCE- BANCO FALABELLA', 'SALES FINANCE- BANCO FALABELLA'),
        ('OTP SAPS', 'OTP SAPS'),
        ('AGENCIA SEGUROS FALABELLA', 'AGENCIA SEGUROS FALABELLA'),
        ('BANCO FALABELLA', 'BANCO FALABELLA'),
        ('OTP SISTEMA POSTVENTA (DEV-SERVICIO TECNICO)', 'OTP SISTEMA POSTVENTA (DEV-SERVICIO TECNICO)'),
    ]
    
    
    PERFIL_SEGMENTACION_CHOICES = [
        ('*', ''),
        ('HOGAR', 'Hogar'),
        ('VENTA EMPRESA', 'Venta empresa'),
        ('PROFESIONAL', 'Profesional'),
        ]
    
    columnas_disponibles = [
        ('Identificacion', 'Identificación'),
        ('Identificacion_corp', 'Identificación Corporativa'),
        ('Tipo_doc', 'Tipo de documento'),
        ('NOMBRES', 'Nombres'),
        ('APELLIDOS', 'Apellidos'),
        ('DIRECCION', 'Dirección'),
        ('CIUDAD', 'Ciudad'),
        ('ESPECIALIDAD', 'Especialidad'),
        ('CONTACTABLE_SODIMAC', 'Contactable Sodimac'),
        ('CONTACTABLE_TERCERO', 'Contactable Tercero'),
        ('CANAL_OPTIN', 'Canal Optin'),
        ('FECHA_AUTORIZACION', 'Fecha de Autorización'),
        ('PERIODO_SEGMENTACION', 'Periodo de Segmentación'),
        ('PERFIL_SEGMENTACION', 'Perfil de Segmentación'),
        ('SEGMENTO_NECESIDAD', 'Segmento de Necesidad'),
        ('SEGMENTO_VALOR', 'Segmento de Valor'),
        ('CICLO_VIDA', 'Ciclo de Vida'),
        ('TIENDA_FRECUENTE', 'Tienda Frecuente'),
        ('FAMILIA_MAYOR_FRECUENCIA', 'Familia de Mayor Frecuencia'),
        ('TIPO_SEGMENTO', 'Tipo de Segmento'),
        ('PIRAMIDE', 'Pirámide'),
        ('GENERO', 'Género'),
        ('FECHA_NACIMIENTO', 'Fecha de Nacimiento'),
        ('ESTADO_CES', 'Estado CES'),
        ('PROFESION', 'Profesión'),
        ('SEGMENTO_CES', 'Segmento CES'),
        ('FECHA_NIVEL', 'Fecha de Nivel'),
        ('FECHA_INICIAL_CES', 'Fecha Inicial CES'),
        ('FECHA_FIN_CES', 'Fecha Fin CES'),
        ('CREATED_AT', 'Fecha de Creación'),
        ('FECHA_INSCRIPCION_CMR', 'Fecha de Inscripción CMR'),
        ('TOTPUNTO', 'Total de Puntos'),
        ('RANGO_PUNTOS', 'Rango de Puntos'),
        ('PUNTOS_REDIMIDOS_12M', 'Puntos Redimidos en los Últimos 12 Meses'),
        ('MARCA_TDC', 'Marca de Tarjeta de Crédito'),
        ('MARCA_TDB', 'Marca de Tarjeta de Débito'),
        ('CLIENTE_ACTIVO', 'Cliente Activo'),
        ('FECHA_ULTIMA_COMPRA', 'Fecha de Última Compra'),
        ('CANAL_VD_ULTIMA_COMPRA', 'Canal de Venta de la Última Compra'),
        ('TIENDA_DESPACHA_ULTIMA_COMPRA', 'Tienda de Despacho de la Última Compra'),
        ('MEDIO_PAGO_ULTIMA_COMPRA', 'Medio de Pago de la Última Compra'),
        ('FLAG_CMR_PUNTOS', 'Puntos CMR'),
        ('FLAG_BANCO', 'Banco'),
        ('FLAG_CEC', 'CEC'),
        ('FLAG_CLIENTE360', 'Cliente 360'),
        ('FLAG_SEGMENTADOS', 'Segmentados'),
        ('FLAG_COMPRADORES_ACTIVOS', 'Compradores Activos'),
        ('FLAG_COMPRADORES_MES_CORTE', 'Compradores en Mes de Corte'),
        ('FLAG_COMPRADORES_ACUMULADOS', 'Compradores Acumulados'),
        ('FLAG_LOYALTY', 'Lealtad')
    ]
    ## Widgets
    
    #Visibles:
    #CONTACTABLE_SODIMAC = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Contactable Sodimac', required=False)
    #CONTACTABLE_TERCERO = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Contactable Tercero', required=False)
    #PERFIL_SEGMENTACION = forms.ChoiceField(choices=PERFIL_SEGMENTACION_CHOICES, label='Perfil de segmentación', required=False)
    #ESPECIALIDAD = forms.ChoiceField(choices=ESPECIALIDAD_CHOICES, label='Especialidad', required=False)
    #FLAG_CMR_PUNTOS = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente CMR', required=False)
    #FLAG_BANCO = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente del banco', required=False)
    #FLAG_CEC = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente CEC', required=False)
    #FLAG_CLIENTE360 = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente 360', required=False)
    #FLAG_SEGMENTADOS = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente segmentado', required=False)
    #FLAG_COMPRADORES_ACTIVOS = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Comprador activo', required=False)
    #FLAG_COMPRADORES_MES_CORTE = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Comprador del ultimo mes', required=False)
    #FLAG_LOYALTY = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente leal', required=False)
    #CLIENTE_ACTIVO = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente activo', required=False)
    
    #Invisibles: 
    Identificacion = forms.CharField(label='id', required=False, widget=forms.HiddenInput())
    Identificacion_corp = forms.CharField(label='id corp', required=False, widget=forms.HiddenInput())
    Tipo_doc = forms.ChoiceField(choices=TIPO_DOC_CHOICES, label='Tipo de Documento', required=False, widget=forms.HiddenInput())
    CIUDAD = forms.ChoiceField(choices=CIUDAD_CHOICES, label='Ciudad', required=False, widget=forms.HiddenInput())
    NOMBRES = forms.CharField(label='Nombres', required=False, widget=forms.HiddenInput())
    APELLIDOS = forms.CharField(label='Apellidos', required=False, widget=forms.HiddenInput())
    DIRECCION = forms.CharField(label='Dirección', required=False, widget=forms.HiddenInput())
    CANAL_OPTIN = forms.ChoiceField(choices=CANAL_OPTIN_CHOICES, label='Canal Optin', required=False, widget=forms.HiddenInput())
    FECHA_AUTORIZACION = forms.ChoiceField(label='Fecha Autorización', required=False, widget=forms.HiddenInput()) 
    PERIODO_SEGMENTACION = forms.ChoiceField(label='Periodo de segmentación', required=False, widget=forms.HiddenInput()) 
    SEGMENTO_NECESIDAD = forms.ChoiceField(label='Semento de necesidad', required=False, widget=forms.HiddenInput()) 
    SEGMENTO_VALOR = forms.ChoiceField(label='Segmento de valor', required=False, widget=forms.HiddenInput()) 
    CICLO_VIDA = forms.ChoiceField(label='Ciclo de vida', required=False, widget=forms.HiddenInput()) 
    TIENDA_FRECUENTE = forms.ChoiceField(label='Tienda frecuente', required=False, widget=forms.HiddenInput()) 
    FAMILIA_MAYOR_FRECUENCIA = forms.ChoiceField(label='Familia Mayor', required=False, widget=forms.HiddenInput()) 
    TIPO_SEGMENTO = forms.ChoiceField(label='Tipo de Segmentación', required=False, widget=forms.HiddenInput()) 
    PIRAMIDE = forms.ChoiceField(label='Piramide', required=False, widget=forms.HiddenInput()) 
    GENERO = forms.ChoiceField(label='Genero', required=False, widget=forms.HiddenInput()) 
    FECHA_NACIMIENTO = forms.ChoiceField(label='Fecha de nacimiento', required=False, widget=forms.HiddenInput()) 
    ESTADO_CES = forms.ChoiceField(label='Estado CES', required=False, widget=forms.HiddenInput()) 
    PROFESION = forms.ChoiceField(label='Profesión', required=False, widget=forms.HiddenInput()) 
    SEGMENTO_CES = forms.ChoiceField(label='Segmento CES', required=False, widget=forms.HiddenInput()) 
    FECHA_NIVEL = forms.ChoiceField(label='Fecha de adquisición de nivel', required=False, widget=forms.HiddenInput()) 
    FECHA_INICIAL_CES = forms.ChoiceField(label='Fecha de inicio CES', required=False, widget=forms.HiddenInput()) 
    FECHA_FIN_CES = forms.ChoiceField(label='Fecha fin de ces', required=False, widget=forms.HiddenInput()) 
    CREATED_AT = forms.ChoiceField(label='Creado en', required=False, widget=forms.HiddenInput()) 
    FECHA_INSCRIPCION_CMR = forms.ChoiceField(label='Fecha inscirpción a CMR', required=False, widget=forms.HiddenInput()) 
    TOTPUNTO = forms.ChoiceField(label='Total de puntos', required=False, widget=forms.HiddenInput()) 
    RANGO_PUNTOS = forms.ChoiceField(label='Rango de puntos', required=False, widget=forms.HiddenInput()) 
    PUNTOS_REDIMIDOS_12M = forms.ChoiceField(label='Puntos redimidos', required=False, widget=forms.HiddenInput()) 
    MARCA_TDC = forms.ChoiceField(label='Marca TDC', required=False, widget=forms.HiddenInput()) 
    MARCA_TDB = forms.ChoiceField(label='Marca TDB', required=False, widget=forms.HiddenInput()) 
    FECHA_ULTIMA_COMPRA = forms.ChoiceField(label='Fecha última comra', required=False, widget=forms.HiddenInput()) 
    CANAL_VD_ULTIMA_COMPRA = forms.ChoiceField(label='PCanal virtual de la última compra', required=False, widget=forms.HiddenInput()) 
    TIENDA_DESPACHA_ULTIMA_COMPRA = forms.ChoiceField(label='Tienda que despacha el último producto', required=False, widget=forms.HiddenInput()) 
    MEDIO_PAGO_ULTIMA_COMPRA = forms.ChoiceField(label='Medio de pago', required=False, widget=forms.HiddenInput()) 
    FLAG_COMPRADORES_ACUMULADOS = forms.ChoiceField(label='Cliente acumulado', required=False, widget=forms.HiddenInput()) 
        
    columnas_seleccionadas = forms.MultipleChoiceField(
        choices=columnas_disponibles,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Columnas Seleccionadas"
    )
    CONTACTABLE_SODIMAC = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Contactable Sodimac', required=False)
    CONTACTABLE_TERCERO = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Contactable Tercero', required=False)
    PERFIL_SEGMENTACION = forms.ChoiceField(choices=PERFIL_SEGMENTACION_CHOICES, label='Perfil de segmentación', required=False)
    ESPECIALIDAD = forms.ChoiceField(choices=ESPECIALIDAD_CHOICES, label='Especialidad', required=False)
    FLAG_CMR_PUNTOS = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente CMR', required=False)
    FLAG_BANCO = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente del banco', required=False)
    FLAG_CEC = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente CEC', required=False)
    FLAG_CLIENTE360 = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente 360', required=False)
    FLAG_SEGMENTADOS = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente segmentado', required=False)
    FLAG_COMPRADORES_ACTIVOS = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Comprador activo', required=False)
    FLAG_COMPRADORES_MES_CORTE = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Comprador del último mes', required=False)
    FLAG_LOYALTY = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente leal', required=False)
    CLIENTE_ACTIVO = forms.ChoiceField(choices=BOOLEAN_CHOICES, label='Cliente activo', required=False)
    
    
    

    class Meta:
        model = FormBasic
        fields = '__all__'
        

     
    
class ColumnSelectionForm(forms.Form):
    columnas = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        valores_por_columna = kwargs.pop('valores_por_columna', {})
        super().__init__(*args, **kwargs)
        
        # Establecer las opciones para el campo de selección múltiple (columnas)
        self.fields['columnas'].choices = self.get_column_choices()

        for columna, valores in valores_por_columna.items():
            # Almacenar los valores específicos en la sesión
            self.fields[columna] = forms.CharField(initial=valores, widget=forms.HiddenInput())
            
    def get_column_choices(self):    
        return [
            ('Identificacion', 'Identificación'),
            ('Identificacion_corp', 'Identificación Corporativa'),
            ('Tipo_doc', 'Tipo de documento'),
            ('NOMBRES', 'Nombres'),
            ('APELLIDOS', 'Apellidos'),
            ('DIRECCION', 'Dirección'),
            ('CIUDAD', 'Ciudad'),
            ('ESPECIALIDAD', 'Especialidad'),
            ('CONTACTABLE_SODIMAC', 'Contactable Sodimac'),
            ('CONTACTABLE_TERCERO', 'Contactable Tercero'),
            ('CANAL_OPTIN', 'Canal Optin'),
            ('FECHA_AUTORIZACION', 'Fecha de Autorización'),
            ('PERIODO_SEGMENTACION', 'Periodo de Segmentación'),
            ('PERFIL_SEGMENTACION', 'Perfil de Segmentación'),
            ('SEGMENTO_NECESIDAD', 'Segmento de Necesidad'),
            ('SEGMENTO_VALOR', 'Segmento de Valor'),
            ('CICLO_VIDA', 'Ciclo de Vida'),
            ('TIENDA_FRECUENTE', 'Tienda Frecuente'),
            ('FAMILIA_MAYOR_FRECUENCIA', 'Familia de Mayor Frecuencia'),
            ('TIPO_SEGMENTO', 'Tipo de Segmento'),
            ('PIRAMIDE', 'Pirámide'),
            ('GENERO', 'Género'),
            ('FECHA_NACIMIENTO', 'Fecha de Nacimiento'),
            ('ESTADO_CES', 'Estado CES'),
            ('PROFESION', 'Profesión'),
            ('SEGMENTO_CES', 'Segmento CES'),
            ('FECHA_NIVEL', 'Fecha de Nivel'),
            ('FECHA_INICIAL_CES', 'Fecha Inicial CES'),
            ('FECHA_FIN_CES', 'Fecha Fin CES'),
            ('CREATED_AT', 'Fecha de Creación'),
            ('FECHA_INSCRIPCION_CMR', 'Fecha de Inscripción CMR'),
            ('TOTPUNTO', 'Total de Puntos'),
            ('RANGO_PUNTOS', 'Rango de Puntos'),
            ('PUNTOS_REDIMIDOS_12M', 'Puntos Redimidos en los Últimos 12 Meses'),
            ('MARCA_TDC', 'Marca de Tarjeta de Crédito'),
            ('MARCA_TDB', 'Marca de Tarjeta de Débito'),
            ('CLIENTE_ACTIVO', 'Cliente Activo'),
            ('FECHA_ULTIMA_COMPRA', 'Fecha de Última Compra'),
            ('CANAL_VD_ULTIMA_COMPRA', 'Canal de Venta de la Última Compra'),
            ('TIENDA_DESPACHA_ULTIMA_COMPRA', 'Tienda de Despacho de la Última Compra'),
            ('MEDIO_PAGO_ULTIMA_COMPRA', 'Medio de Pago de la Última Compra'),
            ('FLAG_CMR_PUNTOS', 'Puntos CMR'),
            ('FLAG_BANCO', 'Banco'),
            ('FLAG_CEC', 'CEC'),
            ('FLAG_CLIENTE360', 'Cliente 360'),
            ('FLAG_SEGMENTADOS', 'Segmentados'),
            ('FLAG_COMPRADORES_ACTIVOS', 'Compradores Activos'),
            ('FLAG_COMPRADORES_MES_CORTE', 'Compradores en Mes de Corte'),
            ('FLAG_COMPRADORES_ACUMULADOS', 'Compradores Acumulados'),
            ('FLAG_LOYALTY', 'Lealtad')
        ]


