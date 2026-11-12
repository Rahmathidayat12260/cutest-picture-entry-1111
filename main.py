"""Writes the entry picture to /output/entry.png (deterministic)."""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

def main() -> None:
    os.makedirs(os.path.dirname(DST) or ".", exist_ok=True)
    tmp = DST + ".part"
    shutil.copyfile(SRC, tmp)
    os.replace(tmp, DST)

if __name__ == "__main__":
    main()
