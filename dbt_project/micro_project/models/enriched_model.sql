select
    id,
    greeting,
    upper(greeting) as greeting_upper,
    length(greeting) as greeting_length
from {{ ref('base_model') }}