<div align="center">

# 📊 Employee Attrition Prediction System

### Machine Learning for HR Analytics: predict who is likely to leave, before they do

*A full-stack machine learning web application that predicts employee attrition risk and presents insights through an interactive dashboard.*



![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)




![Flask](https://img.shields.io/badge/Flask-Backend-000000?logo=flask&logoColor=white)




![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)




![Pandas](https://img.shields.io/badge/Pandas-Data-150458?logo=pandas&logoColor=white)




![Chart.js](https://img.shields.io/badge/Chart.js-Visualisation-FF6384?logo=chartdotjs&logoColor=white)



[📧 Hire Me](mailto:samarthworldwide@gmail.com) · [💼 LinkedIn](https://www.linkedin.com/in/samarth-shukla-b72003293) · [🐙 GitHub](https://github.com/Samarth7272)

</div>

---

## 🎯 The Problem

Employee turnover is expensive. Losing experienced people raises recruitment costs, hurts productivity and adds workload to the rest of the team. Most HR teams still find out *after* someone resigns.

**This project flips that.** It uses employee data such as job satisfaction, salary, work environment, experience and demographics to predict whether an employee is likely to leave. HR teams can then act early.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔮 **Attrition prediction** | Predicts whether an employee is likely to leave or stay |
| 🧠 **Trained ML model** | Model trained in `model.py`, saved as `employee_attrition_model.pkl` and loaded by the web app |
| 🌐 **Flask backend** | Handles requests and connects the model to the web interface |
| 📊 **Interactive dashboard** | Shows attrition insights and visual analytics with Chart.js |
| 🧹 **Data processing** | Cleans and prepares employee data for modelling |
| 📱 **Responsive UI** | Clean, user-friendly interface built with HTML5, CSS3 and JavaScript |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application development |
| **Flask** | Backend and web application |
| **Scikit-learn** | Machine learning model |
| **Pandas** | Data processing |
| **NumPy** | Numerical operations |
| **Joblib** | Model serialisation |
| **HTML5 / CSS3** | Frontend structure and styling |
| **JavaScript** | Frontend interactions |
| **Chart.js** | Data visualisation |

---

## 🧠 Machine Learning Workflow

1. Load the employee dataset
2. Preprocess and prepare the data
3. Select features and prepare model inputs
4. Train the machine learning model
5. Save the trained model (`.pkl`)
6. Load the model into the Flask application
7. Generate attrition predictions
8. Display results and visual insights on the dashboard

---

## 🏗️ System Architecture

```
   EMPLOYEE DATASET
          │
          ▼
   DATA PREPROCESSING
          │
          ▼
    ML MODEL TRAINING
          │
          ▼
  TRAINED MODEL (.pkl)
          │
          ▼
     FLASK BACKEND
          │
          ▼
    WEB APPLICATION
          │
          ▼
  PREDICTION DASHBOARD
          │
          ▼
      HR ANALYTICS
```

---

## 📁 Project Structure

```
Algonive_Employee_Attrition_Prediction_System/
├── dataset/                       Employee data
├── static/                        CSS, JavaScript, assets
├── templates/                     HTML pages
├── app.py                         Flask application
├── model.py                       Model training script
├── employee_attrition_model.pkl   Trained model
└── README.md
```

---

## 🚀 Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/Samarth7272/Algonive_Employee_Attrition_Prediction_System.git
cd Algonive_Employee_Attrition_Prediction_System

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Linux / macOS

# 3. Install dependencies
pip install flask scikit-learn pandas numpy joblib

# 4. (Optional) Retrain the model
python model.py

# 5. Run the application
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

---

## 📈 Business Applications

- **HR analytics:** understand why employees leave
- **Retention planning:** spot at-risk employees early
- **Workforce management:** plan hiring and succession
- **Organisational data analysis:** find patterns across teams
- **Predictive business intelligence:** turn data into decisions

> ⚠️ **Important:** Predictions are intended to support analysis and should not be used as the sole basis for employment decisions.

---

## 🎓 What This Project Demonstrates

- Building an **end-to-end ML pipeline**: data → model → deployment
- **Model serialisation** and loading inside a web application
- **Flask backend** development with frontend integration
- **Data visualisation** for non-technical stakeholders
- Clean project structure, debugging, testing and **Git/GitHub** workflow

---

## 🔮 Future Enhancements

- Compare multiple algorithms (Random Forest, XGBoost, Logistic Regression) and report accuracy, precision and recall
- Add Explainable AI (SHAP) to show *why* an employee is flagged
- Advanced HR analytics dashboard
- Secure user authentication
- Cloud deployment (Render / Railway / AWS)
- Automated model monitoring

---

## 👨‍💻 About the Author

**Samarth Shukla**: Final-year B.Tech Computer Science student and Software Engineer Intern at LV8 Tech, working on REST API design, OAuth 2.0 and backend architecture for fintech integrations (Next.js, TypeScript, PostgreSQL).

**Skills:** Python · JavaScript/TypeScript · FastAPI · Flask · React/Next.js · SQL · PyTorch · scikit-learn · Docker · AWS · Git

### 💼 Open to Opportunities

I'm actively looking for **Software Engineer, Backend, Full-Stack and AI/ML** roles (full-time and internships). If this project impressed you, I'd love to talk.

[

![Email](https://img.shields.io/badge/Email-samarthworldwide%40gmail.com-D14836?logo=gmail&logoColor=white)

](mailto:samarthworldwide@gmail.com)
[

![LinkedIn](https://img.shields.io/badge/LinkedIn-Samarth%20Shukla-0A66C2?logo=linkedin&logoColor=white)

](https://www.linkedin.com/in/samarth-shukla-b72003293)
[

![GitHub](https://img.shields.io/badge/GitHub-Samarth7272-181717?logo=github&logoColor=white)

](https://github.com/Samarth7272)

📧 **Contact:** samarthworldwide@gmail.com

---

<div align="center">

⭐ If you found this project useful, please give it a star!

*Built as part of the Algonive Data Science Internship.*

</div>
