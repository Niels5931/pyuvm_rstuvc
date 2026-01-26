from pyuvm import uvm_env, uvm_component, ConfigDB
from src.cl_rst_agent import cl_rst_agent
from src.cl_rst_config import cl_rst_config


class cl_rst_env(uvm_env):

    def __init__(self, name: str = "cl_rst_env", parent: uvm_component | None = None):
        super().__init__(name, parent)
        self.rst_agent: cl_rst_agent | None = None
        self.cfg: cl_rst_config | None = None

    def build_phase(self):
        super().build_phase()
        self.cfg = ConfigDB().get(self, "", "rst_cfg")
        ConfigDB().set(self, "rst_agent", "rst_cfg", self.cfg)
        self.rst_agent = cl_rst_agent.create("rst_agent", self)

    def connect_phase(self):
        super().connect_phase()
