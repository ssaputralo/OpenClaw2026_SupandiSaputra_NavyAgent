import requests
import re

resp = requests.get('https://repliz.com/assets/index-fhji7pg9.js', timeout=10)
js = resp.text

print("Total JS size:", len(js))

# Look for endpoints near axios or API calls
# Search for "post" or "get" with string patterns
patterns = [
    (r'\.post\([^)]+\)', 'POST calls'),
    (r'\.get\([^)]+\)', 'GET calls'),
    (r'/v1/[a-z]+', 'v1 routes'),
    (r'/comments', 'comments'),
    (r'/chat', 'chat'),
    (r'likeComment', 'likeComment'),
    (r'replyComment', 'replyComment'),
    (r'sendDM', 'sendDM'),
]

for pat, label in patterns:
    matches = re.findall(pat, js, re.I)
    if matches:
        print(f"\n=== {label} ===")
        for m in set(matches[:20]):
            print(f"  {m}")
    else:
        print(f"\n=== {label}: none found ===")
