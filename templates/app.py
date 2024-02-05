# Import necessary modules
from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/overlay_app'  # Update with your MongoDB URI
mongo = PyMongo(app)

# ... Existing API routes for overlays ...
@app.route('/')
def index():
    return render_template('index.html')
    from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Your existing routes...

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
# API routes for overlays
@app.route('/api/overlays', methods=['POST'])
def create_overlay():
    data = request.json
    mongo.db.overlays.insert_one(data)
    return jsonify({"message": "Overlay created successfully"})

@app.route('/api/overlays', methods=['GET'])
def get_overlays():
    overlays = list(mongo.db.overlays.find())
    return jsonify(overlays)

@app.route('/api/overlays/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    data = request.json
    mongo.db.overlays.update_one({"_id": overlay_id}, {"$set": data})
    return jsonify({"message": "Overlay updated successfully"})

@app.route('/api/overlays/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    mongo.db.overlays.delete_one({"_id": overlay_id})
    return jsonify({"message": "Overlay deleted successfully"})
# New API routes for controls
@app.route('/api/play', methods=['POST'])
def play():
    # Logic to play the video
    return jsonify({"message": "Video played successfully"})

@app.route('/api/pause', methods=['POST'])
def pause():
    # Logic to pause the video
    return jsonify({"message": "Video paused successfully"})

@app.route('/api/volume', methods=['POST'])
def set_volume():
    data = request.json
    # Logic to set the volume
    return jsonify({"message": "Volume set successfully"})

if __name__ == '__main__':
    app.run(debug=True)


