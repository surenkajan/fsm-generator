from .exceptions import InvalidStateError, InvalidSymbolError
from .logger import logger


class FiniteAutomaton:
    def __init__(
        self,
        states: set[str],
        alphabet: set[str],
        initial_state: str,
        final_states: set[str],
        transition_function: dict[tuple[str, str], str]
    ) -> None:
        """Initialize the finite automaton (FA) using the 5-tuple definition.
        :param states: (Q) A set of states in the FSM.
        :param alphabet: (Σ) : A set of symbols in the FSM's alphabet.
        :param initial_state: (q0) The initial state of the FSM.
        :param final_states: (F) A set of final (accepting) states in the FSM.
        :param transition_function: (δ) A dictionary mapping (state, symbol) to target
        state.
        """
        self.states: set[str] = set(states)
        self.alphabet: set[str] = set(alphabet)
        self.initial_state: str = initial_state
        self.final_states: set[str] = set(final_states)
        self.transition_function: dict[tuple[str, str], str] = transition_function

        self._validate_fa()

    def _validate_fa(self) -> None:
        """Validates the finite automaton's structure.
        Raises:
            InvalidStateError: If the initial state or any final state is not in the set
            of states.
            InvalidSymbolError: If any transition uses a symbol not in the alphabet.
            InvalidStateError: If any transition state or target state is not in the set
            of states
        """
        if self.initial_state not in self.states:
            logger.error("Initial state '%s' is not in the set of states",
                         self.initial_state)
            raise InvalidStateError(self.initial_state)
        if not self.final_states.issubset(self.states):
            for state in self.final_states - self.states:
                logger.error("Final state '%s' is invalid", state)
                raise InvalidStateError(state)
        for (state, symbol), target_state in self.transition_function.items():
            if state not in self.states:
                logger.error("Transition state '%s' is invalid", state)
                raise InvalidStateError(state)
            if symbol not in self.alphabet:
                logger.error("Transition symbol '%s' is invalid", symbol)
                raise InvalidSymbolError(symbol)
            if target_state not in self.states:
                logger.error("Target state '%s' is invalid", target_state)
                raise InvalidStateError(target_state)
        logger.info("FSM transition function validated successfully.")


    def run(self, input_str: str) -> str:
        """Runs the finite automaton on an input string and returns the final state.
        :param input_str: The input string to process.
        :return: The final state after processing the input string.
        :raises InvalidSymbolError: If an invalid symbol is encountered in the input.
        """
        current_state = self.initial_state
        logger.info("Starting FSM run with input: %s", input_str)

        for symbol in input_str:
            if symbol not in self.alphabet:
                logger.error("Invalid symbol encountered: '%s'", symbol)
                raise InvalidSymbolError(symbol)
            prev_state = current_state
            current_state = self.transition_function[(current_state, symbol)]
            logger.debug("Transition: %s --%s--> %s", prev_state, symbol, current_state)

        logger.info("FSM ended in state: %s", current_state)
        return current_state

    def accepts(self, input_str: str) -> bool:
        """Returns True if the input string ends in an accepting state.
        :param input_str: The input string to process.
        :return: True if the final state is an accepting state, False otherwise.
        """
        final_state = self.run(input_str)
        return final_state in self.final_states

