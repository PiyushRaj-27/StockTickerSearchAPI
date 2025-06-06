"""
Defines configuration for all the components in the Microservice
"""
import logging
from typing import List
from app.services.knowledge_loader import KnowledgeLoader
from app.services.search_backend import RapidFuzzBackend, SearchBackend

def setup_loging():
    """ Sets up logging for the Entire Microservice"""
    logger = logging.getLogger("Search")

    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    logger.propagate = False

class V1Congifuguration():
    """
    Configuration class for version 1 of search API
    """
    prefix: str = "/v1"
    tags: List[str] = ["v1"]
    defaultSearchBackend: SearchBackend = RapidFuzzBackend
 

class DefaultParams():
    """
    Defines default params for the search api
    """

    defaultQuery: str = ""
    defaultSkip: int = 0
    defaultLimit: int = 10


knowledge = KnowledgeLoader()
knowledge.load()


def get_knowledge():
    """
    Dependecy to extract knowledge from database.
    """
    return knowledge.get_data()
