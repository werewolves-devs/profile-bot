from configlib import BaseConfig


class Config(BaseConfig):
    token: str
    game_master: int


config = Config.get_instance()
