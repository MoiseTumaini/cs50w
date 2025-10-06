# Notes on lesson 4

## SQl

- allows us to relate data to each other in the for of tables 

## Common Database Management Systems: 

- MySQL
- PostgreSQL
- SQLite
- ...

## SQLite Types

- TEXT
- NUMERIC
- INTEGER
- REAL
- BLOB - Binary Large Object

## MySQL Types

- CHAR(size)
- VARCHAR(size) - variable character
- SMALLINT
- INT
- BIGINT
- FLOAT
- DOUBLE
- ...

## Common comands for SQL

### CREATE TABLE

```sql
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);
-- After creating the table name, the coloumns are separated by commas.
-- Each of the coloumns have a type
-- After the type there are additional constaints, e.g. PRIMARY KEY, NOT NULL (ensures that these columns are never empty)
-- AUTOINCREMENT is a column attribute is a cue into SQL to automatically update the id every time a new flight is added. So that I do not need to worry about adding the id itself but the other required colums instead. 
```

### Different Constraints 

- CHECK - used to make sure that a value obeys a certain condition
- DEFAULT - adds a default value
- NOT NULL 
- PRIMARY KEY 
- UNIQUE - guarantees every value is going to be unique
- ...

 ### INSERT

 ```sql
INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);

 ```

 ### SELECT

```sql
-- Narrow your search to the particular columns 
SELECT * FROM flights; -- select all the possible columns from that data flights
SELECT origin, destination FROM flights; -- select all data from the origin and destionation column in the flights table

-- Narrow your search to particular rows
SELECT * FROM flights WHERE id = 3; -- select all data from flights where the id is 3
SELECT * FROM flights WHERE origin = "New York"; -- select all data from flights where the origin is "New York"

-- Narrow your search to check in a particular sequence of possible values 
SELECT * From flights WHERE origin IN ("New York", "Lima")

```

### UPDATE

```sql
UPDATE flights 
    SET duration = 430
    WHERE origin = "New York"
    AND destination = "London";
```

### DELETE 

```sql
DELETE From flights WHERE destination = "Tokyo";
```

### Other Clauses

- LIMIT - limits the query search to the specified number 
- ORDER BY - allows to decide how the results are ordered 
- GROUP BY - allows to group rows together
- HAVING - a constraint, typically used on ORDER BY and GROUP BY
- ... 

## How Tables Relate to each other

- The use of a Foriegn key is a way to relate to tables 

### JOIN 

```sql
SELECT first, origin, destination FROM flights JOIN passengers ON passengers.flight_id = flights.id; 

-- select every person's first name, origin and their destination and select from flights table and join with the passengers table but only where the flights id are the same 
```

#### JOIN Types

- JOIN / INNER JOIN - compare 2 tables based on the condition that is specified 
- LEFT OUTER JOIN
- RIGHT OUTER JOIN 
- FULL OUTER JOIN

## CREATE INDEX

- Used as an additional data structure that make queries more efficient

```sql
CREATE INDEX name_index on passengers (last);
```

## SQL Injection Attack

- a security vulnerability happen if you are not careful as to how you execute your sql commands. 

```sql
select * from users
where username = "hacker"--" AND password = "";

-- notice how the password is being ignored, and the hacker can login in regardless 
``` 
 
## Race Condition 

- a condition when there are multiple events/queries that are happening in parallel threads. Conflicts can arise in this case

- can provide a lock on the database to solve this problem

## Django Models

- A way of representing data inside of a Django Application

