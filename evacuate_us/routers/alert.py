from fastapi import APIRouter

alert_router = APIRouter()


@alert_router.get("/alert")
async def alert_give_map():
    pass
