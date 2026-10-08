SELECT
    ROW_NUMBER() OVER (ORDER BY p.opportunity_id) AS opportunity_key,

    a.account_key,
    pr.product_key,
    sa.sales_agent_key,

    p.opportunity_id,
    p.deal_stage,
    p.engage_date,
    p.close_date,
    p.close_value

FROM {{ ref('stg_sales_pipeline') }} AS p

LEFT JOIN {{ ref('dim_account') }} AS a
    ON p.account_name = a.account_name

LEFT JOIN {{ ref('dim_products') }} AS pr
    ON p.product_name = pr.product_name

LEFT JOIN {{ ref('dim_sales_teams') }} AS sa
    ON p.agent_name = sa.agent_name