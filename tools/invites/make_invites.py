"""Generate Sideris invite codes.

    python tools/invites/make_invites.py 20 --label "UC3M group 45"

Writes two files into tools/invites/out/ (gitignored, never commit it):
  * codes-<stamp>.csv  the codes to hand out, one per person, with their sign-up link
                       (--site sets the portal address; keep this file private)
  * codes-<stamp>.sql  the INSERT to paste in the Supabase SQL editor; it holds only the
                       SHA-256 of each code, exactly as public.invite_hash() computes it

Codes look like SIDR-7KQ4-M9XC: 8 random characters from an alphabet without look-alikes
(no 0/O, 1/I/L), about 40 bits each, from the operating system's secure generator.
"""
import argparse
import csv
import datetime
import hashlib
import pathlib
import re
import secrets

ALPHABET = '23456789ABCDEFGHJKMNPQRSTUVWXYZ'


def new_code():
    body = ''.join(secrets.choice(ALPHABET) for _ in range(8))
    return 'SIDR-' + body[:4] + '-' + body[4:]


def code_hash(code):
    """Same normalisation as public.invite_hash(): spaces removed, upper case."""
    return hashlib.sha256(re.sub(r'\s', '', code).upper().encode()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('count', type=int, help='how many codes')
    ap.add_argument('--label', default='', help='a note stored with each code (who it is for)')
    ap.add_argument('--expires', default='', help='optional expiry date, YYYY-MM-DD')
    ap.add_argument('--site', default='https://251-b.github.io/AerospaceEngineering/',
                    help='address of the portal, for the sign-up link of each code')
    ap.add_argument('--out', default=str(pathlib.Path(__file__).parent / 'out'))
    args = ap.parse_args()
    if not 1 <= args.count <= 1000:
        ap.error('count must be between 1 and 1000')

    codes = set()
    while len(codes) < args.count:
        codes.add(new_code())
    codes = sorted(codes)

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    with open(out / f'codes-{stamp}.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['code', 'label', 'link'])
        site = args.site.rstrip('/') + '/'
        for c in codes:
            w.writerow([c, args.label, f'{site}account/signup.html?invite={c}'])

    label = args.label.replace("'", "''")
    expires = f"'{args.expires}'::timestamptz" if args.expires else 'null'
    label_sql = f"'{label}'" if label else 'null'
    rows = ',\n'.join(f"  ('{code_hash(c)}', {label_sql}, {expires})" for c in codes)
    sql = ('-- Sideris invite codes (hashes only). Paste in Supabase > SQL Editor and run.\n'
           'insert into public.invite_codes (code_hash, label, expires_at) values\n' + rows +
           '\non conflict (code_hash) do nothing;\n')
    (out / f'codes-{stamp}.sql').write_text(sql)
    print(f'{len(codes)} codes')
    print(f'  hand out: {out / f"codes-{stamp}.csv"}')
    print(f'  load:     {out / f"codes-{stamp}.sql"}')


if __name__ == '__main__':
    main()
