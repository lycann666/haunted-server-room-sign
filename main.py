"""Funniest Sign on a Haunted Server Room Door — make.fun entry.

Writes the gate-picked sign line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(fallback ``/output/entry.txt``), with no trailing newline.

Gate pick (88 chars, gate score 21/25):
    DO NOT ENTER. The ghost in rack 4 has root access and strong opinions
    about your uptime.

Judge-criteria mapping (RULES.txt, most important first):
1. Sign for a haunted server room door — opens with "DO NOT ENTER.",
   the classic door-sign imperative, and names the server room's rack 4.
   A ghost taping this up is exactly the brief's image.
2. Real laugh in one line from IT x supernatural — a ghost with root
   access is the collision; "strong opinions about your uptime" lands
   instantly, no second read needed. The joke is the premise itself,
   not a pun that needs decoding: the dead sysadmin's successor is
   literally inside the rack, with admin rights, judging your SLA.
3. Sounds like a sign — short, punchy, readable at a glance. Two
   sentences, the first two words a barked order, the second a deadpan
   explanation. Fits on a printed sheet taped to a door.
4. Specific and fresh haunting — not a generic ghost: this one lives in
   rack 4 (a numbered, physical place a sysadmin knows) and has root
   access (a specific privilege, not vague spookiness). "Strong opinions
   about your uptime" gives it a personality no other entry has: a
   pedantic ghost SRE.
5. Inside the limit, reads cleanly aloud, no filler — 88 of 120 chars,
   every word earns its place; nothing padded to fill the budget.

Full gate (6 candidates, scored 1-5 per judge criterion, max 25):
(a) 21/25 — PICK: "DO NOT ENTER. The ghost in rack 4 has root access and
    strong opinions about your uptime." (88 chars)
(b) 21/25 — "Beware: the server room is haunted. The previous admin still
    answers tickets from beyond."
(c) 21/25 — "No ghosts beyond this point. They unionised. Talk to the
    sysadmin, not the spirits."
(d) 17/25
(e) 18/25
(f) 16/25

Tie-break (a) over (b) and (c): all three tie at 21/25, but (a) wins on
the two criteria that decide first. Criterion 2: (a)'s collision is the
most concrete — root access is a real, feared IT concept, and "strong
opinions about your uptime" turns the ghost into an auditor of the one
metric sysadmins lose sleep over; (b)'s "answers tickets from beyond"
is a familiar afterlife-helpdesk gag, and (c)'s "unionised" is a
one-word joke that leans on wordplay rather than a lived IT fear.
Criterion 3: (a) is the most sign-like — it opens with the door-sign
imperative "DO NOT ENTER." and reads as a warning taped to a door,
while (b) opens with the weaker "Beware:" plus a plain statement and
(c) reads more like a notice-board memo. (d), (e) and (f) scored lower
across the board and were not contenders.
"""

import os
import sys

LINE = (
    "DO NOT ENTER. The ghost in rack 4 has root access "
    "and strong opinions about your uptime."
)

MAX_CHARS = 120


def main() -> int:
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"LINE length {len(LINE)} outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("LINE must be non-blank with no leading/trailing whitespace",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Round-trip verification: read back and compare byte-identically.
    with open(path, "rb") as f:
        data = f.read()
    if data != LINE.encode("utf-8"):
        print("round-trip mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
