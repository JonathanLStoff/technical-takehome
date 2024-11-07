WITH 
senators_per_state AS (
    SELECT state, COUNT(*) as total_senators
    FROM senators
    GROUP BY state
),
senators_with_requests AS (
    SELECT s.state, COUNT(DISTINCT s.senator_id) as senators_with_requests
    FROM senators s
    JOIN requests r ON s.senator_id = r.senator_id
    GROUP BY s.state
)
SELECT sps.state, 
        sps.total_senators as total_senators,
        swr.senators_with_requests as senators_who_made_request
FROM senators_per_state sps
JOIN senators_with_requests swr ON sps.state = swr.state
WHERE sps.total_senators = 2 
AND swr.senators_with_requests = 1
ORDER BY sps.state;