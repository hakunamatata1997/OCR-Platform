from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Define the folder for uploaded images

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    
    return render_template('result.html', text=text)

if __name__ == '__main__':
	app.run(debug=True,port=5555)

