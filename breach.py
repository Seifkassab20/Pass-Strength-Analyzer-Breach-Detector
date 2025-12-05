# src/safepass/breach.py
import hashlib
import requests
from pathlib import Path

HIBP_URL = "https://api.pwnedpasswords.com/range/{}"


def sha1_hash(password: str) -> str:
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()


def check_hibp(password: str) -> int:
    """
    Checks the password using HIBP k-anonymity API.
    Returns number of times password appeared in breaches.
    """
    full_hash = sha1_hash(password)
    prefix = full_hash[:5]
    suffix = full_hash[5:]

    response = requests.get(HIBP_URL.format(prefix), timeout=10)

    if response.status_code != 200:
        raise RuntimeError(f"HIBP API error: {response.status_code}")

    for line in response.text.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix == suffix:
            return int(count)

    return 0


def load_local_breach_hashes(path: str) -> set:
    """
    Loads a file of SHA1 hashes (uppercase).
    Each line should contain one SHA1 hash.
    """
    file_path = Path(path)
    if not file_path.exists():
        return set()

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return {line.strip().upper() for line in f}


def check_local_breach(password: str, local_hashes: set) -> bool:
    """
    Checks local breached list.
    Returns True if password is found.
    """
    return sha1_hash(password) in local_hashes

def is_breached(password: str) -> bool:
    local_hashes = load_local_breach_hashes("data/rockyou-hashed.txt")
    hibp_count = check_hibp(password)
    local_hit = check_local_breach(password, local_hashes)
    return hibp_count > 0 or local_hit
