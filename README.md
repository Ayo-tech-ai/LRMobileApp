# Marketing Sales Predictor

This project is a simple end-to-end machine learning deployment project. It uses a linear regression model to predict expected sales from TV advertising spend.

The main goal of the project is not just to build a regression model, but to take the model through a full deployment workflow:

```text
Data analysis -> TensorFlow model -> TensorFlow Lite model -> Streamlit web app -> Android mobile app
```

The model was first explored using ordinary least squares regression, then rebuilt as a TensorFlow model, converted to TensorFlow Lite, tested in a Streamlit web application, and finally integrated into a mobile app built with Android Studio.

---

## Project Overview

The app predicts `Sales` from a single input:

```text
TV advertising spend
```

Example:

```text
Input: 50
Output: Predicted Sales: 177.86
```

The prediction is made by running an actual TensorFlow Lite model file:

```text
marketing_sales_model.tflite
```

The app does not manually calculate the regression equation in the frontend. Instead, it loads the saved `.tflite` model and runs inference using the model.

---

## Dataset

The dataset contains marketing spend and sales data with the following columns:

```text
TV
Radio
Social_Media
Sales
```

Initial analysis showed that `TV` had the strongest relationship with `Sales`.

The simple OLS regression equation was approximately:

```text
Sales = -0.1325 + 3.5615 * TV
```

The TensorFlow model learned a very similar relationship:

```text
Sales = -0.2735 + 3.5627 * TV
```

---

## Model Performance

The TensorFlow model was trained and tested using a train/test split.

Final test performance:

```text
Test MAE: about 2.31
```

This means the model's predictions were off by about 2.31 sales units on average.

The TensorFlow Lite model was also tested directly, and it produced the same expected result:

```text
TV Spend: 50
TFLite Predicted Sales: 177.85913
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Statsmodels
- Scikit-learn
- TensorFlow
- TensorFlow Lite
- Streamlit
- Android Studio
- Kotlin
- Jetpack Compose

---

## Project Files

The Streamlit version of the project uses these main files:

```text
app.py
marketing_sales_model.tflite
requirements.txt
runtime.txt
```

### `app.py`

Contains the Streamlit web application code. It loads the TensorFlow Lite model, accepts a TV spend value, runs prediction, and displays the predicted sales value.

### `marketing_sales_model.tflite`

The converted TensorFlow Lite model used for prediction.

### `requirements.txt`

Contains the Python dependencies needed by Streamlit Cloud.

Example:

```txt
streamlit
numpy
tensorflow==2.16.1
```

### `runtime.txt`

Specifies the Python version for Streamlit Cloud.

Example:

```txt
python-3.11
```

This is important because TensorFlow may not support every new Python version immediately.

---

## Streamlit Web App

The Streamlit app allows users to enter a TV advertising spend value and get a sales prediction.

Example input:

```text
50
```

Example output:

```text
Predicted Sales: 177.86
```

### How the Streamlit App Works

1. The app loads `marketing_sales_model.tflite`.
2. The user enters a TV spend value.
3. The value is converted to a NumPy `float32` input.
4. TensorFlow Lite runs inference.
5. The predicted sales value is displayed on the screen.

---

## Running the Streamlit App Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Then open the local Streamlit URL in your browser.

---

## Deploying to Streamlit Cloud

To deploy the app:

1. Push the project files to GitHub.
2. Go to Streamlit Community Cloud.
3. Create a new app.
4. Select the GitHub repository.
5. Set the main file path to:

```text
app.py
```

6. Deploy the app.

If TensorFlow fails to install because of a Python version issue, make sure `runtime.txt` contains:

```txt
python-3.11
```

---

## Android Mobile App

This project is also available as a mobile app built with Android Studio on desktop.

The Android version uses the same TensorFlow Lite model:

```text
marketing_sales_model.tflite
```

The mobile app was built using:

```text
Android Studio
Kotlin
Jetpack Compose
TensorFlow Lite
```

The Android app accepts a TV spend value, runs the `.tflite` model directly on the phone, and displays the predicted sales value.

This confirms that the model can run both in a web app and on a real Android device.

---

## Android App Setup Summary

The successful Android setup used:

```kotlin
implementation("org.tensorflow:tensorflow-lite:2.17.0")
```

The model file was placed inside:

```text
app/src/main/assets/marketing_sales_model.tflite
```

The Android app loads the model from the assets folder and runs prediction using the TensorFlow Lite `Interpreter`.

The expected Android app test result is:

```text
TV Spend: 50
Predicted Sales: 177.86
```

---

## Why This Project Matters

This project demonstrates a complete machine learning deployment pipeline.

Many beginner ML projects stop after training a model in a notebook. This project goes further by showing how a trained model can be:

- Converted into a mobile-friendly TensorFlow Lite format
- Tested in a Streamlit web app
- Integrated into an Android mobile app
- Run directly on a physical Android device

It is a simple regression project, but it teaches an important real-world workflow for deploying machine learning models.

---

## Future Improvements

Possible improvements include:

- Add support for multiple inputs: `TV`, `Radio`, and `Social_Media`
- Improve the Streamlit user interface
- Improve the Android app design
- Add input validation and helpful error messages
- Package the Android app as an APK
- Add screenshots of both the web app and mobile app
- Try a more complex model or dataset

---

## Example Prediction

```text
TV Spend: 50
Predicted Sales: 177.86
```

This prediction is generated by the TensorFlow Lite model, not by a manually written equation.

---

## Author

Built as a learning project to understand how machine learning models can move from notebook experimentation into real-world web and mobile deployment.
