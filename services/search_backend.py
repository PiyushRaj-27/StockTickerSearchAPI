"""
Module defining various search_backends for the search API
"""
import logging
from typing import List
from abc import ABC, abstractmethod
from rapidfuzz import process

from app.core.types import PackagedSearchResult

logger = logging.getLogger(f"Search.{__name__}")

class SearchBackend(ABC):
    """
    Base SearchBackend.

    Each searchbackend should define the following methods and attribute

    backend_name: str
    search_with_skip_limit(q: str, base: List[str], limit:int, skip: int)
    """
    @abstractmethod
    def search_with_skip_limit(self, q: str, base: List[str], limit: int, skip: int) -> PackagedSearchResult:
        """
        Abstract Base Method for search api
        """

class RapidFuzzBackend(SearchBackend):
    """
    RapidFuzzBackend for the search API. 
    Uses RapidFuzz library for fuzzy search over knowledge base.
    Should be the default choice beacause of high performance.
    """
    def __init__(self):
        super().__init__()
        self.backend_name: str = "Rapid Fuzz Backend"

    def search_with_skip_limit(self, q: str, base: List[str], limit:int, skip: int) -> PackagedSearchResult:
        """
        Implements search using RapidFuzz
        """
        try:
            result = process.extract(query = q, choices = base, limit = limit)
            
        except Exception as e:
            logger.error("[RapidFuzzBackend] error during query searching over base: %s", e)
            return PackagedSearchResult(success=False)


        for idx, matched in enumerate(result):
            try:
                parse = matched[0].split("-")

                if len(parse) < 2:
                    raise Exception("Parsed value has too few elements")

                symbol = parse[0].strip()
                name = parse[1].strip()
                result[idx] = [symbol, name, matched[1], matched[2]]

            except Exception as e:
                logger.error("[RapidFuzzBackend] error during parsing results at %s with error: %s", matched, e)

        return PackagedSearchResult(success= True, result= result)
