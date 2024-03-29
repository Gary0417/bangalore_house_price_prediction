from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location'] 
    bedroom = int(request.form['bedroom'])
    ready_to_move = int(request.form['ready_to_move'])
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bedroom, ready_to_move)
    })
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()