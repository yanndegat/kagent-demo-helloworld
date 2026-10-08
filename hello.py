"""A very small program for an agent to build, test and review."""
import sys


def greet(name: str = "world", loud: bool = False) -> str:
    message = f"Hello, {name}!"
    if loud:
        return message.upper()
    return message


if __name__ == "__main__":
    print(greet(loud="--loud" in sys.argv))
