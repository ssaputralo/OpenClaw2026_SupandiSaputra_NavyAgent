import requests
import re

resp = requests.get('https://repliz.com/assets/index-fhji7pg9.js', timeout=10)
js = resp.text

# Find all backtick template strings containing comment/like
print("=== Backtick templates with comment/like/reply ===")
for m in re.finditer(r'`[^`]{0,100}(?:comment|like|reply)[^`]{0,100}`', js, re.IGNORECASE):
    print(m.group())

# Also find object keys with comment/like related terms
print("\n=== Object keys ===")
for m in re.finditer(r'["\'](comment|like|reply|dm|message)["\']\s*:', js, re.IGNORECASE):
    print(m.group())

# Find v1 API routes
print("\n=== v1 API routes ===")
for m in re.finditer(r'["\'][^"\']{0,50}/v1/[^"\']{0,50}["\']', js):
    print(m.group())
