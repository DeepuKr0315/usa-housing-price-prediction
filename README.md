# **USA Housing Price Prediction** 🏡💸

**USA Housing Price Prediction** is a machine learning project that uses a dataset of real estate listings in the United States to predict housing prices based on various features such as the number of bedrooms, bathrooms, house size, and location. The project utilizes **Linear Regression** and **Streamlit** for the user interface to make the prediction process interactive.

## **Project Overview** 📊

This project is aimed at understanding housing price trends and predicting house prices in the United States using historical real estate data.

The dataset is sourced from [Kaggle - USA Real Estate Dataset](https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset), which contains over **2.2 million listings** of real estate properties. Using this dataset, we built a **Linear Regression** model to predict housing prices based on features such as:

- **Number of Bedrooms** 🛏️
- **Number of Bathrooms** 🚿
- **House Size** (in square feet) 📏
- **Location** (state, city, zip code) 📍

The project is made interactive using **Streamlit** where users can input property details and get price predictions instantly.

## **Project Structure** 📂

The project directory contains the following files:

- `app.py`: The main file that runs the Streamlit app.
- `model.pkl`: The trained machine learning model (Linear Regression).
- `Scaler.pkl`: The scaler used to normalize input features before prediction.
- `realtor-data.csv`: The dataset used for training the model.
- `requirements.txt`: List of dependencies required to run the project.

## **Installation** ⚙️

### To run this project locally, follow these steps:

**1. Clone the repository:**
   - `git clone https://github.com/DeepuKr0315/usa-housing-price-prediction.git`
   - `cd usa-housing-price-prediction`
   
**2. Create a virtual environment and activate it:**
    `python -m venv venv`
    
    # On Windows
    venv\Scripts\activate
    
    # On macOS/Linux
    source venv/bin/activate
 
**3. Install the dependencies:**
    `pip install -r requirements.txt`

**4. Run the app:**
    `streamlit run app.py`
    
**5. Open your browser and go to http://localhost:8501 to interact with the app.**
