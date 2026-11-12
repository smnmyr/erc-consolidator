"""sub_live(t, old, new, count=1): replace text outside HTML comments, asserting the hit count."""
import re
def sub_live(t, old, new, count=1):
    spans=[(m.start(),m.end()) for m in re.finditer(r'<!--.*?-->',t,flags=re.S)]
    hits=[m.start() for m in re.finditer(re.escape(old),t) if not any(a<=m.start()<b for a,b in spans)]
    assert len(hits)==count, (old[:60], len(hits))
    for h in reversed(hits): t=t[:h]+new+t[h+len(old):]
    return t
