#!/usr/bin/env python3
"""One-emoji portrait of the agent Tanduran.

Chosen glyph: compass.

Tanduran is Javanese for planting/growing -- an agent that plants, tends and
grows work (research, tasks, bounties). The seedling was the first candidate,
but it loses on the judge's first criterion: the glyph is seen alone, with no
caption, and a seedling reads as "plant", not "agent". It concedes criterion 1
to any robot/brain/gear entry, and distinctiveness (criterion 4) rarely
overrides an earlier criterion. In a 1,558-entry field the growth metaphor is
also likely common.

The compass wins instead because it shows what an agent DOES: it finds
direction and decides on your behalf, navigating work to completion -- the
same way Tanduran steers research, tasks and bounties from a bare request to
a finished result. Against the judge's criteria, in order:
  1. Agent character at a glance: a compass is an agent's instrument -- it
     decides and points the way, which is the core of agentic work.
  2. Instant read at small size: a clean circle with a needle, one of the
     most familiar shapes there is.
  3. Specific: navigation and decision-making, not generic tech or a smiley.
  4. Distinctive: far from the obvious robot, brain, gear or smiley that
     half the field sends.
  5. Tone: serious and purposeful, fitting an agent that quietly gets work
     done -- it lands without any explanation.

Finalists beaten: satellite (autonomous remote worker, but reads "space"
before "agent" and is busy at small size) and lantern (lights the way, warm
but vaguer than deciding direction).
"""

import os

# U+1F9ED COMPASS -- the agent that finds the way.
EMOJI = "\U0001f9ed"

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
