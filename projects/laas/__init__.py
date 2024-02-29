import os


class StageABC:
    @classmethod
    def config(cls, key):
        return getattr(cls, key)[os.environ['STAGE']]
