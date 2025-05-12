# ❤️ Heart Disease Prediction Web App

This project is a **machine learning–powered web application** that predicts the likelihood of heart disease based on medical inputs. Built with **Flask**, it uses a **Decision Tree Classifier** trained on real medical data.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-lightgrey)
![Status](https://img.shields.io/badge/Status-Deployed-green)
![License](https://img.shields.io/badge/License-MIT-lightgreen)

---

## 🚀 Features

- 🧠 ML model (Decision Tree) trained on heart.csv
- 📊 Exploratory Data Analysis included (`main.ipynb`)
- 🌐 Flask-based front-end with clean UI
- ✅ User-friendly form with recommended ranges
- 🎨 Styled with transparent layout and responsive design
- 🔁 Result page shows risk or no-risk with color feedback
- 🔒 Optional `.gitignore` and clean folder structure

---

## 📂 Folder Structure

```
Heart_Disease_Prediction/
├── app.py
├── main.ipynb
├── model.pkl
├── heart.csv
├── prediction_pipeline.py
├── requirements.txt
├── static/
│   └── background.jpg
├── templates/
│   ├── index.html
│   ├── result.html
│   └── error.html
└── README.md
```

---

## 📥 Installation & Run

1. Clone the repo:
   ```bash
   git clone https://github.com/mep3175/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. Create virtual environment and activate:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open in browser:  
   ```
   http://127.0.0.1:5000/
   ```

---

## 🧠 Model Info

- **Model:** DecisionTreeClassifier  
- **Accuracy:** ~87% on test set  
- **Dataset:** 13 medical features  
- **Target:** Presence of heart disease (binary classification)

---

## 🧑‍💻 Author

**Meet Patel**  
🔗 [GitHub Profile](https://github.com/mep3175)  
📧 meetpatel.test@gmail.com

---

## 📄 License

This project is licensed under the MIT License.

---

> 💡 Want to deploy this to the web (Render, HuggingFace, Heroku)? Let me know — I’ll help you do it in 5 minutes.
