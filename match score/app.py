from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__,template_folder='template')

# Load the dataset (replace with the path to your dataset)
data = pd.read_csv('/Users/surajsamal/Desktop/untitled folder 2/ipl_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    mid = request.form.get('mid')  # Get user input for match ID
    if mid:
        filtered_data = data[data['mid'] == int(mid)]
        if not filtered_data.empty:
            total_runs = filtered_data['runs'].sum()  # Calculate total runs
            return render_template('result.html', mid=mid, total_runs=total_runs)
        else:
            return render_template('result.html', mid=mid, total_runs="No data found.")
    return render_template('result.html', mid=mid, total_runs="Invalid match ID.")

if __name__ == '__main__':
    app.run(debug=True)