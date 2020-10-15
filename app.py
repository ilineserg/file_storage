from aiohttp import web
from routes import routes


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='127.0.0.1', port=8000)
