from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    response = None

    # 50% chance of success
    if random.random() < 0.5:
        response = {"message": "Success", "data": "Some data"}
    
    # 30% chance of 500 error
    elif random.random() < 0.3:
        return jsonify({"error": "Internal Server Error"}), 500

    # 20% chance of nonsensical JSON response
    else:
        response = {"message": "Success", "data": random.choice(["Nonsense1", "Nonsense2", "Nonsense3"])}
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)