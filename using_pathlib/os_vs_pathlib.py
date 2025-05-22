import json
# Instead of juggling strings and manually handling separators (/ or \\),
# Pathing_with_pathlib lets you work with paths as objects
#   — kind of like how you'd use numbers or lists.

# Old way (string-bassed)
import os

path = os.path.join("data", "examplefile.json")
with open(path) as f:
    oldwaydata = json.load(f)

# New way (pathlib)
from pathlib import Path

# Path("data") creates a pathfile object pointing to a folder.
# / is overridden to append paths together.
path = Path("data") / "examplefile.json"
# So "data" / "examplefile.json becomes "data\\creatures.json" automatically
with open(path) as f:
    newwaydata = json.load(f)