from fastapi import APIRouter

from backend_poc.api.v1.endpoints.person import router as person_router

routers = APIRouter()
router_list = [person_router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)