import cocotb
from cocotb.triggers import Timer
from pyuvm import uvm_test, uvm_component, ConfigDB
from src.cl_rst_config import cl_rst_config, cl_rst_polarity
from src.cl_rst_seq_lib import cl_rst_apply_seq, cl_rst_release_seq
from tb.cl_rst_env import cl_rst_env


class cl_rst_base_test(uvm_test):

    def __init__(self, name: str = "cl_rst_base_test", parent: uvm_component | None = None):
        super().__init__(name, parent)
        self.env: cl_rst_env | None = None
        self.cfg: cl_rst_config | None = None

    def build_phase(self):
        super().build_phase()
        self.cfg = cl_rst_config("rst_cfg")
        self.cfg.set_rst_signals([cocotb.top.rst_n])
        self.cfg.set_polarity(cl_rst_polarity.ACTIVE_LOW)
        ConfigDB().set(self, "env", "rst_cfg", self.cfg)
        self.env = cl_rst_env.create("env", self)

    async def run_phase(self):
        self.raise_objection()

        # Apply reset
        apply_seq = cl_rst_apply_seq("apply_rst")
        await apply_seq.start(self.env.rst_agent.sequencer)

        # Hold reset for some time
        await Timer(100, "ns")

        # Release reset
        release_seq = cl_rst_release_seq("release_rst")
        await release_seq.start(self.env.rst_agent.sequencer)

        await Timer(100, "ns")
        self.drop_objection()
