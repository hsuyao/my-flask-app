from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file and file.filename.endswith('.xls'):
        df = pd.read_excel(file)
        analysis = df.describe().to_html()
        return render_template('analysis.html', analysis=analysis)
    else:
        return 'Invalid file format. Please upload an .xls file.'

if __name__ == '__main__':
    app.run(debug=True)

