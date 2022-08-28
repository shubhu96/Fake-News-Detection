
from flask import Flask, render_template, request
import pickle
  
import numpy as np


vector = pickle.load(open('Vectorizer.pkl', 'rb'))
app = Flask(__name__,template_folder='templates')

model = pickle.load(open('finalized_model.pkl', 'rb'))
app = Flask(__name__,template_folder='templates')



@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/prediction", methods=['POST','GET']) 
def prediction():
    if request.method=='POST':
        news=request.form['news']
        print(news)
        predict=model.predict(vector.vectorizer([news]))
        print(predict)
        return render_template("prediction.html",prediction_text="news headline is->{}".format(predict))
    else:
         return render_template('prediction.html')
     
if __name__=="__main__":
    app.run(debug=True)

         