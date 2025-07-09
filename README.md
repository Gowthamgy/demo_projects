# 🧠 Apache Airflow Project Collection by Gowthamgy

This repository contains multiple hands-on demo projects focused on **Apache Airflow**, **ETL pipelines**, **Docker**, and **MySQL**. Each project is self-contained and showcases a different aspect of Airflow-based data engineering workflows.

---

## 👨‍💼 Maintained by Gowthamgy

**Role:** Senior Software Engineer  
🔗 [GitHub Profile](https://github.com/Gowthamgy)  
💼 Passionate about backend systems, data engineering, AI automation pipelines, and leveraging tools like ChatGPT to build intelligent workflows and decision-making systems.

---

## 📦 Projects Overview

### 📁 `Airflow_Demo_1`
A simple Apache Airflow setup showcasing:
- Basic DAG creation
- Airflow Scheduler and Web UI
- Running Python-based tasks
- Uses **Docker** to containerize Airflow and services
- scrapy framework
- Loads it into a **MySQL** database

🔗 [See Project ➤](./Airflow_Demo_1)

---

### 📁 `Airflow_Demo_2`
An extended Airflow demo that adds:
- DAG with multiple tasks
- Python function chaining
- Simulated data processing steps
- Uses **Docker** to containerize Airflow and services
- scrapy framework
- Loads it into a **MySQL** database

🔗 [See Project ➤](./Airflow_Demo_2)

---

### 📁 `ETL_Project`
A full ETL pipeline that:
- Extracts data from a public API
- Loads it into a **MySQL** database
- Uses **Docker** to containerize Airflow and services
- Supports GitHub CI/CD for testing

🔗 [See Project ➤](./ETL_Project)

---

## 🛠️ Prerequisites for All Projects

Make sure the following tools are installed and configured on your system:

- [🐳 Docker](https://docs.docker.com/) — For containerizing Airflow, MySQL, and other services
- [📦 Docker Compose](https://docs.docker.com/compose/) — For orchestrating multi-container environments
- [🐍 Python 3.10+](https://www.python.org/) — Some projects support running scripts directly outside Docker
- [🐘 MySQL 8+](https://www.mysql.com/) — Used as the data store in ETL projects
- [🌬️ Apache Airflow 2.9+](https://airflow.apache.org/docs/) — Orchestrates the ETL workflows
- [🧬 Git](https://git-scm.com/) — For version control and CI/CD integration

---

## 🚀 How to Run Any Project

```bash
cd <Project_Folder>
docker-compose up --build
```
