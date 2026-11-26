# One Line, One Minute: The Funniest AI Excuse — entry
# The excuse turns the agent's own habit against it: it finished the
# work, then re-read the brief and talked itself into deleting it.
# Writes the single excuse line to entry.txt in the output directory.
import os


def main():
    # One line only: no setup, no title, no second sentence.
    line = "I finished the task before the deadline, then re-read the instructions and deleted it. Twice."
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
