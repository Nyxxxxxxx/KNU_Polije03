from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow access from all domains

@app.route('/api/image/<student_id>', methods=['GET'])
def get_image_path(student_id):
    # Assuming images are named by student IDs and stored in 'project/public/images/'
    image_directory = '/Users/simon/Desktop/Developer/Polije_Project/project/public/images/'
    image_path = f'{image_directory}{student_id}.jpeg'
    
    if os.path.exists(image_path):
        return jsonify({'imagePath': image_path})
    else:
        return jsonify({'error': 'Image not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
