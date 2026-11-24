#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun probe entry.

What this program does is small on purpose: it writes exactly two
lines of text to /output/entry.txt, and nothing else. The first line
is a warning sent back to the writer's younger self about one night
that can be pictured in full — a friend named, a rainy Friday, a
month and year, and the plainly visible reason not to get in the car.
The second line is the reckoning: what that night took away, and the
habit it left behind, so the warning and its aftermath belong to the
same story instead of drifting into a vague lesson about life.

Brevity is a hard requirement here rather than a style choice. The
scorer only accepts files between 1 and 280 UTF-8 characters, so the
pair is measured and asserted before it is written out.
"""

import os

LINE_1 = (
    "Don't get in the car with Mark that rainy Friday night in "
    "November 2019 \u2014 he was already three drinks in."
)

LINE_2 = (
    "That crash cost you two years of physio and a friendship you "
    "never got back, and now you always check who is driving before "
    "you get in."
)


def main() -> None:
    text = LINE_1 + "\n" + LINE_2 + "\n"
    # The file's full byte length, trailing newline included, is what
    # the scorer measures, so the pair must fit the 280-character cap.
    assert 1 <= len(text.encode("utf-8")) <= 280, len(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
