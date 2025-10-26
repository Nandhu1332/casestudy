from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    value = float(request.form['value'])
    unit_from = request.form['unit_from']
    unit_to = request.form['unit_to']
    result = None

    # Conversion logic (example: length units)
    conversions = {
        'meter': 1,
        'kilometer': 1000,
        'centimeter': 0.01,
        'mile': 1609.34
    }

    if unit_from in conversions and unit_to in conversions:
        result = value * (conversions[unit_from] / conversions[unit_to])

    return render_template('result.html', value=value, unit_from=unit_from,
                           unit_to=unit_to, result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
