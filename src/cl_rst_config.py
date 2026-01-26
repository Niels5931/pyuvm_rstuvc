from pyuvm import uvm_active_passive_enum, uvm_object
from typing import List
from enum import Enum


class cl_rst_polarity(Enum):
    ACTIVE_LOW = 0
    ACTIVE_HIGH = 1


class cl_rst_config(uvm_object):

    def __init__(self, name="cl_rst_config"):
        super().__init__(name)
        self.active = uvm_active_passive_enum.UVM_ACTIVE
        self.rsts: List = []
        self.polarity: cl_rst_polarity = cl_rst_polarity.ACTIVE_LOW

    def set_rst_signals(self, rst_signals: List) -> None:
        self.rsts = rst_signals

    def set_polarity(self, polarity: cl_rst_polarity) -> None:
        self.polarity = polarity

    def get_rst_signals(self) -> List:
        return self.rsts
