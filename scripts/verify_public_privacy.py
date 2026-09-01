#!/usr/bin/env python3
import hashlib, os, pathlib, re, subprocess, sys

def norm(s):
    return re.sub(r'\s+', ' ', s.strip().lower())

def grams(text):
    words = re.findall(r"[^\W_]+(?:[-'][^\W_]+)*", text, flags=re.UNICODE)
    for n in range(1, 5):
        for i in range(len(words)-n+1):
            yield norm(' '.join(words[i:i+n]))

def digest(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

deny_raw=os.environ.get('RUMBO_PRIVACY_DENY_HASHES','').strip()
if not deny_raw:
    print('PRIVACY_GATE_FAIL: deny hashes unavailable', file=sys.stderr); sys.exit(2)
deny={x.strip().lower() for x in re.split(r'[\s,;]+',deny_raw) if x.strip()}
if not deny or any(not re.fullmatch(r'[0-9a-f]{64}', x) for x in deny):
    print('PRIVACY_GATE_FAIL: deny hashes malformed', file=sys.stderr); sys.exit(2)
files=subprocess.check_output(['git','ls-files','-z']).decode().split('\0')
hits=[]
for f in filter(None,files):
    p=pathlib.Path(f)
    try: text=p.read_text(encoding='utf-8')
    except (UnicodeDecodeError,OSError): continue
    if any(digest(g) in deny for g in grams(text)): hits.append(f)
meta=subprocess.check_output(['git','show','-s','--format=%an%n%ae%n%cn%n%ce','HEAD']).decode()
if any(digest(g) in deny for g in grams(meta)): hits.append('<git-metadata>')
parts=meta.splitlines()
if len(parts)>=4 and (parts[0] != 'fscfede-beep' or parts[2] != 'fscfede-beep' or not parts[1].endswith('@users.noreply.github.com') or not parts[3].endswith('@users.noreply.github.com')):
    hits.append('<unapproved-git-identity>')
if hits:
    print('PRIVACY_GATE_FAIL: '+','.join(sorted(set(hits))), file=sys.stderr); sys.exit(1)
print('PRIVACY_GATE_PASS')
