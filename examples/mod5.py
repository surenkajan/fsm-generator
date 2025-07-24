from fsm import FiniteAutomaton, build_mod_n_fa, logger


class ModFiveFA:
    """Finite Automaton for computing modulus 3 of binary numbers."""
    def __init__(self) -> None:
        """Initializes the finite automaton with states, alphabet, initial state,
        final states, and transition function."""
        self.fsm: FiniteAutomaton = build_mod_n_fa(5)

    def run(self, input_str: str) -> str:
        return self.fsm.run(input_str)


if __name__ == "__main__":
    fa: ModFiveFA = ModFiveFA()
    input1: str = "10111"  # 23 in decimal -> 23 % 5 = 3
    final_state: str = fa.run(input1)
    mod_map: dict[str, int] = {"S0": 0, "S1": 1, "S2": 2, "S3": 3, "S4": 4}
    logger.info(f"Result: {int(input1, 2)} % 5 = {mod_map[final_state]}")
