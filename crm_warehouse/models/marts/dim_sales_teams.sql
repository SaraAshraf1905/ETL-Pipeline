SELECT
    ROW_NUMBER() OVER (ORDER BY agent_name) AS sales_agent_key,
    agent_name,
    manager_name,
    regional_office

FROM {{ ref('stg_sales_teams') }}