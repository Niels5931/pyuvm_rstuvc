from pyuvm import uvm_active_passive_enum, uvm_agent, uvm_component, uvm_fatal, uvm_sequencer, uvm_driver, ConfigDB
from .cl_rst_driver import cl_rst_driver
from .cl_rst_config import cl_rst_config


class cl_rst_agent(uvm_agent):

    def __init__(self, name: str = "cl_rst_agent", parent: uvm_component | None = None):
        super().__init__(name, parent)
        self.sequencer: uvm_sequencer | None = None
        self.driver: uvm_driver | None = None
        self.cfg: cl_rst_config | None = None

    def build_phase(self):
        super().build_phase()
        self.cfg = ConfigDB().get(self, "", "rst_cfg")
        if self.cfg is None:
            uvm_fatal("RST_AGENT", "Can not retrieve config from configDB")
        if self.cfg.active == uvm_active_passive_enum.UVM_ACTIVE:
            self.sequencer = uvm_sequencer.create("sequencer", self)
            ConfigDB().set(self, "driver", "cfg", self.cfg)
            self.driver = cl_rst_driver.create("driver", self)

    def connect_phase(self):
        super().connect_phase()
        if self.cfg.active == uvm_active_passive_enum.UVM_ACTIVE:
            self.driver.seq_item_port.connect(self.sequencer.seq_item_export)
