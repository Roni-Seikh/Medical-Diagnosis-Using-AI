```markdown
# Medical Diagnosis Using AI

This project leverages machine learning models to predict medical conditions such as diabetes, heart disease, Parkinson's disease, hypothyroidism, lung cancer, and thyroid issues based on user inputs. The system is designed to aid healthcare professionals in providing quick predictions and support decision-making.

## Table of Contents
- [Description](#description)
- [Technologies Used](#technologies-used)
- [Models](#models)
- [Setup](#setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Description
This application provides an easy-to-use interface for predicting medical conditions. It uses various machine learning models that have been trained on relevant datasets to make accurate predictions. The goal is to assist healthcare professionals with quicker diagnostic processes.

### **Key Features:**
- **Diabetes Prediction**: Predicts the likelihood of diabetes based on patient data.
- **Heart Disease Prediction**: Identifies the risk of heart disease.
- **Parkinson's Disease Prediction**: Detects early-stage Parkinson's disease.
- **Lung Cancer Prediction**: Assists in predicting lung cancer risk.
- **Thyroid Prediction**: Predicts thyroid conditions using medical inputs.

## Technologies Used
- **Python**: Programming language used for the development.
- **Scikit-learn**: Machine learning library used for model training.
- **Flask/Streamlit**: Web framework used for deploying the application.
- **Pandas, NumPy**: Libraries for data manipulation and analysis.
- **Matplotlib, Seaborn**: Data visualization libraries.
- **Joblib**: Model serialization.

## Models
The following models have been developed and saved as `.sav` files:
- **Diabetes Model**: `diabetes_model.sav`
- **Heart Disease Model**: `heart_disease_model.sav`
- **Parkinson's Disease Model**: `parkinsons_model.sav`
- **Lung Disease Model**: `lungs_disease_model.sav`
- **Thyroid Model**: `thyroid_model.sav`

These models use historical medical data to predict the likelihood of the disease based on user input.

## Setup
### Prerequisites:
1. Python 3.x installed on your system.
2. Git for version control.

### Clone the repository:
```bash
git clone https://github.com/Roni-Seikh/Medical-Diagnosis-Using-AI.git
cd Medical-Diagnosis-Using-AI
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the app by executing the following command:
```bash
streamlit run app.py
```
2. Follow the instructions in the app to enter data for prediction.

## Screenshots
Here are some screenshots of the application in action:

![Diabetes Prediction](https://github.com/Roni-Seikh/Medical-Diagnosis-Using-AI/blob/main/screenshots/Diabetes%20Prediction.png)
![Heart Disease Prediction](https://github.com/Roni-Seikh/Medical-Diagnosis-Using-AI/blob/main/screenshots/Heart%20Disease%20Prediction.png)
![Lung Cancer Prediction](https://github.com/Roni-Seikh/Medical-Diagnosis-Using-AI/blob/main/screenshots/Lung%20Cancer%20Prediction.png)
![Parkinson's Prediction](https://github.com/Roni-Seikh/Medical-Diagnosis-Using-AI/blob/main/screenshots/Parkinson's%20Prediction.png)
![Thyroid Prediction](https://github.com/Roni-Seikh/Medical-Diagnosis-Using-AI/blob/main/screenshots/Thyroid%20Prediction.png)

## Contributing
Feel free to fork this repository and submit pull requests with improvements. Contributions are welcome!

### Steps to contribute:
1. Fork the repository.
2. Clone your fork to your local machine.
3. Make necessary changes and create a pull request with a description of your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---

### 🎉 Now your README will display the images directly from your GitHub repository! Just make sure you push the updated `README.md` to your repo.

Let me know if you need further assistance with anything else. 🚀
