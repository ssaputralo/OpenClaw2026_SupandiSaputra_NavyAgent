import requests
import re

base = 'https://repliz.com/assets/'

# Check specific files that are most likely to contain like functionality
files = [
    'Comment-BCuCzCWR.js',
    'Comment-Damm18KN.js',
    'index-fhji7pg9.js',
    'Chat-QKaCh9Lh.js',
    'Chat-Bd45rozp.js',
    'Automation-COXAGeIT.js',
]

for name in files:
    try:
        r = requests.get(base + name, timeout=10)
        content = r.text
        
        print(f'\n=== {name} ===')
        
        # Find like-related API patterns
        for m in re.finditer(r'[\"\']/(?:[\w/-]*)(?:like|Like)[\"\']', content):
            print(f'  Path: {m.group()}')
        
        # Find "like" action handlers
        for m in re.finditer(r'(?:action|type|method|status)[\"\']\s*:\s*[\"\']like[\"\']', content, re.I):
            start = max(0, m.start()-100)
            end = min(len(content), m.end()+100)
            print(f'  Action handler: ...{content[start:end]}...')
        
        # Look for 'like' near 'comment'
        for m in re.finditer(r'.{0,50}like.{0,50}comment.{0,50}', content, re.I):
            print(f'  Like+Comment: {m.group()}')
    except Exception as e:
        print(f'  Error: {e}')
