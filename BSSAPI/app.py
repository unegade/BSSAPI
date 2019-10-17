from fastapi import FastAPI
from BSSAPI.queue_manager.rabbit import Rabbit
from BSSAPI.api.routers import general, notify
from BSSAPI.settings import *
import uvicorn

app = FastAPI(title=FASTAPI_TITLE, version=FASTAPI_VERSION)
rabbit_sender = Rabbit(RABBIT_HOST, RABBIT_PORT, RABBIT_USER, RABBIT_PASS)
# rabbit_sender.connect(RABBIT_QUEUE_NOTIFY)



def add_routers():
    app.include_router(notify.router)
    app.include_router(general.router)


if __name__ == "__main__":
    add_routers()
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT, debug=FASTAPI_DEBUG)
