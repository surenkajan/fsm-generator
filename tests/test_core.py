import pytest

from fsm import (
    FiniteAutomaton,
    InvalidStateError,
    InvalidSymbolError,
)


def test_finite_automaton_init_and_validate():
    Q = {"S0", "S1"}
    Σ = {"0", "1"}
    q0 = "S0"
    F = {"S0"}
    δ = {("S0", "0"): "S0", ("S0", "1"): "S1", ("S1", "0"): "S0", ("S1", "1"): "S1"}
    fa = FiniteAutomaton(Q, Σ, q0, F, δ)
    assert fa.states == Q
    assert fa.alphabet == Σ
    assert fa.initial_state == q0
    assert fa.final_states == F
    assert fa.transition_function == δ

def test_finite_automaton_invalid_initial_state():
    Q = {"S0", "S1"}
    Σ = {"0", "1"}
    q0 = "S2"  # Invalid
    F = {"S0"}
    δ = {("S0", "0"): "S0", ("S0", "1"): "S1", ("S1", "0"): "S0", ("S1", "1"): "S1"}
    with pytest.raises(InvalidStateError):
        FiniteAutomaton(Q, Σ, q0, F, δ)

def test_finite_automaton_invalid_final_state():
    Q = {"S0", "S1"}
    Σ = {"0", "1"}
    q0 = "S0"
    F = {"S2"}  # Invalid
    δ = {("S0", "0"): "S0", ("S0", "1"): "S1", ("S1", "0"): "S0", ("S1", "1"): "S1"}
    with pytest.raises(InvalidStateError):
        FiniteAutomaton(Q, Σ, q0, F, δ)

def test_finite_automaton_invalid_symbol_in_transition():
    Q = {"S0", "S1"}
    Σ = {"0", "1"}
    q0 = "S0"
    F = {"S0"}
    δ = {("S0", "2"): "S1"}  # Invalid symbol
    with pytest.raises(InvalidSymbolError):
        FiniteAutomaton(Q, Σ, q0, F, δ)

def test_finite_automaton_invalid_target_state_in_transition():
    Q = {"S0", "S1"}
    Σ = {"0", "1"}
    q0 = "S0"
    F = {"S0"}
    δ = {("S0", "0"): "S2"}  # Invalid target state
    with pytest.raises(InvalidStateError):
        FiniteAutomaton(Q, Σ, q0, F, δ)

def test_run_method():
    Q = {"S0", "S1"}
    Σ = {"0", "1"}
    q0 = "S0"
    F = {"S0"}
    δ = {("S0", "0"): "S0", ("S0", "1"): "S1", ("S1", "0"): "S0", ("S1", "1"): "S1"}
    fa = FiniteAutomaton(Q, Σ, q0, F, δ)
    assert fa.run("0") == "S0"
    assert fa.run("1") == "S1"
    assert fa.run("10") == "S0"
    with pytest.raises(InvalidSymbolError):
        fa.run("2")

def test_accepts_method():
    Q = {"S0", "S1"}
    Σ = {"0", "1"}
    q0 = "S0"
    F = {"S1"}
    δ = {("S0", "0"): "S0", ("S0", "1"): "S1", ("S1", "0"): "S0", ("S1", "1"): "S1"}
    fa = FiniteAutomaton(Q, Σ, q0, F, δ)
    assert fa.accepts("1") is True
    assert fa.accepts("0") is False

