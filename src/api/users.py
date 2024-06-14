from fastapi import APIRouter


router = APIRouter(prefix="/user", tags=["User"])


@router.get("/login")
async def login():
    return {"login": "user"}


@router.get("/newlogin")
async def newlogin():
    return {"newlogin": "user"}


@router.get("/profile")
async def profile():
    return {"profile": "user"}


@router.get("/logout")
async def logout():
    return {"logout": "user"}
