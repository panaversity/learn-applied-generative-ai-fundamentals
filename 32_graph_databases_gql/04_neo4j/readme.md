# Neo4j

https://neo4j.com/docs/getting-started/

[Neo4j GQL conformance](https://neo4j.com/docs/cypher-manual/current/appendix/gql-conformance/)

Attend Conference on November 7, 2024

https://neo4j.com/nodes2024/agenda/

Courses:

https://graphacademy.neo4j.com/courses/neo4j-fundamentals/

https://graphacademy.neo4j.com/courses/cypher-fundamentals/


## Important Note:

For us the most important thing is the support of Graph Schema's in the database like this example:

### Creating a Graph
To create a new graph, you can define the graph schema and then instantiate it. For example:

```gql
CREATE GRAPH TYPE socialNetworkSchema (
  Person (name STRING, age INT),
  Friend (since DATE)
);

CREATE GRAPH socialNetwork OF TYPE socialNetworkSchema;
```ok