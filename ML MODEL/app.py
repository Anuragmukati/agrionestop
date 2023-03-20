from flask import Flask, request, render_template
import pickle
import numpy as np
model = pickle.load(open('predict.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/predict', methods=['POST'])
def predict_crops():
    temp = float(request.form['temp'])
    humidity = float(request.form['hum'])
    ph = float(request.form['ph'])
    wa = float(request.form['wa'])
    season = int(request.form['season'])
        # data = [[temp, humidity, ph, wa, season]]
        # print(data)
        # prediction
    result = model.predict(np.array([temp, humidity, ph, wa, season]).reshape(1,5))
    if result[0] == 0:
        result = 'चावल'
    elif result[0] == 1:
        result = 'मक्का'
    elif result[0] == 2:
        result = 'चना'
    elif result[0] == 3:
        result = 'राजमा'
    elif result[0] == 4:
        result = 'मटर'
    elif result[0] == 5:
        result = 'मोथ बीन्स'
    elif result[0] == 6:
        result = 'मूंग '
    elif result[0] == 7:
        result = 'काला चना'
    elif result[0] == 8:
        result = 'मसूर'
    elif result[0] == 9:
        result = 'तरबूज'
    elif result[0] == 10:
        result = 'खरबूजे'
    elif result[0] == 11:
        result = 'कपास'
    elif result[0] == 12:
        result = 'जूट'     
    return render_template('test.html', result='आपकी भूमि के लिए सबसे अच्छी फसल है  {}'.format(result))

if __name__ == '__main__':
    app.run(debug=True)
    