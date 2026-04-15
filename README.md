# 🚀 Salary Prediction using Machine Learning (AWS + Docker + CI/CD)

## 📌 Project Overview
This project is a Machine Learning API that predicts house price based on input features like area, bedrooms, and bathrooms.  
The model is deployed using Flask, Docker, and AWS EC2 with CI/CD integration.

---

## 🧠 Tech Stack
- Python
- Flask
- Scikit-learn
- Docker
- AWS EC2
- GitHub
- Jenkins
- Nginx

---

## 📂 Project Structure
.
├── app.py  
├── model.py  
├── model.pkl  
├── house_price_dataset.csv  
├── requirements.txt  
├── Dockerfile  
└── README.md  

---

## ⚙️ How It Works
1. Train model using model.py  
2. Save model as model.pkl  
3. Flask API loads model  
4. API endpoint /predict returns prediction  
5. Docker container runs the app  
6. AWS EC2 hosts the application  

---

## 🚀 API Endpoint

### POST /predict

Request:
```json
{
  "area": 2000,
  "bedrooms": 3,
  "bathrooms": 2
}
