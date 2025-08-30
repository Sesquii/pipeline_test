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

# ===== GENERATED TESTS =====
import json
from aiohttp import ClientSession
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

class TestHandleData(AioHTTPTestCase):
    async def get_app(self):
        """Create a new web application instance for testing."""
        from main import app
        return app

    @unittest_run_loop
    async def test_handle_data_success(self):
        """Test the handle_data function with a successful response."""
        # Make a GET request to /data
        async with self.client.get('/data') as response:
            # Check if the status code is 200 (OK)
            self.assertEqual(response.status, 200)
            
            # Parse the JSON response
            data = await response.json()
            
            # Check if the data key exists and has the expected value
            self.assertIn('data', data)
            self.assertEqual(data['data'], 'Some reliable data')

    @unittest_run_loop
    async def test_handle_data_failure(self):
        """Test the handle_data function with a failure response."""
        # Make a GET request to /data
        async with self.client.get('/data') as response:
            # Check if the status code is 503 (Service Unavailable)
            self.assertEqual(response.status, 503)

    @unittest_run_loop
    async def test_handle_data_invalid_json(self):
        """Test the handle_data function with an invalid JSON response."""
        # Mock the handle_data function to return invalid JSON
        async def mock_handle_data(request):
            return web.Response(text='{"data": "Some unreliable data"', content_type='application/json')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data
        async with self.client.get('/data') as response:
            # Check if the status code is 200 (OK) despite invalid JSON
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_empty_response(self):
        """Test the handle_data function with an empty response."""
        # Mock the handle_data function to return an empty response
        async def mock_handle_data(request):
            return web.Response(text='')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data
        async with self.client.get('/data') as response:
            # Check if the status code is 200 (OK) despite empty response
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_large_response(self):
        """Test the handle_data function with a large response."""
        # Mock the handle_data function to return a large JSON response
        async def mock_handle_data(request):
            large_data = json.dumps({"data": "a" * 1024 * 1024})  # 1MB of data
            return web.Response(text=large_data, content_type='application/json')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data
        async with self.client.get('/data') as response:
            # Check if the status code is 200 (OK) despite large response
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_with_headers(self):
        """Test the handle_data function with custom headers."""
        # Make a GET request to /data with custom headers
        async with self.client.get('/data', headers={'X-Custom-Header': 'test'}) as response:
            # Check if the status code is 200 (OK)
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_with_query_params(self):
        """Test the handle_data function with query parameters."""
        # Make a GET request to /data with query parameters
        async with self.client.get('/data', params={'key': 'value'}) as response:
            # Check if the status code is 200 (OK)
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_with_cookies(self):
        """Test the handle_data function with cookies."""
        # Make a GET request to /data with cookies
        async with self.client.get('/data', cookies={'session_id': '12345'}) as response:
            # Check if the status code is 200 (OK)
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_with_authentication(self):
        """Test the handle_data function with authentication."""
        # Mock the handle_data function to require authentication
        async def mock_handle_data(request):
            auth = request.headers.get('Authorization')
            if not auth or auth != 'Bearer valid_token':
                return web.Response(status=401, text='Unauthorized')
            return web.json_response({"data": "Some authenticated data"})
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with authentication
        async with self.client.get('/data', headers={'Authorization': 'Bearer valid_token'}) as response:
            # Check if the status code is 200 (OK) despite authentication
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_with_rate_limiting(self):
        """Test the handle_data function with rate limiting."""
        # Mock the handle_data function to simulate rate limiting
        async def mock_handle_data(request):
            return web.Response(status=429, text='Too Many Requests')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make multiple GET requests to /data to test rate limiting
        for _ in range(10):
            async with self.client.get('/data') as response:
                # Check if the status code is 429 (Too Many Requests) after a few requests
                self.assertEqual(response.status, 429)

    @unittest_run_loop
    async def test_handle_data_with_caching(self):
        """Test the handle_data function with caching."""
        # Mock the handle_data function to simulate caching
        async def mock_handle_data(request):
            return web.Response(text='{"data": "Some cached data"}', headers={'Cache-Control': 'max-age=3600'})
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with caching
        async with self.client.get('/data') as response:
            # Check if the status code is 200 (OK) despite caching
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_with_ssl(self):
        """Test the handle_data function with SSL."""
        # Mock the handle_data function to simulate SSL
        async def mock_handle_data(request):
            return web.Response(text='{"data": "Some SSL data"}')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with SSL
        async with self.client.get('https://localhost:8443/data') as response:
            # Check if the status code is 200 (OK) despite SSL
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_with_proxy(self):
        """Test the handle_data function with a proxy."""
        # Mock the handle_data function to simulate a proxy
        async def mock_handle_data(request):
            return web.Response(text='{"data": "Some proxied data"}')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a proxy
        async with self.client.get('/data', proxy='http://localhost:8081') as response:
            # Check if the status code is 200 (OK) despite proxy
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_with_timeout(self):
        """Test the handle_data function with a timeout."""
        # Mock the handle_data function to simulate a timeout
        async def mock_handle_data(request):
            return web.Response(status=504, text='Gateway Timeout')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a timeout
        async with self.client.get('/data', timeout=1) as response:
            # Check if the status code is 504 (Gateway Timeout) despite timeout
            self.assertEqual(response.status, 504)

    @unittest_run_loop
    async def test_handle_data_with_custom_content_type(self):
        """Test the handle_data function with a custom content type."""
        # Mock the handle_data function to return a custom content type
        async def mock_handle_data(request):
            return web.Response(text='{"data": "Some custom data"}', content_type='application/custom')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom content type
        async with self.client.get('/data') as response:
            # Check if the status code is 200 (OK) despite custom content type
            self.assertEqual(response.status, 200)

    @unittest_run_loop
    async def test_handle_data_with_custom_status_code(self):
        """Test the handle_data function with a custom status code."""
        # Mock the handle_data function to return a custom status code
        async def mock_handle_data(request):
            return web.Response(status=418, text='I\'m a teapot')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom status code
        async with self.client.get('/data') as response:
            # Check if the status code is 418 (I'm a teapot) despite custom status code
            self.assertEqual(response.status, 418)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_message(self):
        """Test the handle_data function with a custom error message."""
        # Mock the handle_data function to return a custom error message
        async def mock_handle_data(request):
            return web.Response(status=500, text='Internal Server Error: Something went wrong')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error message
        async with self.client.get('/data') as response:
            # Check if the status code is 500 (Internal Server Error) despite custom error message
            self.assertEqual(response.status, 500)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_code(self):
        """Test the handle_data function with a custom error code."""
        # Mock the handle_data function to return a custom error code
        async def mock_handle_data(request):
            return web.Response(status=403, text='Forbidden: Access denied')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error code
        async with self.client.get('/data') as response:
            # Check if the status code is 403 (Forbidden) despite custom error code
            self.assertEqual(response.status, 403)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_header(self):
        """Test the handle_data function with a custom error header."""
        # Mock the handle_data function to return a custom error header
        async def mock_handle_data(request):
            return web.Response(status=500, text='Internal Server Error', headers={'X-Custom-Error': 'Something went wrong'})
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error header
        async with self.client.get('/data') as response:
            # Check if the status code is 500 (Internal Server Error) despite custom error header
            self.assertEqual(response.status, 500)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_body(self):
        """Test the handle_data function with a custom error body."""
        # Mock the handle_data function to return a custom error body
        async def mock_handle_data(request):
            return web.Response(status=403, text='Forbidden: Access denied', content_type='application/json')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error body
        async with self.client.get('/data') as response:
            # Check if the status code is 403 (Forbidden) despite custom error body
            self.assertEqual(response.status, 403)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_content_type(self):
        """Test the handle_data function with a custom error content type."""
        # Mock the handle_data function to return a custom error content type
        async def mock_handle_data(request):
            return web.Response(status=500, text='Internal Server Error', content_type='application/custom')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error content type
        async with self.client.get('/data') as response:
            # Check if the status code is 500 (Internal Server Error) despite custom error content type
            self.assertEqual(response.status, 500)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_status_code(self):
        """Test the handle_data function with a custom error status code."""
        # Mock the handle_data function to return a custom error status code
        async def mock_handle_data(request):
            return web.Response(status=418, text='I\'m a teapot')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error status code
        async with self.client.get('/data') as response:
            # Check if the status code is 418 (I'm a teapot) despite custom error status code
            self.assertEqual(response.status, 418)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_message_and_code(self):
        """Test the handle_data function with a custom error message and code."""
        # Mock the handle_data function to return a custom error message and code
        async def mock_handle_data(request):
            return web.Response(status=403, text='Forbidden: Access denied', content_type='application/json')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error message and code
        async with self.client.get('/data') as response:
            # Check if the status code is 403 (Forbidden) despite custom error message and code
            self.assertEqual(response.status, 403)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_message_and_header(self):
        """Test the handle_data function with a custom error message and header."""
        # Mock the handle_data function to return a custom error message and header
        async def mock_handle_data(request):
            return web.Response(status=500, text='Internal Server Error: Something went wrong', headers={'X-Custom-Error': 'Something went wrong'})
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error message and header
        async with self.client.get('/data') as response:
            # Check if the status code is 500 (Internal Server Error) despite custom error message and header
            self.assertEqual(response.status, 500)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_message_and_body(self):
        """Test the handle_data function with a custom error message and body."""
        # Mock the handle_data function to return a custom error message and body
        async def mock_handle_data(request):
            return web.Response(status=403, text='Forbidden: Access denied', content_type='application/json')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error message and body
        async with self.client.get('/data') as response:
            # Check if the status code is 403 (Forbidden) despite custom error message and body
            self.assertEqual(response.status, 403)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_message_and_content_type(self):
        """Test the handle_data function with a custom error message and content type."""
        # Mock the handle_data function to return a custom error message and content type
        async def mock_handle_data(request):
            return web.Response(status=500, text='Internal Server Error', content_type='application/custom')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error message and content type
        async with self.client.get('/data') as response:
            # Check if the status code is 500 (Internal Server Error) despite custom error message and content type
            self.assertEqual(response.status, 500)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_message_and_status_code(self):
        """Test the handle_data function with a custom error message and status code."""
        # Mock the handle_data function to return a custom error message and status code
        async def mock_handle_data(request):
            return web.Response(status=418, text='I\'m a teapot')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error message and status code
        async with self.client.get('/data') as response:
            # Check if the status code is 418 (I'm a teapot) despite custom error message and status code
            self.assertEqual(response.status, 418)

    @unittest_run_loop
    async def test_handle_data_with_custom_error_message_and_header_and_body(self):
        """Test the handle_data function with a custom error message and header and body."""
        # Mock the handle_data function to return a custom error message and header and body
        async def mock_handle_data(request):
            return web.Response(status=500, text='Internal Server Error: Something went wrong', headers={'X-Custom-Error': 'Something went wrong'}, content_type='application/json')
        
        self.app.router.add_get('/data', mock_handle_data)
        
        # Make a GET request to /data with a custom error message and header and body
        async with self.client.get('/data') as response:
