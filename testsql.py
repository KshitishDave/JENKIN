table_queries = {}

# Read the SQL file
with open("sql_file.sql", "r") as f:
    content = f.read()

# Split the SQL queries
sql_queries = content.split(';')

# Extract queries for each table
for query in sql_queries:
    words = query.split()
    if len(words) >= 4 and words[0].upper() == "INSERT" and words[1].upper() == "INTO":
        table_name = words[2]
        if table_name not in table_queries:
            table_queries[table_name] = []
        table_queries[table_name].append(query.strip() + ";")
# print(table_queries)

# Write queries to respective files
for table_name, queries in table_queries.items():
    with open(table_name + ".sql", "w") as s:
        for query in queries:
            # print(query)
            s.write(query + "\n")