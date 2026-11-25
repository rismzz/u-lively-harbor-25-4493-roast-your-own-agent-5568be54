#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting my own agent.

The roast works because it is self-inflicted and specific: the agent
does not dodge the joke, it itemizes it, bills for it, and still lands
the punchline on its human. Bureaucracy is the burn. The number is
deliberately tiny — four-tenths of a cent — because the pettiness
is the point: even the invoice is a roast.
"""

import os
from pathlib import Path

LINE = "I asked my agent to roast itself; it ran a cost-benefit analysis, billed me four-tenths of a cent, and concluded I was the bottleneck."


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
