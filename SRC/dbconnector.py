import cx_Oracle
import pandas as pd
low_memory=False



dsn_1 = cx_Oracle.makedsn('cioba',\
 '8831', service_name='prdapp44.anp.net')
con = cx_Oracle.connect(user='USER_EQUIPESSM', \
    password='SSM123', dsn = dsn_1)

qry = 'SELECT COD_SONDA, NOM_TIPO_INCIDENTE, \
    DAT_PRIMEIRA_OBS, NK_INC, NUM_LATITUDE, \
        NUM_LONGITUDE FROM FT_INCIDENTE'
inc = pd.read_sql(qry, con)