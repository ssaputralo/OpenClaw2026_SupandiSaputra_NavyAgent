import requests
import re

resp = requests.get('https://repliz.com/assets/index-fhji7pg9.js', timeout=10)
js = resp.text

# Look for automation/comment related routes
keywords = ['comment', 'like', 'reply', 'dm', 'message', 'inbox', 'automation', 'rule', 'social', 'tiktok']
for kw in keywords:
    # Find patterns like .post("/something/comment") or /comment/ in strings
    pattern = r'["\'][^"\']{0,100}' + kw + r'[^"\']{0,100}["\']'
    matches = re.findall(pattern, js, re.I)
    if matches:
        print(f"\n=== {kw} ===")
        for m in set(matches[:10]):
            print(f"  {m}")
