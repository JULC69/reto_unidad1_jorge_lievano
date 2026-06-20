ESTUDIANTE: Jorge Uriel Liévano Cifuemtes
Viernes 1 de junio de 2026
========================================================================
Q1 — SELECT DISTINCT
Lista todos los productos únicos disponibles usando un alias de 
columna descriptivo.
------------------------------------------------------------------------

SELECT DISTINCT
       producto AS producto_disponible
FROM ventas
WHERE producto IS NOT NULL

========================================================================
Q2 — WHERE + BETWEEN
Filtra pedidos del primer trimestre (ene–mar 2024) con cantidad mayor a 
5 unidades.
------------------------------------------------------------------------
SELECT *
FROM ventas
WHERE fecha BETWEEN '2024-01-01'
                AND '2024-03-31'
  AND cantidad > 5;

========================================================================
Q3 — GROUP BY + HAVING
Vendedores cuyo ingreso bruto total (cantidad × precio) supera $10,000 USD.
------------------------------------------------------------------------
SELECT
    vendedor,
    SUM(cantidad * precio_unitario) AS ingreso_bruto
FROM ventas
GROUP BY vendedor
HAVING ingreso_bruto > 10000;

========================================================================
Q4 — COUNT + SUM + AVG
Por categoría: total de pedidos, suma de unidades vendidas y precio 
unitario promedio.
------------------------------------------------------------------------
SELECT
    categoria,
    COUNT(*) AS total_pedidos,
    SUM(cantidad) AS total_unidades,
    AVG(precio_unitario) AS precio_promedio
FROM ventas
GROUP BY categoria;

========================================================================
Q5 — JOIN
Crea la tabla vendedores (abajo) y calcula el % de cumplimiento de 
meta de cada uno.
------------------------------------------------------------------------
Q5.1 — Crear tabla vendedores
------------------------------------------------------------------------
CREATE TABLE vendedores(
    vendedor TEXT,
    zona TEXT,
    meta_mensual REAL
)

------------------------------------------------------------------------
Q5.2 — Conuslta: Calcula el % de cumplimiento de meta de cada uno.
------------------------------------------------------------------------
SELECT
    v.vendedor,
    v.zona,
    v.meta_mensual,

    SUM(
        vt.cantidad *
        vt.precio_unitario
    ) AS venta_real,

    ROUND(
        SUM(
            vt.cantidad *
            vt.precio_unitario
        ) * 100.0 /
        v.meta_mensual,
        2
    ) AS porcentaje_cumplimiento

FROM ventas vt
JOIN vendedores v
     ON vt.vendedor = v.vendedor

GROUP BY
    v.vendedor,
    v.zona,
    v.meta_mensual;


========================================================================
Q6 — Subconsulta
Encuentra el cliente que generó el mayor ingreso total en el primer semestre.
------------------------------------------------------------------------
SELECT *
FROM
(
    SELECT
        cliente_id,
        SUM(
            cantidad *
            precio_unitario
        ) AS ingreso_total
    FROM ventas
    GROUP BY cliente_id
)
ORDER BY ingreso_total DESC
LIMIT 1;

