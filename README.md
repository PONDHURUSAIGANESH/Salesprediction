# Sales Forecasting using SARIMA Model

This project aims to develop a sales forecasting system using the SARIMA (Seasonal AutoRegressive Integrated Moving Average) model. The forecasting system is integrated with an Angular frontend and powered by Flask, a Python web framework.

## Overview

Sales forecasting plays a crucial role in the business planning process. Accurate sales forecasts can help organizations make informed decisions regarding inventory management, resource allocation, and overall business strategies. This project leverages SARIMA, a popular time series forecasting model, to predict future sales based on historical data.

The system consists of three main components:
1. **Data Preprocessing**: The historical sales data is preprocessed to handle missing values, outliers, and any necessary transformations. This step ensures that the data is suitable for training the SARIMA model.
2. **Model Training**: The SARIMA model is trained using the preprocessed data. The model identifies underlying patterns, trends, and seasonality in the sales data to generate accurate forecasts.
3. **Integration with Angular Frontend**: The trained SARIMA model is integrated into an Angular frontend using Flask, a micro web framework for Python. The frontend provides a user-friendly interface for users to input the required data and view the sales forecasts generated by the model.

## Technologies Used

The following technologies are utilized in this project:

- **SARIMA**: The SARIMA model is implemented using the `statsmodels` library in Python, which provides a comprehensive suite of time series analysis tools.
- **Angular**: The Angular framework is used to develop the frontend interface for user interaction. Angular provides a robust and scalable platform for building modern web applications.
- **Flask**: Flask is a lightweight web framework in Python used to serve the SARIMA model as an API endpoint and handle requests from the Angular frontend.
- **GitHub**: The project is hosted on GitHub, a web-based version control system. GitHub allows for easy collaboration, code sharing, and version tracking.

## Usage

To run the project locally, follow these steps:

1. Clone the repository from GitHub: `git clone https://github.com/your-username/your-repo.git`.
2. Navigate to the project directory: `cd your-repo`.
3. Set up a Python virtual environment: `python3 -m venv venv` (optional but recommended).
4. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows PowerShell).
5. Install the project dependencies: `pip install -r requirements.txt`.
6. Start the Flask server: `flask run`.
7. Open your web browser and visit `http://localhost:5000` to access the Angular frontend.

## Future Improvements

This project provides a solid foundation for sales forecasting using SARIMA. However, there are several potential areas for future improvement and expansion:

- **Model Tuning**: Experiment with different SARIMA configurations and hyperparameters to improve forecasting accuracy.
- **Visualization**: Enhance the frontend by incorporating interactive charts and graphs to visualize the historical data and sales forecasts.
- **User Authentication**: Implement user authentication and authorization to restrict access and ensure data privacy.
- **Database Integration**: Integrate a database system, such as PostgreSQL or MongoDB, to store and retrieve historical sales data.

## Contributions

Contributions to this project are welcome. If you find any issues or have ideas for enhancements, please feel free to submit a pull request or open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use,
Prediction Page
![Screenshot 2023-05-19 204731](https://github.com/PONDHURUSAIGANESH/Salesprediction/assets/78872384/62bb223e-9b46-4e36-ba8d-5e428e2e3b9f)

Dashboard

![Screenshot 2023-05-19 205217](https://github.com/PONDHURUSAIGANESH/Salesprediction/assets/78872384/e097e07f-10ca-4b9f-bf92-a04ae7b53443)
![Screenshot 2023-05-19 205232](https://github.com/PONDHURUSAIGANESH/Salesprediction/assets/78872384/67fc8725-3825-4f68-a437-9af0a2078d36)
