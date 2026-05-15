import requests
import re

# Check Login.js
resp = requests.get('https://repliz.com/assets/Login-BFekdk3r.js', timeout=10)
js = resp.text

print(f"Login.js size: {len(js)} bytes")

# Find API endpoint references
for m in re.finditer(r'["\']([^"\']*api[^"\']*)["\']', js):
    print("API ref:", m.group(1))

# Find any /v1/ references
for m in re.finditer(r'["\'](/v1/[^"\']*)["\']', js):
    print("V1:", m.group(1))

# Find any comment/like/reply references
for m in re.finditer(r'["\']([^"\']*(?:comment|like|reply)[^"\']*)["\']', js, re.I):
    print("Action:", m.group(1))
