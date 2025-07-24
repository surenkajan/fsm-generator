import pytest

from examples.mod3 import ModThreeFA
from fsm import InvalidSymbolError

fa = ModThreeFA()
mod_map = {"S0": 0, "S1": 1, "S2": 2}

def test_mod_three_transitions():
    test_cases = [
        ("0", 0),
        ("1", 1),
        ("10", 2),
        ("11", 0),
        ("100", 1),  # 4 % 3 = 1
        ("101", 2),
        ("110", 0),  # 6 % 3 = 0
        ("111", 1),
        ("1001", 0),  # 9 % 3 = 0
        ("1010", 1),  # 10 % 3 = 1
        ("1111", 0),  # 15 % 3 = 0
    ]
    for binary_str, expected_mod in test_cases:
        final_state = fa.run(binary_str)
        assert mod_map[final_state] == expected_mod, f"Failed on input {binary_str}"

def test_invalid_input():
    with pytest.raises(InvalidSymbolError):
        fa.run("102")  # invalid symbol "2"
