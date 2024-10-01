# Graph Query Lanaguage: The ISO standard for Graphs has arrived

https://www.theregister.com/2024/04/24/gql_iso_recognition/

https://www.theregister.com/2023/03/10/great_graph_debate_friday/

https://finance.yahoo.com/news/nebulagraph-enterprise-v5-0-first-140000670.html


The Graph Query Language (GQL) is an ISO standard specifically designed for querying property graphs. Officially published as ISO/IEC 39075:2024, GQL is the first new database language standard since SQL¹².

GQL provides a declarative approach to managing and querying property graphs, which are a type of graph where nodes (vertices) and edges (relationships) can have associated properties (key-value pairs). This makes it particularly powerful for complex data structures and relationships²³.

Key features of GQL include:
- **Creation and management** of property graphs.
- **CRUD operations** (Create, Read, Update, Delete) on nodes and edges.
- **Advanced querying capabilities** for traversing and analyzing graph data⁴.

This standard aims to unify and standardize the way property graphs are handled, much like SQL did for relational databases².

Is there something specific you would like to know about GQL or its applications?

Source: Conversation with Copilot, 10/1/2024
(1) Graph Query Language GQL. https://www.gqlstandards.org/.
(2) Graph Query Language - Wikipedia. https://en.wikipedia.org/wiki/Graph_Query_Language.
(3) The Rise of GQL: A New ISO Standard in Graph Query Language - TigerGraph. https://www.tigergraph.com/blogs/gsql/the-rise-of-gql-a-new-iso-standard-in-graph-query-language/.
(4) Understanding GQL: A Comprehensive Overview of the Standard Graph Query .... https://www.nebula-graph.io/posts/An_Comprehensive_Overview_of_the_Standard_Graph_Query_Language.
(5) Property Graph Standards Update - July 2020 - JCC 
Consulting. http://www.jcc.com/resources/jcc-blogs-menu/blog-database-dreams/122-property-graph-standards-update-july-2020.
(6) undefined. https://jtc1info.org/slug/gql-database-language/.

## The Databases

 Here are some databases that currently support or are planning to support the GQL standard:

1. **Neo4j**: Known for its Cypher query language, Neo4j is aligning its support with GQL¹⁴.
2. **Amazon Neptune**: This graph database service by AWS is also moving towards GQL compatibility¹⁴.
3. **TigerGraph**: TigerGraph's GSQL is another example of a graph query language that is converging towards GQL³.
4. **NebulaGraph**: NebulaGraph Enterprise v5.0 offers native GQL support⁵.

These databases are part of a broader movement to standardize graph database queries, making it easier for users to work with graph data across different platforms.


Source: Conversation with Copilot, 10/1/2024
(1) GQL: The ISO standard for graphs has arrived | AWS Database Blog. https://aws.amazon.com/blogs/database/gql-the-iso-standard-for-graphs-has-arrived/.
(2) ISO GQL: A Defining Moment in Database Innovation - Neo4j Graph Data .... https://neo4j.com/blog/gql-international-standard/.
(3) The Rise of GQL: A New ISO Standard in Graph Query Language - TigerGraph. https://www.tigergraph.com/blogs/gsql/the-rise-of-gql-a-new-iso-standard-in-graph-query-language/.
(4) Beyond a Query Language: How GQL is Shaping the Future of Graph Databases. https://www.nebula-graph.io/posts/How_GQL_is_Shaping_the_Future_of_Graph_Databases.
(5) Graph Query Language GQL. https://www.gqlstandards.org/home.
(6) undefined. https://jtc1info.org/slug/gql-database-language/.

The Graph Query Language (GQL) is an ISO standard specifically designed for querying property graphs. Officially published as ISO/IEC 39075:2024, GQL is the first new database language standard since SQL¹².

GQL provides a declarative approach to managing and querying property graphs, which are a type of graph where nodes (vertices) and edges (relationships) can have associated properties (key-value pairs). This makes it particularly powerful for complex data structures and relationships²³.

