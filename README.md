# volunteer_management_frappe_erpnext_app

An advanced, production-ready Volunteer Management System built on the **Frappe Framework** and **ERPNext**. This project is designed to support **millions of users**, featuring high scalability, security, and reliability. It demonstrates best practices with OOP principles, design patterns, RESTful APIs, and robust architectural concepts.

---
## 1. Architecture Overview

### 1.1 High-Level Design (HLD)

![High-Level Design Diagram](../diagrams/HLD.png)

**Key Components**:
1. **Client/Front-end** (JS or React/Vue):
   - Consumes RESTful APIs
   - Communicates with Frappe controllers

2. **Frappe/ERPNext** (Python):
   - Business logic in controllers, services, DocTypes
   - RESTful APIs using built-in Frappe endpoints
   - Database abstraction via Frappe ORM (MariaDB/PostgreSQL)

3. **Caching Layer** (Redis):
   - Stores sessions, caching frequently accessed volunteer data
   - Enhances concurrency & performance

4. **Load Balancer** (NGINX/ELB):
   - Distributes requests across multiple Frappe/ERPNext workers
   - Ensures high availability

### 1.2 Low-Level Design (LLD)

![Low-Level Design Diagram](../diagrams/LLD.png)

- **DocType: Volunteer**:
  - Fields: name, email, skills, availability, etc.
  - Linked with events, tasks
- **Controllers**:
  - `controllers.py` contain classes to manage business logic
  - Follows Service Layer pattern
- **Services**:
  - `services.py` perform heavy-lifting operations, external integrations (e.g., external APIs for sending notifications)
- **REST API**:
  - `rest_api.py` handles route definitions and endpoints
- **Database**:
  - All data is stored in the Frappe-backed SQL DB (MariaDB or PostgreSQL)
- **Caching**:
  - Redis used for session management, caching common queries

---
## 2. Technologies and Concepts Used

1. **Frappe Framework** (v14+)
2. **ERPNext** (v14+) integration
3. **Python 3.11**
4. **JavaScript / Node-based tooling** for building front-end
5. **Redis** for caching and queues
6. **Nginx** or **HAProxy** for load balancing
7. **OOP Principles** (Encapsulation, Inheritance, Polymorphism, Abstraction)
8. **Python Design Patterns** (Service layer, Factory pattern for object creation, Singleton for caching utilities, etc.)
9. **DSA (Data Structures and Algorithms)**: 
   - Efficient lookups (e.g., sets, hash maps)
   - Sorting and searching where relevant
10. **Advanced Architecture**:
    - CAP theorem considerations: 
      - Using consistent reads from the DB and eventually consistent caches
    - Scalability and Reliability
    - High Availability through horizontal scaling with multiple workers

---
## 3. Environment Variables

| Variable Name        | Description                                                | Default Value     |
|----------------------|------------------------------------------------------------|-------------------|
| `DB_HOST`            | Host address of the MariaDB/PostgreSQL server             | `localhost`       |
| `DB_PORT`            | Port for the DB                                           | `3306`            |
| `DB_NAME`            | Database name                                             | `erpnext`         |
| `DB_USER`            | Database user                                             | `root`            |
| `DB_PASSWORD`        | Password for the DB user                                  | `password`        |
| `REDIS_HOST`         | Host address for Redis caching                            | `localhost`       |
| `REDIS_PORT`         | Port for Redis                                            | `6379`            |
| `FRAPPE_SITE_NAME`   | Site name for Frappe                                      | `site1.local`     |
| `SECRET_KEY`         | Secret key for encryption/signing                         | `CHANGE_ME`       |
| `DEBUG`              | Debug mode toggle (True/False)                            | `False`           |
| `ALLOWED_HOSTS`      | Comma-separated list of hosts/IPs allowed                 | `localhost`       |
