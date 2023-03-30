"""_summary_
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """_summary_

    Args:
        BaseSettings (_type_): _description_
    """

    main_url: str


settings = Settings()
