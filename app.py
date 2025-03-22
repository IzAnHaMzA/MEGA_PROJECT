from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os
from habit_model import predict_usage

app = Flask(__name__)

# Load and preprocess app usage data
def load_and_preprocess_data():
    data = pd.read_csv('data/app_usage.csv')

    # Convert timestamp to datetime and filter last 7 days
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    recent_data = data[data['timestamp'] >= (pd.Timestamp.now() - pd.Timedelta(days=7))]

    # Aggregate data by app_name
    summary = recent_data.groupby('app_name')['usage_time'].sum().sort_values(ascending=False)
    return summary

# Suggest healthy alternatives
def suggest_habit(app_name):
    suggestions = {
        'Instagram': 'Try reading a book or going for a walk.',
        'YouTube': 'Consider watching educational videos or trying a new hobby.',
        'WhatsApp': 'Spend some time journaling or practicing mindfulness.',
        'Twitter': 'Try engaging in offline conversations or meditating.',
        'LinkedIn': 'Invest time in learning a new skill or networking offline.'
    }
    return suggestions.get(app_name, 'Explore something new!')

@app.route('/')
def index():
    summary = load_and_preprocess_data()
    suggestions = {app: suggest_habit(app) for app in summary.index}

    # Generate Pie Chart
    chart_path = 'static/usage_chart.png'
    if not os.path.exists('static'):
        os.makedirs('static')

    plt.figure(figsize=(6, 6))
    plt.pie(summary, labels=summary.index, autopct='%1.1f%%', startangle=140)
    plt.title('App Usage Distribution (Last 7 Days)')
    plt.savefig(chart_path)
    plt.close()

    return render_template('index.html', summary=summary, suggestions=suggestions, chart_path=chart_path)

@app.route('/predict', methods=['POST'])
def predict():
    day_of_week = int(request.form['day_of_week'])
    launch_count = int(request.form['launch_count'])
    prediction = predict_usage(day_of_week, launch_count)

    return render_template('predict.html', prediction=prediction, day_of_week=day_of_week, launch_count=launch_count)

if __name__ == '__main__':
    app.run(debug=True)
