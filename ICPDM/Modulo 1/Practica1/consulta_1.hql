
SELECT sexo, COUNT(*) as total_por_sexo
FROM accidentes
WHERE rango_edad LIKE '%25 a 29%' AND positiva_alcohol = 'S' AND estado_meteo LIKE '%Lluvia%'
GROUP BY sexo;
