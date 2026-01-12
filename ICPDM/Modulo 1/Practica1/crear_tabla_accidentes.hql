
DROP TABLE IF EXISTS accidentes;
CREATE TABLE accidentes(
    num_expediente STRING,
    fecha DATE,
    hora TIMESTAMP,
    localizacion STRING,
    numero STRING,
    cod_distrito INT,
    distrito STRING,
    tipo_accidente STRING,
    estado_meteo STRING,
    tipo_vehiculo STRING,
    tipo_persona STRING,
    rango_edad STRING,
    sexo STRING,
    cod_lesividad DOUBLE,
    lesividad STRING,
    x_utm DOUBLE,
    y_utm DOUBLE,
    positiva_alcohol STRING,
    positiva_droga DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ";",
    "quoteChar"     = "\"",
    "escapeChar"    = "\\"
)
STORED AS TEXTFILE
TBLPROPERTIES (
    "serialization.encoding" = "UTF-8",
    "skip.header.line.count"="1"
);
