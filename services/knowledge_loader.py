"""
Module defining module loader
"""
import os
import logging
from typing import List
logger = logging.getLogger(f"Search.{__name__}")

# file path for knowledge
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "f.txt")

class KnowledgeLoader():
    """
    Loads knowledge from a txt file.
    """
    def __init__(self, location: str = file_path):
        self.location = location
        self.data: List = None

    def load(self) -> None:
        """
        Loads the data from the given location
        """
        data = None
        try:
            with open(self.location, mode="r", encoding="utf-8") as source:
                data = source.read()

        except FileNotFoundError as e:
            logger.error("[KnowledgeLoader.load] File not found %s", e)

        data = data.split("\n")

        if len(data) == 0:
            logger.warning("[KnowledgeLoader.load] Data found empty. Please recheck the knowledge source")

        self.data = data

    def get_data(self) -> List | None:
        """Returns data if data has beed loaded."""
        if not self.data:
            logger.warning("[KnowledgeLoader.get_data] Trying to access data before calling the load method")
        return self.data


# if __name__ == "__main__":
#     # quick test

#     with open(file_path, "r", encoding="utf-8") as f:
#         content = f.read()
#         lines = content.split("\n")

    