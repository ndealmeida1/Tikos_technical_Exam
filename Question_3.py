##Name - Natasha De Almeida

'''Question 3: Database Design & Query Optimisation (SQL/NoSQL & Graph
Databases)
• Scenario: You are working with a complex dataset that involves relationships between various entities. You need to design a database schema to efficiently
store and query this data.'''


# Describe the database schema you'd use (SQL, NoSQL, or Graph database), justifying your choice based on the data and query requirements.
'''A graph database like Neo4j would be the best option for a dataset that has intricate interactions between different elements.  Graph databases store data as nodes 
(entities) and edges (relationships), enabling more effective and user-friendly querying of highly linked data than standard relational databases, which need numerous 
joins to traverse relationships.  When the main queries entail relationship-heavy tasks like determining the shortest pathways, making suggestions, or comprehending 
network architecture, this design is very advantageous.  In comparison to SQL or NoSQL alternatives, a graph structure provides greater performance and flexibility 
when the use case entails hierarchical data, frequent traversal, or many-to-many links.'''

#Write sample SQL or NoSQL queries to retrieve specific data and relationships.
'''SQL Example


SELECT p.item, p.price
FROM Items p
JOIN Users u ON p.user_id = u.user_id
WHERE u.name = 'Alice';

'''

''''NoSQL Example
db.items.find({ "user.name": "Alice" })
'''


# Discuss how you'd optimise queries for performance, especially when dealing with large datasets and complex relationships.\
'''Several techniques may be used to optimise queries for performance, particularly when dealing with complicated connections and huge datasets.  Lookup time in a 
graph database can be decreased by indexing node characteristics that are often requested.  By beginning with well-indexed nodes and implementing filters early in 
the traversal, query patterns should be created to reduce the search space.  Performance may be greatly improved for SQL databases by indexing main and foreign keys, 
denormalising when needed, and utilising strategies like query caching or materialised views.  By examining execution plans, bottlenecks may be found and queries can 
be optimised appropriately.'''

#If using a graph database, explain why, and explain how you would query the data.
'''Languages like Cypher (in Neo4j), which is expressive and made especially for working with patterns in graphs, are used to query data while utilising a graph database. 
For instance, a Cypher query may simply use a pattern match to discover all users who are two degrees away from a certain user. This would be difficult and wasteful in 
a relational database because of the numerous joins needed.'''

#Explain the difference between SQL and NoSQL databases, and when to use each.
'''The type of data and the needs of the application determine whether to use a SQL or NoSQL database.  For structured data with clearly defined schemas that need ACID 
compliance, intricate transactions, and high consistency, SQL databases are ideal.  They perform exceptionally well in use scenarios such as typical commercial 
applications, inventory management, and finance systems.  On the other hand, NoSQL databases are excellent for flexible schema design, high scalability requirements, 
and unstructured or semi-structured data.  They provide use cases including IoT data input, large-scale content management, and real-time analytics.  Under the NoSQL 
umbrella, key-value stores, document databases, and wide-column stores provide a variety of architectures tailored to meet distinct performance and scalability 
requirements.'''