from fastapi import FastAPI
from mangum import Mangum
from uvicorn import run

app = FastAPI()
handler = Mangum(app)


@app.get('/')
async def home():
    print('app running')
    return {'message': 'app running'}


if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8000)
