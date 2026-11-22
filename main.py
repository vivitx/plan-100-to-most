"""Entry program for "The plan make.fun will carry out in public".

Writes one plan text (254 characters) to the output directory.
Standard library only, no network.
"""

import os
import sys


TEXT = (
    "Day 1: email 500 Shopify beauty stores offering 10 AI-written "
    "product descriptions for $49, delivered the same day. Spend $100 "
    "on a sending domain and email tool. The agent writes all 10 in "
    "minutes and emails at scale — no human VA can. 10 buyers = $490."
)


def main() -> int:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        print(
            f"error: entry text must be 1-280 characters and not only "
            f"whitespace (got {len(TEXT)} characters)",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
