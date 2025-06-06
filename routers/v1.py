"""
Version 1 of the search API
"""
import logging
from typing import List
from fastapi import APIRouter, Depends, Query, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.services.search import search_knowledge_base
from app.core.config import V1Congifuguration, DefaultParams, setup_loging, get_knowledge


setup_loging()
logger = logging.getLogger(f"Search.{__name__}")
logger.info("Starting Logging Services")
router = APIRouter(
    prefix = V1Congifuguration.prefix,
    tags = V1Congifuguration.tags
)

limiter = Limiter(key_func=get_remote_address)


@router.get("/")
async def check_health():
    """
    Root endpoint for API version 1 for health check.
    """
    return {"status": "Live"}


@router.get("/search")
@limiter.limit("30/minute")
async def search(request: Request, q:str = Query(default = DefaultParams.defaultQuery, description="Query to search matches for"), 
                 limit:int = Query(default = DefaultParams.defaultLimit, description="How much to limit search to"), 
                 skip: int = Query(default = DefaultParams.defaultSkip, description="Pagination, [Not Implemented]"),
                 knowledge: List = Depends(get_knowledge)):
    """
    Search endpoint for API version 1
    """

    try:
        result = search_knowledge_base(q, limit, skip, knowledge ,V1Congifuguration.defaultSearchBackend)

    except Exception as e:
        logging.error("[/v1/search] search failed with exception: %s",e)
        return {"success": False, "result": ""}

    return {"success": True, "result": result}
    