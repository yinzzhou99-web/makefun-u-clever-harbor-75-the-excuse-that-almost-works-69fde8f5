"""The Excuse That Almost Works — make.fun entry.

Writes a single excuse line to /output/entry.txt.
The line is the whole entry: a hurried text, no setup, no signature.
Standard library only, no network, deterministic.
"""

import os

LINE = "Boss, the office VPN keeps dropping, IT said don't touch it till Monday, so I'm locked out all week."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
