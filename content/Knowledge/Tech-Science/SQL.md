---
tags:
  - Programming
  - softwareengineering
  - Coding
  - Database
  - SQL
  - Hive
  - Postgresql
---
# Different Database Options

| Commands                                                     | Purpose |
| ------------------------------------------------------------ | ------- |
| `PRAGMA table_info(<table_name>)`                            |         |
| ```sql<br>SELECT ... <br>FROM ...<br>EXCEPT<br>   ...<br>``` |         |

| Commands (for Hive)                 | Purpose |
| ----------------------------------- | ------- |
| `CREATE TABLE ...`                  |         |
| `CREATE TABLE IF NOT EXISTS ...`    |         |
| `DROP TABLE ...`                    |         |
| `CREATE OR REPLACE TABLE ...`       |         |
| `ALTER TABLE ... RENAME TO ...`     |         |
| `ALTER TABLE ... SET LOCATION`      |         |
| `DESCRIBE`                          |         |
| `DESCRIBE FORMATTED`                |         |
| `ALTER TABLE ... DROP PARITION ...` |         |
| `ALTER TABLE ... ADD PARTITION ...` |         |
| `SHOW PARTITIONS`                   |         |
|                                     |         |
# PostgreSQL Commands
## List all tables in a specific schema
```sql
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
```

## List all tables with their schemas
```sql
SELECT table_schema, table_name 
FROM information_schema.tables 
WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
ORDER BY table_schema, table_name;
```



## Get column details for a specific table:

```sql
SELECT 
    column_name,
    data_type,
    is_nullable,
    column_default,
    character_maximum_length
FROM information_schema.columns 
WHERE table_schema = 'public' 
AND table_name = 'your_table_name'
ORDER BY ordinal_position;
```

## Get all columns from all tables
```sql
SELECT 
    table_schema,
    table_name,
    column_name,
    data_type,
    is_nullable
FROM information_schema.columns 
WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
ORDER BY table_schema, table_name, ordinal_position;
```