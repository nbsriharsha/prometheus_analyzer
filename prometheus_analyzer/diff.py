def diff_snapshots(a, b):
    sa = {(s.metric_name, s.labels) for f in a.families for s in f.samples}
    sb = {(s.metric_name, s.labels) for f in b.families for s in f.samples}
    return {
        "added": len(sb - sa),
        "removed": len(sa - sb),
    }
