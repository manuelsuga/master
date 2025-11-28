
INSERT INTO TABLE convocatoria
SELECT     
    n_procedimiento,n_saf,desc_saf,n_uoc,desc_uoc,tipo_procedimiento,modalidad,apartado_directa,ejercicio,
    from_unixtime(
        unix_timestamp(
            regexp_replace(fecha_publicacion, '\\.', ''),
            'dd/MM/yyyy hh:mm:ss a'
        )
    ) AS fecha_publicacion,
    from_unixtime(
        unix_timestamp(
            regexp_replace(fecha_apertura, '\\.', ''),
            'dd/MM/yyyy hh:mm:ss a'
        )
    ) AS fecha_apertura,
    etapa,alcance,nom_procedimiento,obj_procedimiento,monto_estimado,tipo_operacion
FROM convocatoria_intermedia;
