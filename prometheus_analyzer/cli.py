import argparse
from .fetcher import fetch_from_url, read_from_file, FetchOptions
from .parser import parse_text_exposition
from .models import Snapshot
from .analysis import analyze_snapshot

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--url')
    p.add_argument('--file')
    args = p.parse_args()

    if args.url:
        text = fetch_from_url(args.url, FetchOptions())
        src = args.url
    else:
        text = read_from_file(args.file)
        src = args.file

    families = parse_text_exposition(text)
    snap = Snapshot(src, families)
    report = analyze_snapshot(snap)

    print(f"Source: {src}")
    print(f"Metric families: {report.families}")
    print(f"Samples: {report.samples}")

if __name__ == '__main__':
    main()
