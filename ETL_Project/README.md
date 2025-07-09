# 🚀 ETL Pipeline with Apache Airflow & MySQL (Dockerized)

This project implements an **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow**, **Docker**, and **MySQL**. The pipeline extracts data from an API, processes it, and loads it into a MySQL database.

---

## 📁 Project Structure

```
├── docker-compose.yaml # Docker Compose file for Airflow & MySQL
├── Dockerfile # Optional custom Docker build for Airflow
├── .gitignore # Git ignore rules
│
├── dags/
│ └── test_dag.py # Airflow DAG to orchestrate ETL flow
│
├── ETL/
│ ├── config/
│ │ └── mysql_config.py # MySQL connection settings
│ ├── extract/
│ │ └── extract_api.py # Extract data from an external API
│ └── load/
│ └── load_to_mysql.py # Load data into MySQL
│
├── logs/ # Airflow logs (ignored by Git)
└── plugins/ # Optional Airflow plugins
```

---

## 🛠️ Prerequisites

Make sure the following are installed on your machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

---

Configure MySQL Settings

```
Edit the file ETL/config/mysql_config.py with your MySQL credentials:

```
MYSQL_CONFIG = {
    "user": "root",
    "password": "122877",
    "host": "host.docker.internal",
    "port": 3306,
    "database": "example"
}

```
✅ Note: host.docker.internal is used to connect from a Docker container to your host system (for local MySQL).

---

🐳 Run with Docker

```
Start Airflow and (optionally) MySQL via Docker:
```
docker-compose up --build

---

▶️ Run the ETL DAG

- Open the Airflow UI.
- Locate test_dag in the DAG list.
- Turn it "On" and click the "Play" (▶) button to trigger it.

The pipeline will:
- Extract data from an API (extract_api.py)
- Optionally transform it
- Load the result into MySQL (load_to_mysql.py)
- Load the result into MySQL (load_to_mysql.py)

---

🙌 Credits

## 🙋 About Me

- **Name:** Gowtham  
- **LinkedIn:** [Your LinkedIn](https://www.linkedin.com)  
- **GitHub:** https://github.com/Gowthamgy/workspace/ 
- **Email:** gowthamjohn7@gmail.com.com  

---

## ⚠️ Notes

- Keep `.env` file secure, with real credentials only in your local environment.  
- Adjust configurations like Airflow schedules, MySQL settings as per your needs.  
- Contributions or suggestions are welcome!  

---

**Thank you for exploring this project!**



