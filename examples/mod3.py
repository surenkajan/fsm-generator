from fsm import FiniteAutomaton, logger


class ModThreeFA:
    """Finite Automaton for computing modulus 3 of binary numbers."""
    def __init__(self) -> None:
        """Initializes the finite automaton with states, alphabet, initial state,
        final states, and transition function."""
        Q: set[str] = {"S0", "S1", "S2"}
        Σ: set[str] = {"0", "1"}
        q0: str = "S0"
        F: set[str] = {"S0", "S1", "S2"}
        δ: dict[tuple[str, str], str] = {
            ("S0", "0"): "S0",
            ("S0", "1"): "S1",
            ("S1", "0"): "S2",
            ("S1", "1"): "S0",
            ("S2", "0"): "S1",
            ("S2", "1"): "S2",
        }

        self.fsm: FiniteAutomaton = FiniteAutomaton(Q, Σ, q0, F, δ)

    def run(self, input_str: str) -> str:
        return self.fsm.run(input_str)


if __name__ == "__main__":
    fa = ModThreeFA()
    input1 = "101"  # 5 in decimal -> 5 % 3 = 2
    final_state = fa.run(input1)
    mod_map = {"S0": 0, "S1": 1, "S2": 2}
    logger.info(f"Result: {int(input1, 2)} % 3 = {mod_map[final_state]}")
