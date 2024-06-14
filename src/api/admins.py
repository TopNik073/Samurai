from fastapi import APIRouter


router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/login")
async def login_admin():
    return


@router.get("/")
async def admin():
    return
