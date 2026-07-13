import json
import re
from collections import Counter

INPUT_PATH = "/app/data/access.log"
OUTPUT_PATH = "/app/report.json"

def main():
    paths = Counter()
    ips = set()
    total = 0

    with open(INPUT_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            # Extract IP (first field)
            parts = line.split()
            if parts:
                ips.add(parts[0])
            # Extract request path
            match = re.search(r'"[A-Z]+\s+([^\s]+)\s+HTTP', line)
            if match:
                paths[match.group(1)] += 1

    top_path = paths.most_common(1)[0][0] if paths else ""

    result = {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": top_path
    }

    with open(OUTPUT_PATH, "w") as out:
        json.dump(result, out, indent=2)

if __name__ == "__main__":
    main()
