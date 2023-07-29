import uvicorn
from views.api import ConsultApi


api_app = ConsultApi().app

if __name__ == "__main__":
    uvicorn.run(api_app, host="localhost", port=8000)
