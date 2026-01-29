# 01. Import required libraries
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# 02. Page Configuration
st.set_page_config(
    page_title="AI Student Performance Predictor",
    layout="centered"
)


# 03. Title Section
st.title("🎓 AI-Based Student Performance Prediction")
st.subheader("Helping Faculty Identify At-Risk Students Early")


# 04. Load Dataset
df = pd.read_csv("student data.csv")

st.markdown("### 📊 Student Academic Dataset")
st.dataframe(df)


# 05. Encode Target Variable
df["Final_result"] = df["Final_result"].map({
    "Pass": 1,
    "Fail": 0
})


# 06. Feature Selection
X = df[[
    "Attendance",
    "Internal marks",
    "Assignment",
    "Quize _score"
]]
y = df["Final_result"]


# 07. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 08. Train Model
model = LogisticRegression()
model.fit(X_train, y_train)


# 09. Model Accuracy
accuracy = accuracy_score(y_test, model.predict(X_test))
st.success(f"✅ Model Accuracy: {round(accuracy * 100, 2)}%")


# 10. Prediction Section
st.markdown("---")
st.header("✏️ Predict Student Performance")

attendance = st.slider("Attendance (%)", 0, 100, 75)
internal = st.slider("Internal Marks", 0, 100, 65)
assignment = st.slider("Assignment Score", 0, 100, 70)
quiz = st.slider("Quiz Score", 0, 100, 60)


# 11. Prediction Button
if st.button("🔍 Predict Result"):
    prediction = model.predict(
        [[attendance, internal, assignment, quiz]]
    )

    if prediction[0] == 1:
        st.success("🎉 Student is likely to PASS")
    else:
        st.error("⚠️ Student is AT RISK (Needs Attention)")


# 12. Visualization Section
st.markdown("---")
st.header("📈 Attendance vs Performance")

fig, ax = plt.subplots()
ax.scatter(df["Attendance"], df["Final_result"])
ax.set_xlabel("Attendance")
ax.set_ylabel("Result (1 = Pass, 0 = Fail)")
st.pyplot(fig)


# 13. Footer
st.markdown(
    "💡 *This AI system supports faculty decision-making. "
    "It does not replace academic judgment.*"
)
