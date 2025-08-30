import asyncio
import random
from aiohttp import web

async def handle_data(request):
    # Simulate flaky API behavior with 70% success rate and 30% failure rate
    if random.random() < 0.7:
        # Return valid JSON response for 70% of the time
        return web.json_response({
            "status": "success",
            "data": {
                "id": 1,
                "name": "Test Data",
                "value": 42
            }
        })
    else:
        # Raise TimeoutError for 30% of the time to simulate flakiness
        raise web.HTTPServiceUnavailable(reason='TimeoutError')

async def init_app():
    app = web.Application()
    app.router.add_get('/data', handle_data)
    return app

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app())
    web.run_app(app, port=8080)