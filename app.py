from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Cluster26114:<password>@cluster26114.vviwijj.mongodb.net/'
mongo = PyMongo(app)

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

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
