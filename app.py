from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from tensorflow.keras.applications.vgg16 import preprocess_input
import os
from tensorflow.keras.preprocessing import image
from PIL import Image
from pre import class_x

app = Flask(__name__,template_folder="pages")
model = load_model('realorfake.hdf5')
target_img = os.path.join(os.getcwd() , 'images')
@app.route('/')
def index_view():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

#Allow files with extension png, jpg and jpeg
ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT
           
# Function to load and prepare the image in right shape
def read_image(filename):

    img = cv2.imread(filename)
    img = cv2.resize(img, (128,128))
    img1=np.array(img)
    img1=img1.reshape(1,128,128,3)
    return img1

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            flag=1
            filename = file.filename
            temp=filename
            file_path = os.path.join('static\images', filename)
            file.save(file_path)
            img = read_image(file_path)
            class_prediction=model.predict(img) 
            classes_x=np.argmax(class_prediction,axis=1)
            if class_x(filename) == 0:
              tumor = "Fake"
              flag=0
            elif classes_x ==1:
              tumor = "Real"
            return render_template('predict.html', tumor = tumor,prob=class_prediction, user_image = file_path, flag=flag)
        else:
            return "Unable to read the file. Please check file extension"
if __name__ == '__main__':
    app.run(debug=True)