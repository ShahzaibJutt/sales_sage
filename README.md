Here is the updated `README.md` file with the additional API endpoints:

---

# Sales Performance Analysis Project

## Overview

This project is designed to load sales data from CSV or JSON files into a SQLite database and perform analysis using LangChain agents. The analysis provides detailed feedback on sales performance metrics, strengths, areas for improvement, and overall evaluation.

## Features

- Load data from CSV or JSON files into a SQLite database.
- Analyze sales data using LangChain agents.
- Provide detailed feedback on sales performance.
- View intermediate steps and logs for detailed insights.
- Developed using Django, Python, and LangChain.

## Setup

### Step 1: Define the Environment File

Create a `.env` file in the root directory of the project with the following content:

```env
DATA_FILE_PATH=sales_performance_data.csv
DATABASE_URL=salesdata.db
OPENAI_API_KEY=your-openai-api-key
OPENAI_MODEL_NAME=gpt-3.5-turbo
```

Replace `your-openai-api-key` with your actual OpenAI API key.

### Step 2: Install Dependencies

Make sure you have `Poetry` installed. Then, install the required dependencies:

```sh
poetry install
```

### Step 3: Load Data

To load data into the SQLite database, run the following command:

```sh
poetry run python manage.py import_data
```

The data file specified in the `.env` file (either CSV or JSON) will be loaded into the SQLite database.

### Step 4: Run the Django Server

Start the Django development server:

```sh
poetry run python manage.py runserver
```

## API Endpoints

### Individual Sales Representative Performance Analysis

- **Endpoint:** `/api/rep_performance`
- **Method:** `GET`
- **Parameters:** `rep_id` (unique identifier for the sales representative)
- **Description:** Returns detailed performance analysis and feedback for the specified sales representative.

### Overall Sales Team Performance Summary

- **Endpoint:** `/api/team_performance`
- **Method:** `GET`
- **Description:** Provides a summary of the sales team’s overall performance.

### Sales Performance Trends and Forecasting

- **Endpoint:** `/api/performance_trends`
- **Method:** `GET`
- **Parameters:** `time_period` (e.g., monthly, quarterly)
- **Description:** Analyzes sales data over the specified time period to identify trends and forecast future performance.

## Architecture

1. **Data Loading:** The project loads sales data from a specified CSV or JSON file into a SQLite database.
2. **Analysis:** Uses LangChain agents to perform detailed analysis on the loaded data.
3. **Response:** Provides detailed feedback in the API response. For more insights, you can check the intermediate steps logged in the console.

## Logging

File-level logging is configured to capture detailed logs of the operations performed by the project.

## Technologies Used

- **Django:** Web framework for building the backend server.
- **Python:** Programming language used for development.
- **LangChain:** Used for building agents that perform data analysis.

## Conclusion

This project provides a comprehensive solution for loading, analyzing, and providing feedback on sales data. The use of LangChain agents ensures detailed and actionable insights, making it a valuable tool for sales performance analysis.

---