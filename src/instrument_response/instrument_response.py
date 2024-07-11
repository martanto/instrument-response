import pandas as pd


class InstrumentResponse:
    def __init__(self):
        self.df = pd.DataFrame

    def available(self):
        return self
