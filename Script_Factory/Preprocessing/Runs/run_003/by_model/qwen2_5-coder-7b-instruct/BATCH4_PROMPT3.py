# BATCH4_PROMPT3_flask.py

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/unreliable')
def unreliable_api():
    """
    Simulates a flaky API that responds with:
    - 50% chance of success with a valid but nonsensical JSON response.
    - 30% chance of a 500 error.
    - 20% chance of success with a valid but nonsensical JSON response.
    """
    random_number = random.random()
    
    if random_number < 0.3:
        # 30% chance of returning a 500 error
        return "Internal Server Error", 500
    elif random_number < 0.5:
        # 20% chance of returning a valid but nonsensical JSON response
        return jsonify({"message": "This is a nonsensical response"})
    else:
        # 50% chance of success with a valid but nonsensical JSON response
        return jsonify({"message": "This is a successful response"})

if __name__ == "__main__":
    app.run(debug=True)
```

```python
# BATCH4_PROMPT3_fastapi.py

from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

@app.get("/api/unreliable")
async def unreliable_api():
    """
    Simulates a flaky API that responds with:
    - 50% chance of success with a valid but nonsensical JSON response.
    - 30% chance of a 500 error.
    - 20% chance of success with a valid but nonsensical JSON response.
    """
    random_number = random.random()
    
    if random_number < 0.3:
        # 30% chance of returning a 500 error
        raise HTTPException(status_code=500, detail="Internal Server Error")
    elif random_number < 0.5:
        # 20% chance of returning a valid but nonsensical JSON response
        return {"message": "This is a nonsensical response"}
    else:
        # 50% chance of success with a valid but nonsensical JSON response
        return {"message": "This is a successful response"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)