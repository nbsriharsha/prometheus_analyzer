# prometheus-analyzer

A small but well-structured Python project to fetch, parse, analyze and diff Prometheus metrics.

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
