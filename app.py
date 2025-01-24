from flask import Flask, render_template, request, send_from_directory
import webbrowser
import os

app = Flask(__name__)

# Update the data path to use the network drive
DATA_PATH = r"O:\Program Files\ArmstrongApp\Data"
# Create directory if it doesn't exist
os.makedirs(DATA_PATH, exist_ok=True)

@app.route('/')
def index():
    # Get list of files in data directory
    files = os.listdir(DATA_PATH)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
        
    # Save to local data folder
    file.save(os.path.join(DATA_PATH, file.filename))
    return 'File uploaded successfully'

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(DATA_PATH, filename)

def main():
    # Open browser automatically
    webbrowser.open('http://localhost:5000')
    # Run Flask without admin rights
    app.run(host='localhost', port=5000)

if __name__ == '__main__':
    main() 