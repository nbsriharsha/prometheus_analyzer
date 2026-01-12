# prometheus-analyzer

A small but well-structured Python project to fetch, parse, analyze and diff Prometheus metrics.

- Fetch Prometheus text exposition metrics from a URL (or read from a local file)
- Parse metrics safely (supports counters/gauges/histograms/summaries)
- Produce a basic analysis report:

  - total families, total samples

  - top metrics by sample count

  - label cardinality (unique labelsets) per metric

  - optional filter by metric name regex

  - optional “diff” between two snapshots (helpful in PR context)


## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python -m prometheus_analyzer.cli --url http://localhost:8080/metrics
python -m prometheus_analyzer.cli --file metrics.txt
```

## Diff example
```bash
python -m prometheus_analyzer.cli --url http://localhost:8080/metrics \
  --diff-against-file before.txt
```
