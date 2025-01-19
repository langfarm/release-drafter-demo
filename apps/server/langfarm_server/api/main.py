from fastapi import APIRouter

from langfarm_server.api.routes import public

api_router = APIRouter()
api_router.include_router(public.router, prefix="", tags=["public"])
