from fastapi import APIRouter
from .routers_1 import router as router_1
from .routers_2 import router as router_2

router = APIRouter()

router.include_router(router_1, prefix="/routers_1", tags=["Routers 1"])
router.include_router(router_2, prefix="/routers_2", tags=["Routers 2"])
