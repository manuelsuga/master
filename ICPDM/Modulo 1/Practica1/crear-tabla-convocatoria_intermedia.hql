
DROP TABLE IF EXISTS convocatoria_intermedia;
CREATE TABLE convocatoria_intermedia(
    n_procedimiento STRING,
    n_saf INT,
    desc_saf STRING,
    n_uoc INT,
    desc_uoc STRING,
    tipo_procedimiento STRING,
    modalidad STRING,
    apartado_directa STRING,
    ejercicio INT,
    fecha_publicacion STRING,
    fecha_apertura STRING,
    etapa STRING,
    alcance STRING,
    nom_procedimiento STRING,
    obj_procedimiento STRING,
    monto_estimado DOUBLE,
    tipo_operacion STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar"     = "\"",
    "escapeChar"    = "\\"
)
STORED AS TEXTFILE
TBLPROPERTIES (
    "serialization.encoding" = "UTF-8"
);
