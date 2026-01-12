from prometheus_client.parser import text_string_to_metric_families
from .models import MetricFamilyInfo, SamplePoint

def parse_text_exposition(text: str):
    families = []
    for fam in text_string_to_metric_families(text):
        samples = []
        for s in fam.samples:
            name, labels, value = s[0], s[1], s[2]
            ts = s[3] if len(s) > 3 else None
            samples.append(SamplePoint(name, frozenset(labels.items()), float(value), ts))
        families.append(MetricFamilyInfo(fam.name, fam.type, fam.documentation or '', tuple(samples)))
    return tuple(families)
