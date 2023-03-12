from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import pickle
#
# import cv2
# from keras.models import load_model
# from keras.preprocessing import image
#         # img=request.form['file']
# import matplotlib
# matplotlib.use('Agg')
# import easyocr
# from matplotlib import pyplot as plt
# from matplotlib import image as mpimg
# from matplotlib import patches as mpatches
#%matplotlib inline
app = Flask(__name__)
# file='my_model.pkl'
# #load_model=pickle.load(open(file,'rb'))
# model=load_model(file)
# model.make_predict_function()
# UPLOAD_FOLDER = "\Flask\static"

 
# app.secret_key = "secret key"
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
# ALLOWED_EXTENSIONS = set(['png', 'jpg'])
 
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
    
# @app.route('/predict',methods=['POST','GET'])
# def upload():
#     if request.method=='POST':
#         f=request.form['file']
#         basepath=os.path.dirname(__file__)
#         filepath=os.path.join(basepath,'uploads',secure_filename(f.filename))
#         f.save(filepath)
        
#         pred=model_predict(filepath,model)
#         pred
# @app.route('/submit/',methods=['POST','GET'])
# def submit():
#     if request.method=='POST':
        
        
        
#         reader = easyocr.Reader(['en'])
#         test_photo_path = request.form['file']

# # results = model(test_photo_path)
#         results = model(test_photo_path)
#         detections=np.squeeze(results.render())

#         labels, coordinates = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
#         image = cv2.imread(test_photo_path)
#         width, height = image.shape[1], image.shape[0]
#         print()
#         print(f'Photo width,height: {width},{height}. Detected plates: {len(labels)}')
# # predicted_result = pytesseract.image_to_string(image, lang ='eng',config ='--oem 3 --psm 7 -c tessedit_char_whitelist = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
# # filter_predicted_result = "".join(predicted_result.split()).replace(":", "").replace("-", "")
# # predicted_license_plates.append(filter_predicted_result)
#         print(labels)
# # for i in range(len(labels)):
# #   row=coordinates[i]
# #   print(row)


#         for i in range(len(labels)):

#             row = coordinates[i]
#   # if row[4] >= 0.6:

#             x1, y1, x2, y2 = int(row[0]*width), int(row[1]*height), int(row[2]*width), int(row[3]*height)
#             plate_crop = image[int(y1):int(y2), int(x1):int(x2)]
#   # print(plate_crop)
#             ocr_result = reader.readtext((plate_crop))
#             print(ocr_result)
#   # text=ocr_result[0][1]
#             cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 6) ## BBox
#   # cv2.putText(image, f"{text}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)
#   # plt.axis(False)
#             plt.imshow((image)[...,::-1])
#   # print(f'Detection: {i+1}. YOLOv5 prob: {row[4]:.2f}, easyOCR results: {ocr_result}')
# # @app.route('/', methods=['POST'])
# # def upload_image():
# #     # 
# #     if 'file' not in request.files:
# #         flash('No file part')
# #         return redirect(request.url)
# #     file = request.files['file']
# #     if file.filename == '':
# #         flash('No image selected for uploading')
# #         return redirect(request.url)
# #     if file and allowed_file(file.filename):
# #         filename = secure_filename(file.filename)
# #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# #         #print('upload_image filename: ' + filename)
# #         flash('Image successfully uploaded and displayed below')
# #         return render_template('index.html', filename=filename)
# #     else:
# #         flash('Allowed image types are - png, jpg')
# #         return redirect(request.url)
# # @app.route('')
# # @app.route('/display/<filename>')
# # def display_image(filename):
# #     #print('display_image filename: ' + filename)
# #     return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)