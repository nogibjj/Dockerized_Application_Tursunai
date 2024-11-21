## Data Pipeline with Databricks
### By Tursunai Turumbekova
[![CI](https://github.com/nogibjj/Dockerized_Application_Tursunai/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Dockerized_Application_Tursunai/actions/workflows/cicd.yml)

This project builds upon an earlier PySpark implementation to leverage the Databricks ecosystem. It demonstrates the creation and execution of a Databricks pipeline using PySpark for managing and analyzing datasets. The primary focus of this project is on extracting, transforming, and diving into urbanization metrics data from FiveThirtyEight, utilizing Databricks APIs and Python libraries.

[Demo video](https://youtu.be/afhGBaAZU-A)
## Key Features

1. **Data Extraction**
   - Utilizes the `requests` library to fetch datasets from specified URLs.
   - Stores the extracted data in the Databricks FileStore for further processing.

2. **Databricks Environment Setup**
   - Establishes a connection to the Databricks environment using environment variables for authentication (`SERVER_HOSTNAME` and `ACCESS_TOKEN`).
   - Configures Databricks clusters to support PySpark workflows.

3. **Data Transformation and Load**
   - Converts CSV files into Spark DataFrames for processing.
   - Transforms and stores the processed data as Delta Lake Tables in the Databricks environment.

4. **Query Transformation and Visualization**
   - Performs predefined Spark SQL queries to transform the data.
   - Creates visualizations from the transformed Spark DataFrames to analyze various metrics.

5. **File Path Validation**
   - Implements a function to check if specified file paths exist in the Databricks FileStore.
   - Verifies connectivity with the Databricks API for automated workflows.

6. **Automated Job Trigger via GitHub Push**
   - Configures a GitHub workflow to trigger a job run in the Databricks workspace whenever new commits are pushed to the repository.

## Dockerized Application

This project also includes a Dockerized implementation of the pipeline for local development and deployment. The Docker image can be found on Docker Hub.

### Docker Image

The Docker image for this project is available on Docker Hub:spark-python-app.

### Running the Docker Container Locally

To run the pipeline using Docker, follow these steps:

``` bash
docker pull /spark-python-app:latest
```    
```bash
docker run -it --rm /spark-python-app:latest
```
![Docker](img/docker.png)
## Project Components

### Environment Setup
- Create a Databricks workspace on Azure.
- Connect your GitHub account to the Databricks workspace.
- Set up a global init script for cluster start to store environment variables.
- Create a Databricks cluster that supports PySpark operations.
### Job Run from Automated Trigger:
![Pipeline](img/Runs.png)

### Pipeline Workflow
1. **Data Extraction**
   - **File:** `mylib/extract.py`
   - Retrieves data from the source and stores it in Databricks FileStore.

2. **Data Transformation and Load**
   - **File:** `mylib/transform_load.py`
   - Converts raw data into Delta Lake Tables and loads them into the Databricks environment.

3. **Query and Visualization**
   - **File:** `mylib/query.py`
   - Defines SQL queries and generates visualizations using Spark.

![Pipeline](img/ETL.png)

## Sample Visualizations from Query

![Pipeline](img/plot1.png)
![Pipeline](img/plot2.png)

## Preparation Steps

1. Set up a Databricks workspace and cluster on Azure.
2. Clone this repository into your Databricks workspace.
3. Configure environment variables (`SERVER_HOSTNAME` and `ACCESS_TOKEN`) for API access.
4. Create a Databricks job to build and run the pipeline:
   - **Extract Task:** `mylib/extract.py`
   - **Transform and Load Task:** `mylib/transform_load.py`
   - **Query and Visualization Task:** `mylib/query.py`

## Additional Notes

- This project is specifically designed for use within the Databricks environment. Due to the dependency on Databricks' infrastructure, some functionalities cannot be replicated outside the workspace (e.g., testing data access in a GitHub environment).
- A YouTube video demonstration of the pipeline implementation and data analysis is available for further insight.

## Future Enhancements

- Expand the pipeline to handle additional datasets.
- Integrate advanced visualizations and analytics using tools like Tableau or Power BI.
- Optimize the pipeline for larger datasets and higher computational efficiency.

Feel free to explore, contribute, and reach out with suggestions or questions!

