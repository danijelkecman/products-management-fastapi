# project/app/api/ping.py


from fastapi import APIRouter, Depends

from app.config import get_settings, Settings


router = APIRouter()


@router.get('/ping')
async def ping(settings: Settings = Depends(get_settings)):
    return {
        'ttl': '1100',
        'environment': settings.environment,
        'testing': settings.testing
    }