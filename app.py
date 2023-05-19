from flask import Flask, request, jsonify, Response
import pandas as pd
from flask_cors import CORS
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import r2_score
import itertools

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def upload():
    file = request.files['csvFile']
    if file.filename == '':
        return 'No file selected'

    file.save(file.filename)
    print("File saved successfully")

    periodicity = request.form['periodicity']
    periods = int(request.form['periods'])

    df = pd.read_csv(file.filename)

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Sales'] = df['Quantity'] * df['UnitPrice']
    df = df.groupby(pd.Grouper(key='InvoiceDate', freq=periodicity)).agg({'Sales': 'sum'}).reset_index()

    df['InvoiceDate'].fillna(-1, inplace=True)
    train_data = df.iloc[:-periods, :]
    test_data = df.iloc[-periods:, :]

    train_data['day_of_week'] = train_data['InvoiceDate'].dt.dayofweek
    train_data['day_of_year'] = train_data['InvoiceDate'].dt.day_of_year
    train_data['month'] = train_data['InvoiceDate'].dt.month
    train_data['quarter'] = train_data['InvoiceDate'].dt.quarter

    param_grid = {
        'order': [(1, 0, 0), (2, 0, 0)],
        'seasonal_order': [(1, 0, 0, 7), (2, 0, 0, 7)]
    }

    best_r2 = float('-inf')
    best_params = None

    for params in itertools.product(param_grid['order'], param_grid['seasonal_order']):
        model = SARIMAX(train_data['Sales'], order=params[0], seasonal_order=params[1])
        model_fit = model.fit(disp=0)

        test_data['day_of_week'] = test_data['InvoiceDate'].dt.dayofweek
        test_data['day_of_year'] = test_data['InvoiceDate'].dt.day_of_year
        test_data['month'] = test_data['InvoiceDate'].dt.month
        test_data['quarter'] = test_data['InvoiceDate'].dt.quarter

        y_pred = model_fit.predict(start=test_data.index[0], end=test_data.index[-1])

        r2 = r2_score(test_data['Sales'], y_pred)

        if r2 > best_r2:
            best_r2 = r2
            best_params = params
            best_y_pred = y_pred

    pred_sales = pd.DataFrame({'Sales': best_y_pred})
    pred_sales.index = pd.date_range(start=train_data['InvoiceDate'].max() + pd.Timedelta(days=1), periods=periods, freq=periodicity)

    output = pred_sales.to_csv(header=True)

    return Response(
        f'R2 Score: {best_r2}\n' + output,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=predicted_sales.csv"})



@app.route('/', methods=['GET'])
def up():
    return "<h3>Sales Forecasting Prediction</h3>"

if __name__ == '__main__':
    app.run(debug=False)
