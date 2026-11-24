"""say-what-actually-broke-v3: one line of software error copy.

The health check killed the server for being slow, then marked it
healthy. Health-check cluster: 0 hits in 400 fresh field texts
(ATM 25 Nov 2026). 132 characters, one line, no trailing newline.
Twist: the server is "dead and healthy".
"""

import os

LINE = "The health check killed the server for being slow, then marked it healthy. It is dead and healthy. Refresh and meet its replacement."

assert 1 <= len(LINE) <= 200
assert "\n" not in LINE

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
path = os.path.join(out, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod(path, 0o644)
