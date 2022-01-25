from json import load
from flask import Flask , render_template, request
import joblib



app_flask = Flask(__name__)
#name file create application for the variable app.

loaded_model = joblib.load('dib_78.pkl')



@app_flask.route('/') #decorator 
def index():
    return 'hello'

@app_flask.route('/homepage') #decorator 
def home():
    return render_template('homepage.html')

@app_flask.route('/predict', methods = ['POST']) #decorator 
def predict():
    preg = request.form.get('preg')
    plas =  request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    

    
    predication =  loaded_model.predict([[preg , plas, pres, skin, test, mass, pedi, age]])

    if predication[0]==1:
       val = 'diabatic'
    else:
        val = 'Not a diabtic'

    return render_template('result.html' , value = val)


if __name__ == '__main__':
 app_flask.run(debug=True)



