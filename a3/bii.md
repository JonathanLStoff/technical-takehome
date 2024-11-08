## Part B: Section ii Answers - Architecture Design

1. Describe how you would architect such a system. In your answer, describe alternatives you considered and the tradeoffs of each compared to your preferred design.

A. 
**Preferred Design**:
- **Database**: I would use a relational database to store the data. Relational databases are well-suited for structured data and can handle complex queries efficiently. Given that the system needs to track relationships between requests, a relational database would be a good fit. PostgreSQL would be a good choice due to its performance, scalability, and support for complex queries.
- **Data Schema**: I would design the data schema with two main tables: `requests` and `duplicates`. The `requests` table would store information about each request, and the `duplicates` table would store relationships between requests that are marked as duplicates. The `requests` table would have a foreign key referencing the `duplicates` table to establish the relationships. Likely duplicates could be linked to a row in the `duplicates` table with a confirmed status indicating that they are potential duplicates. If only one request is known then it can still be added, and the other duplicates can be added later. Another column would be added to the `requests` table to store if it is confirmed not a duplicate.
e.g.:
```
CREATE TABLE duplicates (
    duplicate_id SERIAL PRIMARY KEY,
    confirmed BOOLEAN DEFAULT FALSE
    description VARCHAR(255)
);


CREATE TABLE requests (
    request_id INTEGER PRIMARY KEY,
    duplicate_id INTEGER REFERENCES duplicates(duplicate_id) ON DELETE SET NULL,
    not_duplicate BOOLEAN DEFAULT FALSE,
    senator_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    recipient VARCHAR(255) NOT NULL
);
```

**Alternative**:
- **Database**: An alternative approach could be to use a document-oriented database like MongoDB. Document databases are schema-less and can handle unstructured data well. However, trying to track relationships would require more work and potentially slower queries compared to a relational database.
- **Data Schema**: Other alternatives could include complex triggers/functions, but these could introduce performance issues and make the system harder to maintain. Triggers also take out some ability to integrate with other systems like Django's models. Using Django's models would be a great way to control and integrate the database with other systems, and frontend control.