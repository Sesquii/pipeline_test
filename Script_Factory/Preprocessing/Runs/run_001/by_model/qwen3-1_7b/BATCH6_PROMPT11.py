```python
import asyncio
import random
import json
from aiohttp import web

async def handle_data(request):
    """Handle GET request to /data, simulates an unreliable API."""
    # Generate a random number between 0 and 1 to determine reliability
    chance = random.random()
    
    if chance < 0.7:
        # 70% probability of success: return valid JSON response
        return web.json_response({"data": "Some reliable data"})
    else:
        # 30% probability of failure: raise TimeoutError
        raise web.HTTPTimeout(503, "API timeout")

def main():
    """Main function to run the aiohttp server."""
    app = web.Application()
    app.router.add_get('/data', handle_data)
    
    # Run the server on localhost:8080
    web.run_app(app, port=8080)

if __name__ == '__main__':
    asyncio.run(main())