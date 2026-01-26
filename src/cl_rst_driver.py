import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pyuvm import ConfigDB, uvm_component, uvm_driver, uvm_fatal
from .cl_rst_config import cl_rst_config, cl_rst_polarity
from .cl_rst_seq_item import cl_rst_seq_item


class cl_rst_driver(uvm_driver):

    def __init__(self, name: str = "cl_rst_driver", parent: uvm_component | None = None):
        super().__init__(name, parent)
        self.cfg: cl_rst_config | None = None

    def build_phase(self):
        super().build_phase()
        self.cfg = ConfigDB().get(self, "", "cfg")
        if self.cfg is None:
            uvm_fatal("RST_DRV", "No config passed to rst driver")
        self.logger.info("Build phase complete")

    async def run_phase(self):
        await super().run_phase()
        while True:
            seq_item: cl_rst_seq_item = await self.seq_item_port.get_next_item()
            parent = seq_item.parent_sequnce
            if parent == "apply":
                self.drive_reset()
            elif parent == "release":
                self.release_reset()
            else:
                uvm_fatal("RST_DRV", "Error! sequence_item_parent not recognized")
            self.seq_item_port.item_done()

    def drive_reset(self) -> None:
        for rst_signal in self.cfg.get_rst_signals():
            if self.cfg.active == cl_rst_polarity.ACTIVE_HIGH:
                rst_signal.value = 1
            else:
                rst_signal.value = 0

    def release_reset(self) -> None:
        for rst_signal in self.cfg.get_rst_signals():
            if self.cfg.active == cl_rst_polarity.ACTIVE_HIGH:
                rst_signal.value = 0
            else:
                rst_signal.value = 1
