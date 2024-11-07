SELECT requests.request_id, senators.last_name, senators.party, requests.title
FROM requests
JOIN senators ON requests.senator_id = senators.senator_id
WHERE senators.party = 'Democrat'
ORDER BY requests.request_id;