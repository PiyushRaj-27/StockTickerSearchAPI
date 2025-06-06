"""
Module to define the types used througt the microservice
"""

from typing import List

class PackagedSearchResult():
    """
    Search Result type
    """

    def __init__(self, success: bool, result: List | None = None):
        """
        Constructor for PackagedSearchResult
        """
        self.success = success
        self.result = result

    def is_success(self) -> bool:
        """Returns true if searching succeded"""
        return self.success

    def is_failure(self) -> bool:
        """Returns true if searching fails"""
        return not self.success

    def get_result(self):
        """Returns the search result"""
        return self.result
