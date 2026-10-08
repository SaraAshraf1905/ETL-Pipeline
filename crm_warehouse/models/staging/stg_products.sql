SELECT
    product AS product_name,
    series,
    CAST("sales_price" AS DECIMAL(10,2)) AS price
FROM {{ source('raw', 'products') }}