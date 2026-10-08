SELECT
    "sales_agent" AS agent_name,
    "manager" AS manager_name,
    regional_office
FROM {{ source('raw', 'sales_teams') }}