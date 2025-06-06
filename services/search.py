"""
module defining search function
"""

import logging
from typing import List
from app.core.types import PackagedSearchResult
from app.services.search_backend import SearchBackend


logger = logging.getLogger(f"Search.{__name__}")

def search_knowledge_base(q: str, limit: int, skip:int,knowledgebase:List, search_backend: SearchBackend) -> List:
    """
    Main search function called by the end point
    """
    try:
        searcher: SearchBackend = search_backend()

        result:PackagedSearchResult = searcher.search_with_skip_limit(q, knowledgebase, limit, skip)

    except Exception as e:
        logger.error("[search_knowledge_base] Failed to search: %s", e)

    if result.is_failure():
        return None

    return result.get_result()