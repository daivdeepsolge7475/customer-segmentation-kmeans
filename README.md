# 🛍️ Customer Segmentation using K-Means Clustering

A Machine Learning project that segments mall customers into different groups based on their **Annual Income** and **Spending Score** using the **K-Means Clustering** algorithm. The project also includes an interactive **Streamlit Web Application** for predicting customer segments.

---

## 📌 Project Overview

Customer segmentation is an important business strategy that helps companies understand customer behavior and create targeted marketing campaigns.

In this project, the K-Means Clustering algorithm groups customers with similar purchasing behavior into different segments.

The application allows users to enter:

- Annual Income
- Spending Score

and predicts the customer's segment along with a business recommendation.

---
## Demo link of project

Demo link: https://customer-segmentation-kmeans-nqkzz6dfy8ibu26h76hqzl.streamlit.app/


## 🎯 Problem Statement

Businesses have thousands of customers with different spending habits.

Instead of treating every customer the same, we can group similar customers together to:

- Improve customer satisfaction
- Increase sales
- Create personalized marketing campaigns
- Identify premium customers
- Improve business decision-making

---

## 📂 Dataset

**Dataset:** Mall Customers Dataset

### Features

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

---

## 📊 Exploratory Data Analysis (EDA)

Performed:

- Dataset inspection
- Missing value check
- Duplicate value check
- Statistical summary
- Gender distribution
- Age distribution
- Spending Score distribution
- Annual Income vs Spending Score
- Age vs Spending Score

---

## 🤖 Machine Learning Algorithm

### K-Means Clustering

K-Means is an **Unsupervised Machine Learning Algorithm** used to group similar data points.

Since the dataset has no target labels, clustering is the most suitable technique.

---

## 📈 Elbow Method

The Elbow Method was used to determine the optimal number of clusters.

The optimal value of **K = 5** was selected based on the WCSS curve.

---

## 👥 Customer Segments

The model divides customers into five groups:

- 💎 High Income – High Spending
- 🎯 High Income – Low Spending
- 🌟 Low Income – High Spending
- 💰 Low Income – Low Spending
- 🛒 Regular Customers

Each segment includes business recommendations for marketing purposes.

---

## 🌐 Streamlit Web Application

The application allows users to:

- Enter Annual Income
- Enter Spending Score
- Predict Customer Segment
- View Business Recommendation

---

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/daivdeepsolge7475/customer-segmentation-kmeans.git
```

### Move into Project Folder

```bash
cd customer-segmentation-kmeans
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m streamlit run app.py
```

---

## 📁 Project Structure

```
Customer-Segmentation-KMeans/
│
├── app.py
├── main.py
├── Mall_Customers.csv
├── kmeans_model.pkl
├── requirements.txt
├── README.md
└── .gitignore

---

## 📈 Future Improvements

- Hyperparameter tuning
- Automatic cluster naming
- Interactive visualizations using Plotly
- Customer profile analytics
- Database integration
- Cloud deployment
- REST API using FastAPI

---

## 💼 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Unsupervised Machine Learning
- K-Means Clustering
- Elbow Method
- Model Serialization
- Streamlit Deployment
- Git & GitHub

---

## 👨‍💻 Developer

**Daivdeep Solge**

B.Tech Artificial Intelligence & Data Science Student

Machine Learning | Data Science | Python | SQL | Streamlit

GitHub:
https://github.com/daivdeepsolge7475

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.