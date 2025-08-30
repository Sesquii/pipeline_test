# BATCH6_PROMPT11_Granite.py

import asyncio
import random
from aiohttp import web
from urllib.parse import quote_plus

async def handle(request):
    if random.random() < 0.7:  # 70% chance of success
        data = {"message": "Success", "value": 42}
        return web.json_response(data)
    else:  # 30% chance of failure
        raise web.Timeout

async def main():
    app = web.Application()
    app.router.add_get('/data', handle)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    print("Server started at http://localhost:8080")
    try:
        await asyncio.Future()  # Keep the server running
    except KeyboardInterrupt:
        pass
    finally:
        await runner.cleanup()

if __name__ == "__main__":
    asyncio.run(main())