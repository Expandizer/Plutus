from abc import ABC
import pandas as pd
from anyio import abc


class Instrument(object):
    @abc.abstractmethod
    def run_model(self):
        """Calculate measures (i.e. theoretical value & greeks) for this instrument"""
