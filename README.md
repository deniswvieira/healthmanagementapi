# 🏥 FHIR REST API - Health Management

This project is a **FHIR-compliant RESTful API** built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**. It provides endpoints for **patient CRUD operations**, authentication via **JWT**, **Swagger and Redoc documentation**

🚀 **The API is hosted on Railway and can be accessed at:**

[🔗 FHIR API on Railway](https://healthmanagementapi-production.up.railway.app/)

## 📖 **API Documentation**

The interactive API documentation is available at:

- **Swagger UI**: [🔗 /swagger/](https://healthmanagementapi-production.up.railway.app/swagger/)
- **ReDoc**: [🔗 /redoc/](https://healthmanagementapi-production.up.railway.app/redoc/)

All endpoints follow the **FHIR Patient** format, ensuring compatibility with medical systems.

## 📈 **View Code Coverage on Codecov**
The test coverage results are uploaded to **Codecov** for better visualization and tracking.

To see the coverage report, visit:
[🔗 Codecov Report](https://app.codecov.io/gh/deniswvieira/healthmanagementapi)

## 💻 **Development Setup**

This project uses **Poetry** for dependency management and enforces code quality with **Commitlint, Black, Flake8, and isort**.

### 🛠 **1. Prerequisites**

Ensure you have the following installed:
- **Python 3.10+**
- **Poetry**
- **PostgreSQL**
- **Node.js** and **npm** (required for Commitlint)

### 📦 **2. Install Dependencies**
```sh
# Clone the repository
git clone git@github.com:deniswvieira/healthmanagementapi.git
cd healthmanagementapi

# Install Python dependencies
poetry install

# Install Commitlint dependencies
npm install
```

### 📜 **3. Run Migrations**
```sh
poetry run python manage.py migrate
```

### 🚀 **4. Start the Server**
```sh
poetry run python manage.py runserver
```
The API will now be available at **http://127.0.0.1:8000/** 🎉


## 🧪 **Running Tests with Coverage**

### ✅ **Run All Tests**
```sh
poetry run pytest
```

### 📊 **Generate Coverage Report**
```sh
poetry run pytest --cov=patients --cov-report=term-missing
```
This will display which parts of the code are covered (or not covered) by tests.


## 🔍 **Code Quality and Linting**

This project follows strict code quality standards using **Python Black, Flake8, and isort**.

### 🎨 **Format Code with Black**
```sh
poetry run black .
```

### 🔍 **Check Code Style with Flake8**
```sh
poetry run flake8 .
```

### 📌 **Organize Imports with isort**
```sh
poetry run isort .
```

We provide the `vscode` configuration for handling this formatters and linters on file save.

### ✅ **Commitlint - Enforcing Commit Message Standards**
To ensure standardized commit messages, we use **Commitlint**.

⚠ **You must run `npm install` in the root directory to use it!**

### 🔒 Pre Commit validations
Before any commit is validated, we run pre-commit validations for commitlint, black and flake8.
If any of this tools fails, the commit is not applied.


## 🚀 **Deploying on Railway**

The project is **hosted on Railway**, allowing continuous deployment of the API. It is configured to automatically build and deploy `main` commits **if the pipeline succeeds.**

🔗 **Access the API on Railway:** [https://healthmanagementapi-production.up.railway.app/](https://healthmanagementapi-production.up.railway.app/)


## 🔮 **Next Steps and Improvements**

🔹 **Integrate SonarQube** for code quality analysis and test coverage reports.

🔹 **Implement monitoring with Prometheus & Grafana** for API performance metrics.

🔹 **Set up centralized logging with Kibana** for better debugging and auditing.

🔹 **Branching and Pull Requests** with GitHub.

🔹 **Build a Postman collection** for a better development experience.


## 📝 **License**
This project is **closed-source** and cannot be distributed or modified without authorization.

📌 **Created by:** Denis Vieira - [LinkedIn](https://www.linkedin.com/in/deniswvieira)
