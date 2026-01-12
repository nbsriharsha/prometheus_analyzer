from dataclasses import dataclass
from .models import Snapshot

@dataclass(frozen=True)
class AnalysisReport:
    families: int
    samples: int

def analyze_snapshot(snap: Snapshot) -> AnalysisReport:
    total_samples = sum(len(f.samples) for f in snap.families)
    return AnalysisReport(len(snap.families), total_samples)
