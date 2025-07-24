import pytest

from examples.mod5 import ModFiveFA
from fsm import InvalidSymbolError, build_mod_n_fa


def test_mod_5_basic():
    fa = ModFiveFA()
    mod_map = {f"S{i}": i for i in range(5)}
    test_cases = [
        ("0", 0),
        ("1", 1),
        ("10", 2),
        ("11", 3),
        ("100", 4),
        ("101", 0),
        ("110", 1),
        ("111", 2),
        ("1000", 3),
        ("1001", 4),
        ("1010", 0)
    ]
    for binary_str, expected in test_cases:
        assert mod_map[fa.run(binary_str)] == expected

def test_empty_input():
    fa = build_mod_n_fa(5)
    assert fa.run("") == "S0"

def test_invalid_characters():
    fa = build_mod_n_fa(5)
    with pytest.raises(InvalidSymbolError):
        fa.run("abc")
