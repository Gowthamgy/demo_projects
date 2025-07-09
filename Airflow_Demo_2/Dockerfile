# Use official Airflow image
FROM apache/airflow:2.9.2-python3.10

# Install system dependencies
USER root
RUN apt-get update && apt-get install -y gcc libmysqlclient-dev

# Switch back to airflow user
USER airflow

# Copy your Scrapy project
COPY ./scraper /opt/airflow/scraper

# Install Python dependencies
RUN pip install scrapy mysql-connector-python mysqlclient

# Optional: Set PYTHONPATH globally so 'scraper' is always discoverable
ENV PYTHONPATH="/opt/airflow:${PYTHONPATH}"
