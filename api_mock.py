import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse

MOCK_PORT = os.environ.get('PORT', 8000)
MOCK_ENDPOINT = "api/v2/projects/999"
MOCK_RESPONCE = {
    "id": 1,
    "name": "Mock Response",
    "status": "successfull",
    "description": "This is a mock response"
}
app = FastAPI()


@app.get(f'/{MOCK_ENDPOINT}')
def api_endpoint():
    return JSONResponse(content=MOCK_RESPONCE)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(MOCK_PORT))
