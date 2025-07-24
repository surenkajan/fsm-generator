class FSMError(Exception):
    pass

class InvalidSymbolError(FSMError):
    def __init__(self, symbol: str) -> None:
        super().__init__(f"Invalid input symbol: '{symbol}' not in Σ.")

class InvalidStateError(FSMError):
    def __init__(self, state: str) -> None:
        super().__init__(f"Invalid state: '{state}' not in the FSM state set.")

class ModulusError(FSMError):
    def __init__(self, n: int) -> None:
        super().__init__(f"Modulus must be a positive integer (got {n}).")
