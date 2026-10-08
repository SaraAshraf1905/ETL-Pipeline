SELECT
    ROW_NUMBER() OVER (ORDER BY product_name) AS product_key,
    product_name,
    series,
    price

FROM {{ ref('stg_products') }}