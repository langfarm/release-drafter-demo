import logging

import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRoute

from langfarm_server.api.main import api_router


logger = logging.getLogger(__name__)


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


API_V1_STR = "/api/public"

app = FastAPI(
    title="Langfarm",
    openapi_url=f"{API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)


app.include_router(api_router, prefix=API_V1_STR)


# for debug app within idea start
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9180, log_config="logging.yaml")
