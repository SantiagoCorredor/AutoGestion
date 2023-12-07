from django.db import models


# Create your models here.
class FormBasic(models.Model):
    Identificacion = models.IntegerField()
    Identificacion_corp = models.IntegerField()
    Tipo_doc = models.CharField(max_length=255)
    NOMBRES = models.CharField(max_length=255)
    APELLIDOS = models.CharField(max_length=255)
    DIRECCION = models.CharField(max_length=255)
    CIUDAD = models.CharField(max_length=255)
    ESPECIALIDAD = models.CharField(max_length=255)
    CONTACTABLE_SODIMAC = models.CharField(max_length=20)
    CONTACTABLE_TERCERO = models.CharField(max_length=20)
    CANAL_OPTIN = models.CharField(max_length=255)
    FECHA_AUTORIZACION = models.CharField(max_length=255)
    PERIODO_SEGMENTACION = models.CharField(max_length=255)
    PERFIL_SEGMENTACION = models.CharField(max_length=255)
    SEGMENTO_NECESIDAD = models.CharField(max_length=255)
    SEGMENTO_VALOR = models.CharField(max_length=255)
    CICLO_VIDA = models.CharField(max_length=255)
    TIENDA_FRECUENTE = models.CharField(max_length=255)
    FAMILIA_MAYOR_FRECUENCIA = models.CharField(max_length=255)
    TIPO_SEGMENTO = models.CharField(max_length=255)
    PIRAMIDE = models.CharField(max_length=255)
    GENERO = models.CharField(max_length=255)
    FECHA_NACIMIENTO = models.CharField(max_length=255)
    ESTADO_CES = models.CharField(max_length=255)
    PROFESION = models.CharField(max_length=255)
    SEGMENTO_CES = models.CharField(max_length=255)
    FECHA_NIVEL = models.CharField(max_length=255)
    FECHA_INICIAL_CES = models.CharField(max_length=255)
    FECHA_FIN_CES = models.CharField(max_length=255)
    CREATED_AT = models.CharField(max_length=255)
    FECHA_INSCRIPCION_CMR = models.CharField(max_length=255)
    TOTPUNTO = models.IntegerField()
    RANGO_PUNTOS = models.CharField(max_length=255)
    PUNTOS_REDIMIDOS_12M = models.CharField(max_length=255)
    MARCA_TDC = models.CharField(max_length=255)
    MARCA_TDB = models.CharField(max_length=255)
    CLIENTE_ACTIVO = models.CharField(max_length=255)
    FECHA_ULTIMA_COMPRA = models.CharField(max_length=255)
    CANAL_VD_ULTIMA_COMPRA = models.CharField(max_length=255)
    TIENDA_DESPACHA_ULTIMA_COMPRA = models.CharField(max_length=255)
    MEDIO_PAGO_ULTIMA_COMPRA = models.CharField(max_length=255)
    FLAG_CMR_PUNTOS = models.CharField(max_length=255)
    FLAG_BANCO = models.CharField(max_length=255)   
    FLAG_CEC = models.CharField(max_length=255)
    FLAG_CLIENTE360 = models.CharField(max_length=255)
    FLAG_SEGMENTADOS = models.CharField(max_length=255)
    FLAG_COMPRADORES_ACTIVOS = models.CharField(max_length=255)
    FLAG_COMPRADORES_MES_CORTE = models.CharField(max_length=255)
    FLAG_COMPRADORES_ACUMULADOS = models.CharField(max_length=255)
    FLAG_LOYALTY = models.CharField(max_length=255)

    class Meta:
        verbose_name = "FormBasic"
        verbose_name_plural = "FormBasics"

    def __str__(self):
        return self.id

