##Name - Natasha De Almeida
##Tikos Research Engineering technical assessment


##Question 1: Scalable Data Processing & API Integration (Python & System Design)
'''Scenario: You have been tasked with building a backend service that takes in large amounts of data from various external APIs (RESTful and GraphQL).
This data needs to be processed, transformed, and stored efficiently in a database (SQL or NoSQL). The service must then make this processed data
available via a RESTful API for client applications.'''

#Write Python code (or pseudo-code) showing how you'd handle data ingestion, transformation, and storage. Consider efficiency and scalability.


'''The following is a high-level pseudo-code architecture for a backend service that may grow:

 Absorbs information from several external REST and GraphQL APIs.

 cleans and transforms the data

 Effectively stores the data (for example, in a SQL database like PostgreSQL or a NoSQL database like MongoDB).

 makes the data available using a RESTful API (like FastAPI).
 
 asyncio, aiohttp and celery makes it can be used to fetch APIs concurrently'''


#Describe the architectural design of your API, focusing on how you'd ensure performance, reliability, and security.

'''In order to effectively manage concurrent requests and backend processing, the system design starts with external APIs as the data source, 
which are coupled to an asynchronous ingestion layer utilising technologies like aiohttp, asyncio, and Celery.  After being cleansed and organised 
in a transformation layer, the ingested data moves on to a storage layer where, depending on the use case, it is stored in either PostgreSQL or MongoDB.  
A RESTful API constructed with FastAPI, which has identification and rate-limiting features, is then used to make this data public.  The system employs 
JWT-based authentication, rate limitation with libraries like slowapi, and HTTPS enforcement with a reverse proxy like Nginx for security.'''


#Discuss how you'd implement parallel processing or multi-threading to manage the large data volumes.

'''Asynchronous I/O methods and parallel computing can be used in tandem to effectively manage massive data volumes.  
Using asynchronous I/O libraries like asyncio and aiohttp enables the system to submit several requests in parallel without stopping, greatly increasing 
performance for network-bound processes like retrieving data from multiple external APIs.  A task queue system like Celery or RQ may be used to offload 
processing to background workers for labour-intensive or time-consuming activities like data transformation or enrichment. This allows for horizontal scaling 
and improved resource utilisation.  Batch processing techniques should be used to optimise database interactions; committing API data fetches to the database 
in chunks and grouping them together reduces I/O overhead.'''

#Describe how you'd handle error handling and logging.
'''RotatingFileHandler and other capabilities of the Python logging module should be used for logging in order to control log rotation and stop log files from 
increasing endlessly.  To give logs clarity and control over their verbosity, distinct log levels like INFO, ERROR, and DEBUG should be defined.  Ingestion 
logs can benefit greatly from structured logging, such as json-logger, which makes them machine-readable and searchable.  Resilience against temporary failures 
is ensured in error handling by providing retry methods utilising libraries like as Tenacity or Celery's built-in retry capabilities.  A gentle fallback method 
that reports the error, omits the problematic data, and optionally sounds an alarm should be in place for unsuccessful API requests.
Celery's dead-letter queues may be used to record and archive unsuccessful tasks for subsequent review or rework.  While connecting with tools like Sentry 
enables real-time fault tracking and alert notifications, Prometheus and Grafana offer a strong solution for monitoring and alerting by tracking system metrics 
and performance.'''
