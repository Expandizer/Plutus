from assets.instrument import Instrument
from enums import *


class Stock(Instrument):

    def __init__(self):


    # Name of model gets modified for testing, kwargs to run multiple models at once
    def run_model(self, model=STOCK_MODEL.BLACK_SCHOLES, **kwargs):
        if model == STOCK_MODEL.BLACK_SCHOLES:
            return self.black_scholes(self, **kwargs)
        elif model == STOCK_MODEL.BINOMIAL_TREE:
            return self.binomial_tree(self, **kwargs)
        elif model == STOCK_MODEL.MONTE_CARLO:
            return self.monte_carlo(self, **kwargs)
        else:
            return ValueError("Unsupported model")
