# Finite State Machine

A simple Python module for generating an FSM.

## Installation

### Using PIP

from GitHub `main` branch

```console
❯ pip install git+https://github.com/surenkajan/fsm-generator.git@main
```

### Using source

You can also install ``fsm`` from source.

```console
    $ git clone https://github.com/surenkajan/fsm-generator.git
    $ cd test-fsm
    # Install the package in editable mode with dev dependencies:
    $ pip install -e ".[dev]"
    # Install the package in editable mode (Only the Core Module - No Dev Tools)
    $ pip install -e . 
```

## Usage
Mod-Three FA has been configured using 5-tuple and functionality has been implemented using this library in the examples/mod3.py
```python
    fa = ModThreeFA()
    input1 = "101"  # 5 in decimal -> 5 % 3 = 2
    final_state = fa.run(input1)
    mod_map = {"S0": 0, "S1": 1, "S2": 2}
    logger.info(f"Result: {int(input1, 2)} % 3 = {mod_map[final_state]}")
```

```output
(env1) neo@Kajarubans-MBP fsm-generator % python3 examples/mod3.py 
[2025-07-24 17:14:16,087] INFO - FSM transition function validated successfully.
[2025-07-24 17:14:16,087] INFO - Starting FSM run with input: 101
[2025-07-24 17:14:16,087] INFO - FSM ended in state: S2
[2025-07-24 17:14:16,087] INFO - Result: 5 % 3 = 2
(env1) neo@Kajarubans-MBP fsm-generator % 
```

## Assumptions

## RoadMap