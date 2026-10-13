# Employee Attrition Predictor 🚀

An end-to-end Machine Learning and web-based application designed to predict employee attrition risk. This tool helps organizations identify employees who are likely to leave, enabling proactive retention strategies.

---

## 🛠️ Tech Stack
* **Programming Language:** Python
* **Machine Learning:** Scikit-learn (Gradient Boosting Classifier), NumPy, Pandas
* **Web Framework:** Flask
* **Frontend:** HTML5, CSS3
* **Version Control:** Git & GitHub

---

## 📊 Features & Model Inputs
The model is trained on key workplace and demographic features to provide accurate predictions:
1. **Age:** Employee's age.
2. **Monthly Income:** Current salary package.
3. **Distance From Home:** Daily commute distance in kilometers.
4. **Overtime:** Whether the employee frequently works overtime (Yes/No).
5. **Marital Status:** Single, Married, or Divorced.

---

## 📂 Project Structure
```text
Employee-Attrition-Predictor/
│
├── static/                # CSS and styling assets
├── templates/
│   └── index.html         # Frontend user interface
├── analysis.ipynb         # Jupyter Notebook for EDA & Model Training
├── app.py                 # Flask backend application
├── model.pkl              # Serialized Gradient Boosting model
└── README.md              # Project documentation
