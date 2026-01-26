TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/dut.sv
TOPLEVEL = dut
SIM = verilator
MODULE = test_rst

# Enable waveform tracing
WAVES = 1
EXTRA_ARGS += --trace --trace-structs

PYTHONPATH := $(abspath $(PWD)/..):$(PYTHONPATH)
export PYTHONPATH

include $(shell cocotb-config --makefiles)/Makefile.sim
