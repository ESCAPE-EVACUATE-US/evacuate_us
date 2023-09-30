from fastapi import APIRouter

exit_router = APIRouter()


@exit_router.get("/alert")
async def exit_give_map():
    pass
