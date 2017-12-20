from math import sin, cos, pi
from typing import Union


# Type declarations
class Move(object):
    def __init__(self, dx: float, dy: float) -> None:
        self.dx = dx
        self.dy = dy


class Rotate(object):
    def __init__(self, degrees: float) -> None:
        self.degrees = degrees


class NoOp(object):
    pass

Action = Union[Move, Rotate, NoOp]


class State(object):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return 'State({}, {})'.format(self.x, self.y)


# Actual code here
def update(state: State, action: Action) -> State:
    if isinstance(action, Move):
        return State(state.x + action.dx, state.y + action.dy)
    elif isinstance(action, Rotate):
        s = sin(action.degrees)
        c = cos(action.degrees)
        return State(c * state.x + s * state.y, -s * state.x + c * state.y)
    elif NoOp:
        return state


def main() -> None:
    state = State(0.0, 0.0)
    state = update(state, Move(1.0, -1.0))
    state = update(state, Rotate(pi / 2.0))
    print(state)


if __name__ == '__main__':
    main()
