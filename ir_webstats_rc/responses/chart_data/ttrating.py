from datetime import datetime


class TTRating:
    def __init__(self, tuple):
        self.datetime = self.datetime_from_iracing_timestamp(tuple[0])
        self.value = tuple[1]

    # iRacing has all of their timestamps in ms so we need to divide
    @staticmethod
    def datetime_from_iracing_timestamp(timestamp):
        return datetime.utcfromtimestamp(timestamp / 1000)