Key features of GQL include:
- **Creation and management** of property graphs.
- **CRUD operations** (Create, Read, Update, Delete) on nodes and edges.
- **Advanced querying capabilities** for traversing and analyzing graph data⁴.

This standard aims to unify and standardize the way property graphs are handled, much like SQL did for relational databases².

Is there something specific you would like to know about GQL or its applications?

Source: Conversation with Copilot, 10/1/2024
(1) Graph Query Language GQL. https://www.gqlstandards.org/.
(2) Graph Query Language - Wikipedia. https://en.wikipedia.org/wiki/Graph_Query_Language.
(3) The Rise of GQL: A New ISO Standard in Graph Query Language - TigerGraph. https://www.tigergraph.com/blogs/gsql/the-rise-of-gql-a-new-iso-standard-in-graph-query-language/.
(4) Understanding GQL: A Comprehensive Overview of the Standard Graph Query .... https://www.nebula-graph.io/posts/An_Comprehensive_Overview_of_the_Standard_Graph_Query_Language.
(5) Property Graph Standards Update - July 2020 - JCC Consulting. http://www.jcc.com/resources/jcc-blogs-menu/blog-database-dreams/122-property-graph-standards-update-july-2020.
(6) undefined. https://jtc1info.org/slug/gql-database-language/.

## Examples

https://www.nebula-graph.io/posts/An_Comprehensive_Overview_of_the_Standard_Graph_Query_Language

Here are some examples of how you can create and manage property graphs using GQL:

### Creating a Graph
To create a new graph, you can define the graph schema and then instantiate it. For example:

```gql
CREATE GRAPH TYPE socialNetworkSchema (
  Person (name STRING, age INT),
  Friend (since DATE)
);

CREATE GRAPH socialNetwork OF TYPE socialNetworkSchema;
```

### Adding Nodes and Edges
You can add nodes (vertices) and edges (relationships) to the graph:

```gql
INSERT INTO socialNetwork {
  (p1:Person {name: 'Alice', age: 30}),
  (p2:Person {name: 'Bob', age: 25}),
  (p1)-[:Friend {since: DATE '2020-01-01'}]->(p2)
};
```

### Querying the Graph
To query the graph, you can use pattern matching to find specific nodes and relationships:

```gql
MATCH (p:Person)-[f:Friend]->(q:Person)
WHERE p.name = 'Alice'
RETURN p, f, q;
```

### Updating Properties
You can update properties of nodes and edges:

```gql
MATCH (p:Person)
WHERE p.name = 'Alice'
SET p.age = 31;
```

### Deleting Nodes and Edges
To delete nodes and edges, you can use the `DETACH DELETE` command:

```gql
MATCH (p:Person)-[f:Friend]->(q:Person)
WHERE p.name = 'Alice' AND q.name = 'Bob'
DETACH DELETE p, f, q;
```

These examples illustrate some of the basic operations you can perform with GQL to manage property graphs⁶⁵. If you have any specific scenarios or more detailed queries, feel free to ask!

Source: Conversation with Copilot, 10/1/2024
(1) Understanding GQL: A Comprehensive Overview of the Standard Graph Query .... https://www.nebula-graph.io/posts/An_Comprehensive_Overview_of_the_Standard_Graph_Query_Language.
(2) Property Graph Standards Update - July 2020 - JCC Consulting. http://www.jcc.com/resources/jcc-blogs-menu/blog-database-dreams/122-property-graph-standards-update-july-2020.
(3) Graph Query Language - Wikipedia. https://en.wikipedia.org/wiki/Graph_Query_Language.
(4) GQL - initiating an industry standard property graph query language. https://db-engines.com/en/blog_post/78.
(5) Information technology — Database languages — GQL - ISO. https://www.iso.org/standard/76120.html.
(6) [2211.10962] PG-Schema: Schemas for Property Graphs - arXiv.org. https://arxiv.org/abs/2211.10962.



