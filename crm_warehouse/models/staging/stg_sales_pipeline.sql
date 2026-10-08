SELECT
    opportunity_id,
    "sales_agent" AS agent_name,
    "product" AS product_name,
    "account" AS account_name,
    deal_stage,
    CAST("engage_date" AS DATE) AS engage_date,
    CAST("close_date" AS DATE) AS close_date,
    close_value AS close_value

FROM {{ source('raw', 'sales_pipeline') }}