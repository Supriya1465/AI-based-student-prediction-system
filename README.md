AI-Based Student Performance Prediction System
📌 Project Overview

The AI-Based Student Performance Prediction System is a machine learning web application that predicts whether a student is likely to Pass or is At Risk based on academic parameters such as attendance, internal marks, assignments, and quiz scores.
This system helps faculty identify struggling students early and take corrective actions.

🎯 Objectives

To analyze student academic data using machine learning

To predict student performance (Pass / Fail)

To assist faculty in early identification of at-risk students

To provide a simple and interactive prediction interface

🧠 Technology Used

Programming Language: Python

Framework: Streamlit

Machine Learning Algorithm: Logistic Regression

Libraries:

pandas

scikit-learn

matplotlib

📂 Dataset Description

The dataset (student data.csv) contains the following attributes:

Column Name	Description
Attendance	Attendance percentage
Internal marks	Internal assessment marks
Assignment	Assignment score
Quiz_score	Quiz score
Final_result	Pass / Fail
⚙️ Methodology

Load and display the student dataset

Encode the target variable (Pass = 1, Fail = 0)

Select relevant academic features

Split data into training and testing sets

Train Logistic Regression model

Evaluate model accuracy

Predict student performance using user inputs

Visualize attendance vs performance

🖥️ Application Features

Interactive sliders for student input

Real-time prediction results

Model accuracy display

Data visualization using graphs

Simple and user-friendly interface

📊 Output

Pass: Student is likely to succeed

At Risk: Student requires academic attention

🚀 How to Run the Project

Install required libraries:

pip install streamlit pandas scikit-learn matplotlib


Place student data.csv in the project folder

Run the application:

streamlit run app.py


Open the browser and use the app

✅ Conclusion

This AI-based system provides a reliable and efficient way to predict student performance using machine learning. It supports academic decision-making and improves early intervention strategies in educational institutions.