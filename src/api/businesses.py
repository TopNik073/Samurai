from fastapi import APIRouter, Request
from api.templates_config import templates


router = APIRouter(prefix="", tags=["Businesses"])


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "auth": False})


@router.get("newsline")
async def newsline():
    return {"newsline": "news"}
