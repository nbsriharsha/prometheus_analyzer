from dataclasses import dataclass
from typing import FrozenSet, Tuple, Optional

LabelSet = FrozenSet[Tuple[str, str]]

@dataclass(frozen=True)
class SamplePoint:
    metric_name: str
    labels: LabelSet
    value: float
    timestamp_ms: Optional[int] = None

@dataclass(frozen=True)
class MetricFamilyInfo:
    name: str
    type: str
    help: str
    samples: Tuple[SamplePoint, ...]

@dataclass(frozen=True)
class Snapshot:
    source: str
    families: Tuple[MetricFamilyInfo, ...]
