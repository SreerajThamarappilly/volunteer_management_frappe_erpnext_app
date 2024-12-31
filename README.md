# volunteer_management_frappe_erpnext_app

An advanced, production-ready Volunteer Management System built on the **Frappe Framework** and **ERPNext**, with a **React** front-end. This project is designed to support millions of users, featuring high scalability, security, and reliability. It demonstrates best practices with OOP principles, design patterns, RESTful APIs, and robust architectural concepts.

---
## 1. Architecture Overview

### 1.1 High-Level Design (HLD)

**Key Components**:

1. **Client/Front-end** (React.js):
   - Consumes RESTful APIs
   - Communicates with Frappe controllers

2. **Frappe/ERPNext** (Python):
   - Business logic in controllers, services, DocTypes
   - RESTful APIs using built-in Frappe endpoints
   - Database abstraction via Frappe ORM (PostgreSQL)

3. **Caching Layer** (Redis):
   - Stores sessions, caching frequently accessed volunteer data
   - Enhances concurrency & performance

4. **Load Balancer** (NGINX/ELB):
   - Distributes requests across multiple Frappe/ERPNext workers
   - Ensures high availability

### 1.2 Low-Level Design (LLD)

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
  - All data is stored in the Frappe-backed SQL DB (PostgreSQL)
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
## 3. Directory Structure

```bash
volunteer_management_frappe_erpnext_app/
├── README.md              // Project overview, usage, instructions
├── .env.example           // Sample environment variables
├── requirements.txt       // Python dependencies
├── setup.py               // Setup script (if packaging as a Python package)
├── volunteer_management_frappe_erpnext_app/
│   ├── volunteer_management_frappe_erpnext_app/
│   │   ├── hooks.py
│   │   ├── modules/
│   │   │   └── volunteer_management/
│   │   │       ├── doctype/
│   │   │       │   └── volunteer/
│   │   │       │       ├── volunteer.json
│   │   │       │       ├── volunteer.py
│   │   │       ├── controllers.py
│   │   │       ├── rest_api.py
│   │   │       └── services.py
│   │   └── tests/
│   │       └── test_volunteer_management.py
└── frontend/
    ├── package.json
    ├── public/
    │   └── index.html
    └── src/
        ├── config/        // Frappe app configuration
        ├── index.js
        ├── App.js
        ├── api.js
        └── components/
            ├── VolunteersList.js
            └── CreateVolunteer.js
```

---
## 4. Environment Variables

| Variable Name        | Description                                               | Default Value     |
|----------------------|-----------------------------------------------------------|-------------------|
| `DB_HOST`            | Host address of the PostgreSQL server                     | `localhost`       |
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
## 5. Running the Application Locally

### 5.1 Prerequisites

- **Python 3.11**
- **Node.js** and **npm** (for front-end assets)
- **Redis** installed locally or accessible
- **PostgreSQL** installed locally or accessible
- **Bench CLI** (Frappe/ERPNext)
- **Git** installed

### 5.2 Steps

1. **Install required Python packages**:

```bash
pip install -r requirements.txt
```

2. **Build and Run the Docker Image**:

```bash
docker-compose build
docker-compose up -d
docker ps
docker exec -it frappe-backend bash
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

5. **Exit the Container**:

```bash
exit
```

6. **Access the site at**:

```bash
http://localhost:8000
```

7. **Install dependencies and start the dev server for React Front-End**:

```bash
npm install
npm start
```

8. **Access the front-end in your browser at**:

```bash
http://localhost:3000
```

### 5.3 Testing the Application

1. **Test PostgreSQL Connection**:

Inside the PostgreSQL container:

```bash
docker exec -it postgres-db bash
psql -U frappe_user -d erpnext
```

Run SQL Queries:

```bash
\dt  -- List tables
\q   -- Exit
```

2. **Test Redis Connection**:

Inside the Redis container:

```bash
docker exec -it redis-cache redis-cli
```

Test a key-value pair:

```bash
set test_key "hello_world"
get test_key
```

3. **Use Postman or CURL to test the REST endpoints**:

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
## 6. Deploying to AWS

### 6.1 Infrastructure Setup

1. **EC2 Instances**: Host Frappe/ERPNext with multiple workers.
2. **RDS (PostgreSQL)**: Managed DB for high availability.
3. **ElastiCache (Redis)**: Managed Redis for caching sessions, data.
4. **Load Balancer (ELB or ALB)**: Distribute traffic to multiple EC2 instances.
5. **S3 (optional)**: For file backups, static assets.

### 6.2 Deployment Steps

1. Provision an EC2 instance and install Bench, Frappe, Python, Redis CLI.
2. Connect EC2 instance to your RDS and ElastiCache instances (update .env).
3. Clone this repo on EC2 and install dependencies (pip install -r requirements.txt).
4. Install Frappe/ERPNext apps on your bench environment.
5. Set up Supervisor or Systemd to run Bench processes in the background.
6. Configure Nginx with a domain or subdomain pointing to your instance.
7. Scale horizontally by adding more EC2 instances behind a Load Balancer if traffic demands it.

---
## 7. License

*This project is licensed under the MIT License.*
