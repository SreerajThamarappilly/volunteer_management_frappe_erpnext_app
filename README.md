# volunteer_management_frappe_erpnext_app

An advanced, production-ready Volunteer Management System built on the **Frappe Framework** and **ERPNext**. This project is designed to support millions of users, featuring high scalability, security, and reliability. It demonstrates best practices with OOP principles, design patterns, RESTful APIs, and robust architectural concepts.

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

1. **Frappe Framework 5.23.0**
2. **ERPNext** integration
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

---
## 4. Running the Application Locally

### 4.1 Prerequisites

- **Python 3.11**
- **Node.js** and **npm** (for front-end assets)
- **Redis** installed locally or accessible
- **PostgreSQL** installed locally or accessible
- **Bench CLI** (Frappe/ERPNext)
- **Git** installed

### 4.2 Steps

1. **Install required Python packages**:

```bash
pip install -r requirements.txt
```

2. **Install Frappe/ERPNext (if not already done)**:

```bash
# Use Bench to init a frappe-bench
bench init frappe-bench
cd frappe-bench
bench get-app erpnext --branch version-14
bench get-app ../volunteer_management_frappe_erpnext_app # path to cloned folder
```

3. **Create a new site**:

```bash
bench new-site site1.local \
    --db-name ${DB_NAME} \
    --db-host ${DB_HOST} \
    --db-port ${DB_PORT} \
    --db-user ${DB_USER} \
    --db-password ${DB_PASSWORD}
```

4. **Install apps on the site**:

```bash
bench --site site1.local install-app erpnext
bench --site site1.local install-app volunteer_management_frappe_erpnext_app
```

5. **Start bench**:

```bash
bench start
```

6. **Access the site at**:

```bash
http://localhost:8000
```

### 4.3 Testing the Application

Use Postman or CURL to test the REST endpoints.

```bash
# Example: Fetch all volunteers
curl -X GET http://localhost:8000/api/method/volunteer_management_frappe_erpnext_app.volunteer_management_frappe_erpnext_app.modules.volunteer_management.rest_api.get_all_volunteers
```

```bash
# Example: Create a new volunteer
curl -X POST http://localhost:8000/api/method/volunteer_management_frappe_erpnext_app.volunteer_management_frappe_erpnext_app.modules.volunteer_management.rest_api.create_volunteer \
    -H 'Content-Type: application/json' \
    -d '{
          "name": "Sreeraj Thamarappilly",
          "email": "sreeraj.techie@gmail.com",
          "skills": ["Python", "Data Analysis"]
        }'
```

---
## 5. Deploying to AWS

### 5.1 Infrastructure Setup

1. **EC2 Instances**: Host Frappe/ERPNext with multiple workers.
2. **RDS (PostgreSQL)**: Managed DB for high availability.
3. **ElastiCache (Redis)**: Managed Redis for caching sessions, data.
4. **Load Balancer (ELB or ALB)**: Distribute traffic to multiple EC2 instances.
5. **S3 (optional)**: For file backups, static assets.

### 5.2 Deployment Steps

1. Provision an EC2 instance and install Bench, Frappe, Python, Redis CLI.
2. Connect EC2 instance to your RDS and ElastiCache instances (update .env).
3. Clone this repo on EC2 and install dependencies (pip install -r requirements.txt).
4. Install Frappe/ERPNext apps on your bench environment.
5. Set up Supervisor or Systemd to run Bench processes in the background.
6. Configure Nginx with a domain or subdomain pointing to your instance.
7. Scale horizontally by adding more EC2 instances behind a Load Balancer if traffic demands it.

---
## 6. License

*This project is licensed under the MIT License.*
