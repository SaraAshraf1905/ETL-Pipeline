SELECT
    ROW_NUMBER() OVER (ORDER BY account_name) AS account_key,
    account_name,
    sector,
    number_of_employees,
    office_location,
    year_established,
    revenue,
    subsidiary_of

FROM {{ ref('stg_accounts') }}