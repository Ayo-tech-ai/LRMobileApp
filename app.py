# Import Streamlit for building the web app
import streamlit as st

# Import NumPy for preparing model input
import numpy as np

# Import TensorFlow so we can run the TensorFlow Lite model
import tensorflow as tf


# Load the TensorFlow Lite model only once.
# cache_resource prevents Streamlit from reloading the model every time the user changes input.
@st.cache_resource
def load_tflite_model():
    interpreter = tf.lite.Interpreter(model_path="marketing_sales_model.tflite")
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    return interpreter, input_details, output_details


# Function to make prediction from one TV spend value
def predict_sales(tv_spend):
    interpreter, input_details, output_details = load_tflite_model()

    # The TFLite model expects input shape (1, 1) and dtype float32.
    input_data = np.array([[tv_spend]], dtype=np.float32)

    # Send input into the model
    interpreter.set_tensor(input_details[0]["index"], input_data)

    # Run the model
    interpreter.invoke()

    # Get prediction from model output
    prediction = interpreter.get_tensor(output_details[0]["index"])

    return float(prediction[0][0])


# App title
st.title("Marketing Sales Predictor")

# Short description
st.write("Enter TV advertising spend and the model will predict expected Sales.")

# User input
tv_spend = st.number_input(
    "TV Spend",
    min_value=0.0,
    max_value=200.0,
    value=50.0,
    step=1.0
)

# Prediction button
if st.button("Predict Sales"):
    predicted_sales = predict_sales(tv_spend)

    st.success(f"Predicted Sales: {predicted_sales:.2f}")
