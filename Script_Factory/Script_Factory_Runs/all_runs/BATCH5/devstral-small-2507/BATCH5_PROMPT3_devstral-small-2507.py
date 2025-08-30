from flask import Flask, jsonify, make_response
import random

app = Flask(__name__)

@app.route('/flaky-api', methods=['GET'])
def flaky_api():
    # Determine which response to return based on random chance
    rand_num = random.random()

    if rand_num < 0.5:
        # 50% chance of success with valid JSON response
        return jsonify({"status": "success", "data": {"message": "Operation completed successfully"}})
    
    elif rand_num < 0.8:
        # 30% chance of a 500 error (500 - 50 = 30%)
        return make_response(jsonify({"error": "Internal Server Error"}), 500)
    
    else:
        # 20% chance of valid but nonsensical JSON response
        return jsonify({
            "status": "nonsense",
            "data": {
                "random_number": random.randint(1, 100),
                "meaningless_string": ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)),
                "timestamp": str(random.randint(1000000000, 2000000000))
            }
        })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)