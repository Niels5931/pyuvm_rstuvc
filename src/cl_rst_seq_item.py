from enum import Enum
from pyuvm import uvm_sequence_item


class cl_rst_level(Enum):
    ACTIVE_HIGH = 1
    ACTIVE_LOW = 0


class cl_rst_seq_item(uvm_sequence_item):

    def __init__(self, name: str = "cl_rst_seq_item"):
        super().__init__(name)
        self.parent_sequnce : str | None = None
