import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def polyregression(x, y, degree):
    coefficients = np.polyfit(x, y, degree)
    poly_function = np.poly1d(coefficients)

    y_pred = poly_function(x)

    plt.scatter(x, y, label='Actual Data')
    plt.plot(x, y_pred, color='red', label='Polynomial Regression')
    plt.xlabel('Motor RPM')
    plt.ylabel('Current')
    plt.title(f'Polynomial Regression (Degree {degree})')
    plt.legend()
    plt.show()

    return poly_function

def load_data(file_path):
    df = pd.read_csv(file_path)
    x = df['Motor RPM'].values
    y = df['Current'].values
    return x, y


if __name__ == "__main__":
    csv_file_path = 'C:\\Users\\pradh\\Desktop\\SAIL PROJECT\\my_data_csv.csv'
    motor_rpm, current = load_data(csv_file_path)
    degree = 2  
    poly_function = polyregression(motor_rpm, current, degree)
    rpm_to_predict = 1500
    predicted_current = poly_function(rpm_to_predict)
    print(f'Predicted current at {rpm_to_predict} RPM: {predicted_current}')
