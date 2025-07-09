
# Airflow + Scrapy + MySQL Data Pipeline Project 🚀

This project demonstrates a complete, containerized data pipeline using:

✅ **Apache Airflow** - Workflow orchestration  
✅ **Scrapy** - Web scraping framework  
✅ **MySQL** - Database for data storage  
✅ **Docker & Docker Compose** - Containerized deployment  

---

## 📁 Project Structure

```
.
├── dags/               # Airflow DAGs
├── scraper/            # Scrapy project with spiders and settings
├── plugins/            # Airflow plugins (optional)
├── logs/               # Airflow logs
├── docker-compose.yaml # Docker Compose configuration
├── Dockerfile          # Docker image setup
├── .env                # Environment variables (DO NOT COMMIT real credentials)
├── scrapy.cfg          # Scrapy configuration file
└── README.md           # Project documentation
```

---

## ⚡ Quick Start Guide

### 1️⃣ Clone the repository
```bash
git clone <your-repository-url>
cd <your-project-directory>
```

### 2️⃣ Build & Run Containers
```bash
docker-compose up --build
```

### 3️⃣ Access Airflow Web Interface
- URL: [http://localhost:8080](http://localhost:8080)
- Default credentials:
  ```
  Username: airflow
  Password: airflow
  ```

---

## 🐍 Scrapy Spider

Your Scrapy spider is located here:
```
scraper/spiders/sample.py
```

**Manual Run Example (inside container):**
```bash
docker exec -it <scraper-container-name> scrapy crawl sample
```

---

## 🗄️ MySQL Database

**Default Configuration:**
- Host: `localhost`
- Port: `3306`
- Username, Password: Configured via `.env` file

**Note:** `.env` file contains sensitive credentials. Do **NOT** push real `.env` to public repositories.

---

## ⏰ Airflow DAG

The DAG is located in:
```
dags/mysql_example_dag.py
```

**Responsibilities:**
- Runs Scrapy spider  
- Processes scraped data  
- Inserts results into MySQL  

---

## 💻 Requirements

Ensure you have:
- Docker  
- Docker Compose  

All services are containerized; no local Python installation required.

---

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
