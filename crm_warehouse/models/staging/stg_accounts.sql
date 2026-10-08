SELECT
    "account" AS account_name,
    sector,
    "employees" AS number_of_employees,
    office_location,
    year_established,
    revenue,
    subsidiary_of

FROM {{ source('raw', 'accounts') }}