## Part B: Section i Answers - Architecture Design

1. What kind of database would you use to store the data?

A. I would recommend a relational database since the data will be structured in a ways that is efficient for exporting and querying. More specifically, I would say PostgreSQL as it is fast, efficient, and developement continues to keep up with ever changing security needs.

2. How might you design the data schema? In particular, how would you efficiently track groups of duplicate requests?

A. Depending on the type of each column, I would endeavor to index the columns that have "mostly" unique values. The easiest example is that we have two items with the same description, but different request_id's. If we index the description column, we can quickly find all items with the same description. This would help in finding duplicates in order to present them to the user who marks duplicates.

Another table would help in tracking these duplicates by using a one-to-many relationship between the requests and the duplicates. Which could be grouped by duplicate_id.

Example:
```
CREATE TABLE duplicates (
    duplicate_id SERIAL PRIMARY KEY,
    description VARCHAR(255)
);


CREATE TABLE requests (
    request_id INTEGER PRIMARY KEY,
    duplicate_id INTEGER REFERENCES duplicates(duplicate_id) ON DELETE SET NULL,
    senator_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    recipient VARCHAR(255) NOT NULL
);
```


3. For questions 1 and 2, what other options did you consider? What are the tradeoffs between your selected approach and others you might have taken?

A. For 1, I think that the non-relational databases would be a poor choice as the data is structured and the relationships between the data are important. This would also make data export hard. As for the type of database, I would say that MySQL would be a good choice as well, but I think that PostgreSQL is a better choice for staying securely up to date and compatible with many technologies.

For 2, there are many other ways of going about this, however I believe that the way I have described is the most reliable method of tracking duplicates. Other methods like triggers or functions could be used to track and find duplicates, but a lot of databases become bogged down when doing queries on them when too many of these functions are in place.