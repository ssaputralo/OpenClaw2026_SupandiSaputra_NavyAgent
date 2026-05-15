import requests
import re

# Check comment service
services = [
    'https://repliz.com/assets/comment.service-SWj2QyeB.js',
    'https://repliz.com/assets/automation.service-Da7-i4xR.js',
    'https://repliz.com/assets/account.tiktok.service-Cf0swyI0.js',
]

for url in services:
    try:
        resp = requests.get(url, timeout=10)
        js = resp.text
        print(f"\n=== {url.split('/')[-1]} ({len(js)} bytes) ===")
        
        # Find API routes/paths
        for m in re.finditer(r'["\']/[^"\']{1,100}["\']', js):
            path = m.group()
            if any(kw in path.lower() for kw in ['comment', 'like', 'reply', 'dm', 'chat', 'send', 'message']):
                print(f"  Route: {path}")
                
        # Find function names
        for m in re.finditer(r'(?:like|reply|send|comment|get|post|put|delete)\w*(?=\s*[=:]\s*(?:async)?\s*[\(\[]', js):
            print(f"  Func: {m.group()}")
    except Exception as e:
        print(f"\n=== {url} === Error: {e}")
