import cocotb
from pyuvm import uvm_root
from tb.cl_rst_base_test import cl_rst_base_test


@cocotb.test()
async def rst_test(dut):
    await uvm_root().run_test(cl_rst_base_test)
