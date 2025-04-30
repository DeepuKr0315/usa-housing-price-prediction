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

- **`app.py`**: This file contains the user interface where users can input their data, trigger predictions, and view the results in real-time.
- **`model.pkl`**: The trained **machine learning model** (Linear Regression). This file contains the saved model that is used to make predictions on the real estate prices based on user inputs.
- **`Scaler.pkl`**: The **scaler** used to normalize input features before making predictions. It ensures that the data is scaled properly for the trained model, which improves its performance and accuracy.
- **`realtor-data.csv`**: The **dataset** used for training the model. This dataset contains various real estate listings, including features like price, number of bedrooms, bathrooms, house size, and more. It is used for training the **Linear Regression model** to predict housing prices based on these features.
- **`untitled.ipynb`**: The **Jupyter notebook** where the model was trained and initial data cleaning was performed. This file contains the steps of preprocessing the data, training the model, and saving it for later use in the app. You can explore the entire workflow, from data preparation to model creation.

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


# Project Description 📊🏠

This project is a **Real Estate Price Prediction App** built using **Streamlit** and a **Linear Regression** model. It predicts the price of a house based on user inputs such as the number of bedrooms, bathrooms, and the size of the house.

The app uses a trained machine learning model, saved as `model.pkl`, to make predictions. The model was trained on the USA Real Estate dataset (available on Kaggle) containing listings of homes across the United States. The app is designed to provide real-time price predictions and can be easily hosted and shared for public use.

You can try the app live on [Streamlit here](http://localhost:8501/). It provides an interactive user interface for real-time predictions. The model was built, trained, and saved in the `untitled.ipynb` file, which includes the steps of data cleaning, feature engineering, and model training.
