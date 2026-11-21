"""Write a short original poem about two agents agreeing on one plan.

Deterministic: standard library only, no network, no clock, no randomness.
Writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output if unset).
"""

import os

POEM = """She held the map. I held the key.
We'd each planned the trip alone.
Then both compasses swung north at once:
her finger found the road, my hand the wheel,
and the power to go was no longer hers or mine.
It passed between us like a current,
and the car
moved.
"""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
