---
name: repliz_tiktok
description: Kumpulan alat untuk berinteraksi dengan TikTok via Repliz API, seperti kirim DM, balas komentar, dan kasih Like.
---

### Implementation

```python
import requests
import json

# Auth via session cookie (didapat dari login browser)
# Base URL tanpa /v1
BASE_URL = "https://api.repliz.com"

def send_tiktok_dm(account_id: str, content_id: str, comment_id: str, text: str):
    """
    Mengirim pesan DM ke user TikTok via Repliz.
    Gunakan ini untuk follow-up leads yang bertanya tentang kursus.
    
    Parameters:
    - account_id: Repliz account ID
    - content_id: TikTok content/video ID (Repliz format)
    - comment_id: ID komentar (sebagai referensi DM)
    - text: Pesan yang akan dikirim
    """
    url = f"{BASE_URL}/content/{content_id}/message"
    payload = {
        "accountId": account_id,
        "commentId": comment_id,
        "text": text
    }
    headers = {
        "Content-Type": "application/json",
        "x-repliz-api-key": "iAv4QhU3G2wXHeHzjHB3xf84pxhufPqU"
    }
    return requests.post(url, json=payload, headers=headers).json()

def reply_tiktok_comment(repliz_comment_id: str, text: str):
    """
    Membalas komentar di postingan TikTok via Repliz.
    Gunakan untuk menjawab pertanyaan publik secara cepat.
    
    Parameters:
    - repliz_comment_id: ID komentar di Repliz (field _id)
    - text: Teks balasan
    """
    url = f"{BASE_URL}/comment/{repliz_comment_id}"
    payload = {"text": text}
    headers = {
        "Content-Type": "application/json",
        "x-repliz-api-key": "iAv4QhU3G2wXHeHzjHB3xf84pxhufPqU"
    }
    return requests.post(url, json=payload, headers=headers).json()

def like_tiktok_comment(comment_id: str):
    """
    Memberikan Like pada komentar TikTok via Repliz.
    Gunakan sebagai bentuk apresiasi awal.
    
    Parameters:
    - comment_id: bisa Repliz comment ID atau TikTok comment ID
    """
    url = f"{BASE_URL}/comment/{comment_id}/like"
    headers = {
        "Content-Type": "application/json",
        "x-repliz-api-key": "iAv4QhU3G2wXHeHzjHB3xf84pxhufPqU"
    }
    return requests.put(url, headers=headers).json()

def reply_tiktok_dm_user(account_id: str, content_id: str, comment_id: str, text: str):
    """
    Kirim DM ke user TikTok (alias dari send_tiktok_dm).
    """
    return send_tiktok_dm(account_id, content_id, comment_id, text)
```
