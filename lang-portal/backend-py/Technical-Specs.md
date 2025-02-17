# Backend Server Technical Specs

## Business Goal:

Business Goal: 
A language learning school wants to build a prototype of learning portal which will act as three things:
Inventory of possible vocabulary that can be learned
Act as a  Learning record store (LRS), providing correct and wrong score on practice vocabulary
A unified launchpad to launch different learning apps

## Technical Requirements
- The backend will be built using python
- The database will be SQLite3
- The API will be built using Gin
- The API will always return JSON
- There will no authentication or authorization
- Everything will be treated a single user

## Database Schema

Tables:
- words – Stores vocabulary words
    - id (integer, primary key)
    - thai (string)
    - english (string)
    - parts (JSON) – Stores additional word attributes

- words_groups – Join table for words and groups (Many-to-Many)
    - id (integer, primary key)
    - word_id (integer, foreign key → words.id)
    - group_id (integer, foreign key → groups.id)

- groups – Thematic groups of words
    - id (integer, primary key)
    - name (string)

- study_sessions – Records of study sessions
    - id (integer, primary key)
    - group_id (integer, foreign key → groups.id)

- study_activities – Links study sessions to vocabulary words
    - id (integer, primary key)
    - session_id (integer, foreign key → study_sessions.id)
    - word_id (integer, foreign key → words.id)
    - correct (boolean) – Whether the answer was correct

- words_review_items – Tracks word review sessions
    - id (integer, primary key)
    - word_id (integer, foreign key → words.id)
    - reviewed_at (timestamp)
    - correct (boolean)

### API Endpoints

- GET /words
- GET /words/:id
- GET /groups
- GET /groups/:id
- GET /groups/:id/words

## Key Considerations

1. Database Selection
Relational Databases (SQL-based) – If you need structured data with relationships.
PostgreSQL (best for scalability, indexing, and JSON support)
MySQL/MariaDB (widely used, good for high-read applications)
SQLite (lightweight, good for small projects)
NoSQL Databases – If you need flexibility and high-speed lookups.
MongoDB (great for document-based storage, flexible schemas)
Redis (best for caching and real-time applications)
Cassandra (high availability, distributed systems)
2. ORM vs. Raw Queries
ORM (Object-Relational Mapper) – Easier development, but slightly slower.
SQLAlchemy (most powerful for PostgreSQL/MySQL)
Tortoise-ORM (async ORM for FastAPI)
Raw SQL Queries – More efficient for large datasets, but requires manual handling.
3. Database Connection Management
Use connection pooling to avoid excessive database connections.
Example: asyncpg (for PostgreSQL), aiomysql (for MySQL).
Avoid long-lived connections; close them after queries.
4. API Design and Query Optimization
Implement pagination (limit results) to prevent excessive data fetching.
Use indexes on frequently queried columns.
Use prepared statements to prevent SQL injection.
Optimize joins and avoid N+1 query problems.
5. Caching for Performance
Use Redis or Memcached to store frequently accessed data.
Cache results of expensive database queries.
Implement Query Result Caching with FastAPI + Redis.
6. Security Best Practices
Use environment variables for database credentials (avoid hardcoding).
Enable TLS encryption for database connections.
Implement role-based access control (RBAC) in your database.
Use parameterized queries to prevent SQL injection.
7. Backup and Replication
Set up automated database backups (daily, weekly, etc.).
Use database replication (if high availability is needed).
Consider sharding for massive data scaling.
8. Handling High Traffic and Scaling
Use read replicas for load balancing.
Implement message queues (RabbitMQ, Kafka) for async processing.
Use database partitioning to distribute large datasets.
9. Monitoring and Logging
Enable query logging to track slow queries.
Use Prometheus + Grafana to monitor database performance.
Implement error tracking (Sentry, ELK stack).