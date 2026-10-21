"""Extract text from two RTF tables and show line-level differences."""
import sys, difflib
from striprtf.striprtf import rtf_to_text

def load(path):
    return rtf_to_text(open(path, encoding="latin-1").read()).splitlines()

ref, new = load(sys.argv[1]), load(sys.argv[2])
diff = list(difflib.unified_diff(ref, new, "reference", "regenerated", lineterm="", n=0))
print("IDENTICAL" if not diff else "\n".join(diff))
