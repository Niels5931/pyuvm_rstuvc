# Done did crazy change for the fork

# cl_rst - Reset Driver for PyUVM

A reusable reset driver component for UVM-based verification using PyUVM and cocotb.

## Overview

This package provides UVM components for managing reset signals in cocotb-based testbenches:

- **cl_rst_agent** - UVM agent containing sequencer and driver
- **cl_rst_config** - Configuration object for reset settings (signal bindings, polarity)
- **cl_rst_driver** - UVM driver that applies and releases reset signals
- **cl_rst_seq_item** - Sequence item for reset transactions (apply/release operations)
- **cl_rst_seq_lib** - Sequences for applying and releasing reset

## Requirements

- Python 3.10+
- [cocotb](https://github.com/cocotb/cocotb) 2.0+
- [pyuvm](https://github.com/pyuvm/pyuvm)

## Usage

### Single Reset (Active-Low)

```python
from src.cl_rst_config import cl_rst_config, cl_rst_polarity
from src.cl_rst_seq_lib import cl_rst_apply_seq, cl_rst_release_seq

# Configure active-low reset
cfg = cl_rst_config()
cfg.set_rst_signals([cocotb.top.rst_n])
cfg.set_polarity(cl_rst_polarity.ACTIVE_LOW)

# Add to ConfigDB
ConfigDB().set(self, "env", "rst_cfg", cfg)

# Apply reset
apply_seq = cl_rst_apply_seq()
await apply_seq.start(env.rst_agent.sequencer)

# Wait for reset duration
await Timer(100, "ns")

# Release reset
release_seq = cl_rst_release_seq()
await release_seq.start(env.rst_agent.sequencer)
```

### Multiple Reset Signals (Same Polarity)

```python
from src.cl_rst_config import cl_rst_config, cl_rst_polarity
from src.cl_rst_seq_lib import cl_rst_apply_seq, cl_rst_release_seq

# Configure multiple active-high reset signals
cfg = cl_rst_config()
cfg.set_rst_signals([cocotb.top.rst, cocotb.top.subsys_rst])
cfg.set_polarity(cl_rst_polarity.ACTIVE_HIGH)

# Add to ConfigDB
ConfigDB().set(self, "env", "rst_cfg", cfg)

# Apply reset to ALL signals
apply_seq = cl_rst_apply_seq()
await apply_seq.start(env.rst_agent.sequencer)

# Wait for reset duration
await Timer(100, "ns")

# Release reset on ALL signals
release_seq = cl_rst_release_seq()
await release_seq.start(env.rst_agent.sequencer)
```

## Running Tests

```bash
cd tb
make SIM=verilator
```

## License

MIT
