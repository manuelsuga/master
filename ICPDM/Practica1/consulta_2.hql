
SELECT tipo_vehiculo, COUNT(*) as total_por_vehiculo
FROM accidentes
WHERE (rango_edad LIKE '%30 a 34%' OR rango_edad LIKE '%35 a 39%' OR rango_edad LIKE '%40 a 44%' OR rango_edad LIKE '%45 a 50%') AND tipo_accidente = 'Alcance' AND localizacion LIKE '%AVDA.%'
GROUP BY tipo_vehiculo;
