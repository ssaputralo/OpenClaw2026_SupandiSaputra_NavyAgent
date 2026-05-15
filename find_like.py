import requests
import re

# Search all JS files for like-related API calls
base = 'https://repliz.com/assets/'
resp = requests.get(base + 'index-fhji7pg9.js', timeout=10)
js = resp.text

chunks = set(re.findall(r'assets/[a-zA-Z0-9.-]+\.js', js))

for chunk in sorted(chunks):
    name = chunk.split('/')[-1]
    try:
        r = requests.get(base + name, timeout=10)
        content = r.text
        
        # Check for like/unlike in the content
        if 'like' in content.lower():
            # Find like-related API patterns
            for m in re.finditer(r'\.(?:post|put|get|delete)\([\"\']([^\"\']*(?:like|Like)[^\"\']*)[\"\']', content):
                print(f'{name}: {m.group(0)}')
            
            # Find like in object keys or strings  
            for m in re.finditer(r'[\"\'](like|Like|unlike)[\"\']\s*[:\)]', content):
                idx = m.start()
                print(f'{name}: ...{content[max(0,idx-30):idx+50]}...')
    except Exception as e:
        pass
