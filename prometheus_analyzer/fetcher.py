import requests
from dataclasses import dataclass

@dataclass(frozen=True)
class FetchOptions:
    timeout_s: int = 10
    verify_tls: bool = True

def fetch_from_url(url: str, opts: FetchOptions) -> str:
    r = requests.get(url, timeout=opts.timeout_s, verify=opts.verify_tls)
    r.raise_for_status()
    return r.text

def read_from_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()
