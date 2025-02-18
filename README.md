# Customer Churn Prediction

## 📌 Project Overview
This project is a **Customer Churn Prediction System** built using **Machine Learning** and deployed via **Flask**. The application allows users to input customer details and predicts whether they are likely to churn or not, helping businesses take proactive measures to retain customers.

## 🔧 Tech Stack
- **Programming Language**: Python
- **Framework**: Flask
- **Machine Learning**: Scikit-learn
- **Frontend**: HTML, CSS
- **Data Handling**: Pandas, NumPy
- **Model Deployment**: Joblib

## 📂 Project Structure
```
Customer-Churn-Prediction/
│-- static/
│   ├── style.css
│-- templates/
│   ├── index.html
│-- churn.py  (Main Flask App)
│-- churn_model.joblib  (Trained ML Model)
│-- requirements.txt  (Project Dependencies)
│-- README.md  (Project Documentation)
```

## 🚀 How to Run the Project

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/yourusername/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### 2️⃣ **Create a Virtual Environment** (Recommended)
```sh
python -m venv myenv
source myenv/bin/activate   # For macOS/Linux
myenv\Scripts\activate      # For Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 4️⃣ **Run the Flask App**
```sh
python churn.py
```
The application will be available at **http://127.0.0.1:5000/**.

## 🎯 Features
✅ **User Input Form** – Enter customer data via a web interface.  
✅ **ML Model Prediction** – Uses a trained model to predict churn.  
✅ **Flask Web App** – Lightweight, easy-to-use interface.  
✅ **Real-time Results** – Predicts and displays results instantly.  

## 📊 Machine Learning Model
- **Algorithm Used**: VotingClassifier(Logistic Regression + RandomForestClassifier)
- **Training Data**: Customer data including tenure, billing, contract type, etc.
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score
- **Model Accuracy**: **91.76%**

## 📝 Example Input & Output
**Input Features:**
- Senior Citizen: 0
- Partner: 1
- Dependents: 0
- Tenure: 12 months
- Monthly Charges: $70

**Predicted Output:** ✅ **No Churn**

## 🚀 Deployment Steps
### 1️⃣ **Prepare the Environment**
Ensure you have Python and the required dependencies installed.

### 2️⃣ **Run the Flask App Locally**
```sh
python churn.py
```

### 3️⃣ **Deploy on Heroku**
#### Install Heroku CLI
```sh
npm install -g heroku
```

#### Login to Heroku
```sh
heroku login
```

#### Create a Heroku App
```sh
heroku create your-app-name
```

#### Push to Heroku
```sh
git add .
git commit -m "Initial commit"
git push heroku main
```

#### Scale the App
```sh
heroku ps:scale web=1
```

#### Open the Deployed App
```sh
heroku open
```

## 🛠 Future Improvements
- Deploy on **Heroku/AWS** for public access.
- Improve model with **deep learning** or **ensemble techniques**.
- Add **data visualization** to show customer insights.

## 🤝 Contributing
Feel free to contribute by submitting a pull request. For major changes, please open an issue first.

