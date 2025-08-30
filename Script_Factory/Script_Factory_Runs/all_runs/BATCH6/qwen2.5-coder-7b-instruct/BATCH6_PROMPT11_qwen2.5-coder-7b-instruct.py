import aiohttp
from aiohttp import web
import random

async def data_handler(request):
    # 70% chance to return valid JSON response
    if random.random() < 0.7:
        return web.json_response({"message": "Success", "data": {"key": "value"}})
    else:
        # 30% chance to raise a TimeoutError
        raise asyncio.TimeoutError("API timed out")

app = web.Application()
app.router.add_get('/data', data_handler)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)