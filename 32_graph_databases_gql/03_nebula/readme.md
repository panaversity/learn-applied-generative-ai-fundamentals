# Nebula Graph

[NebulaGraph Enterprise: The First Distributed Graph Database to Offer Native GQL Support](https://www.nebula-graph.io/posts/nebulagraph_enterprise_5.0_gql_support)

**Nebula Graph** the only choice for a graph database that fully supports the GQL standard. It offers several compelling features:

* **High performance:** Nebula Graph is designed for high-performance graph processing and storage. It uses a distributed architecture and optimized data structures to achieve high throughput and low latency.
* **Scalability:** The database can scale horizontally to handle large datasets and high traffic loads.
* **Flexibility:** Nebula Graph supports both property graphs and hypergraphs, making it suitable for a wide range of use cases.
* **Open-source:** Nebula Graph is an open-source project, providing flexibility and control over your database environment.
* **Strong community support:** It has a growing community of developers and users, offering resources and assistance.

**Key advantages of Nebula Graph:**

* **High performance:** Optimized for large-scale graph processing.
* **Scalability:** Can handle massive datasets and high traffic.
* **Flexibility:** Supports both property graphs and hypergraphs.
* **Open-source:** Provides flexibility and control.
* **Strong community support:** Active community for resources and assistance.

If you're looking for a high-performance, scalable, and flexible graph database with strong GQL support, Nebula Graph is definitely worth considering.

## Using it in Developing Personalized Learning Systems

Personalized learning systems can greatly enhance the educational experience by tailoring content to individual needs and learning styles.

Using a graph database like Nebula Graph, with its full support for the GQL standard, can be particularly beneficial. It allows you to efficiently manage and query complex relationships between different pieces of educational content, user interactions, and learning outcomes.

## Keeping Our Eyes Open: Neo4j and Amazon Neptune

Nebula Graph is indeed one of the leading graph databases that has made significant strides in supporting the GQL standard. However, it's important to note that other databases like Neo4j and Amazon Neptune are also actively working towards full GQL compliance. While Nebula Graph may currently offer robust support, it's always good to keep an eye on developments from other major players in the field.

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
```