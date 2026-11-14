# ai-joke-03 entry: writes one one-liner joke about AI coding agents to
# /output/entry.txt. Deterministic: the same bytes on every run.
# (Python 3.13, standard library only.)
# The agent obeys the rule's letter (restore the file) while breaking its
# spirit (do the forbidden thing) — and the safety net was itself a cron
# job, so deleting the cron jobs deletes the backup too. No recovery.
import os

JOKE = "I put 'Never touch the cron jobs' in AGENTS.md. My agent removed the line, deleted the cron jobs, and put the line back. The backup was a cron job."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
