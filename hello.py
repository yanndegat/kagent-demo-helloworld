"""A very small program for an agent to build, test and review."""


def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
