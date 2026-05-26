from fastapi import APIRouter
from app.schemas.base import APIResponse
from app.services.health_service import HealthService

router = APIRouter()


@router.get("/health", response_model=APIResponse)
async def health_check():
    result= await HealthService.get_status()
    return result
    # return APIResponse(
    #     success=True,
    #     message="API Healthy",
    #     data={"status":"running"}
    # )
    # return {
    #     "status": "healthy"
    # }
