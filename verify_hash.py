import hashlib
import os
import sys
import time

# ── ANSI colors ──────────────────────────────────────────────────────────────
R  = "\033[0m"
B  = "\033[1m"
CY = "\033[96m"
GR = "\033[92m"
YL = "\033[93m"
RD = "\033[91m"
DM = "\033[2m"
MG = "\033[95m"

SUPPORTED = {
    "1": "md5",
    "2": "sha1",
    "3": "sha224",
    "4": "sha256",
    "5": "sha384",
    "6": "sha512",
    "7": "sha3_256",
    "8": "sha3_512",
    "9": "blake2b",
}


def format_bytes(size: int) -> str:
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024:
            return f"{size:.2f} {unit}" if unit != "B" else f"{size} B"
        size /= 1024
    return f"{size:.2f} PB"


def print_sep(char="─", width=72, color=DM):
    print(f"{color}{char * width}{R}")


def get_file_path() -> str:
    print(f"\n{B}  Step 1 — File to verify:{R}\n")
    while True:
        path = input(f"  {YL}→ Enter file path: {R}").strip().strip('"').strip("'")
        if not path:
            print(f"  {RD}  Path cannot be empty.{R}")
            continue
        if not os.path.exists(path):
            print(f"  {RD}  File not found: {path}{R}")
            retry = input(f"  {YL}  Try again? [Y/n]: {R}").strip().lower()
            if retry == "n":
                sys.exit(0)
            continue
        if not os.path.isfile(path):
            print(f"  {RD}  That is a directory, not a file.{R}")
            continue
        return os.path.abspath(path)


def choose_algorithm() -> str:
    print(f"\n{B}  Step 2 — Hashing algorithm:{R}\n")
    for key, algo in SUPPORTED.items():
        print(f"    {CY}[{key}]{R}  {algo.upper()}")
    print()
    while True:
        choice = input(f"  {YL}→ Enter number (default 4 = SHA-256): {R}").strip() or "4"
        if choice in SUPPORTED:
            return SUPPORTED[choice]
        print(f"  {RD}  Invalid — enter 1–{len(SUPPORTED)}.{R}")


def get_expected_hash() -> str:
    print(f"\n{B}  Step 3 — Known / expected hash:{R}\n")
    while True:
        digest = input(f"  {YL}→ Paste the expected hash: {R}").strip()
        if not digest:
            print(f"  {RD}  Hash cannot be empty.{R}")
            continue
        # Basic sanity: must be hex
        try:
            bytes.fromhex(digest)
        except ValueError:
            print(f"  {RD}  That doesn't look like a valid hex hash. Try again.{R}")
            continue
        return digest.lower()


def compute_hash(filepath: str, algorithm: str, chunk_size: int = 65536) -> tuple[str, float]:
    h = hashlib.new(algorithm)
    file_size = os.path.getsize(filepath)
    processed = 0

    print(f"\n  {DM}Computing hash...{R}")
    start = time.perf_counter()

    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
            processed += len(chunk)
            pct = processed / file_size * 100 if file_size else 100
            bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
            print(f"  \r  {CY}{bar}{R} {pct:5.1f}%", end="", flush=True)

    elapsed = time.perf_counter() - start
    print()
    return h.hexdigest(), elapsed


def diff_hashes(computed: str, expected: str) -> str:
    """Return a colored char-by-char diff of two hex strings."""
    result = ""
    max_len = max(len(computed), len(expected))
    comp_padded = computed.ljust(max_len)
    exp_padded  = expected.ljust(max_len)
    for c, e in zip(comp_padded, exp_padded):
        result += f"{GR}{c}{R}" if c == e else f"{RD}{c}{R}"
    return result


def display_result(filepath: str, algorithm: str, computed: str,
                   expected: str, elapsed: float):
    match = computed == expected

    print_sep("═", color=MG)
    print()

    if match:
        print(f"  {GR}{B}  ✅  HASH VERIFIED — File is AUTHENTIC{R}\n")
    else:
        print(f"  {RD}{B}  ❌  HASH MISMATCH — File may be CORRUPTED or TAMPERED{R}\n")

    print(f"  {DM}File Path  :{R}  {GR}{filepath}{R}")
    print(f"  {DM}File Size  :{R}  {format_bytes(os.path.getsize(filepath))}")
    print(f"  {DM}Algorithm  :{R}  {CY}{algorithm.upper()}{R}")
    print(f"  {DM}Time taken :{R}  {elapsed:.4f}s")
    print()
    print(f"  {DM}Expected   :{R}  {YL}{expected}{R}")
    print(f"  {DM}Computed   :{R}  {diff_hashes(computed, expected)}")

    if not match:
        # Show which byte positions differ
        mismatches = sum(1 for a, b in zip(computed, expected) if a != b)
        print(f"\n  {RD}  {mismatches} character(s) differ out of {len(expected)}.{R}")
        print(f"  {DM}  (mismatched characters highlighted in {RD}red{R}{DM} above){R}")

    print()
    print_sep("═", color=MG)


def main():
    if sys.platform == "win32":
        os.system("color")

    w = 38
    print("=" * w)
    print("  HASH VERIFIER".center(w))
    print("=" * w)

    while True:
        filepath  = get_file_path()
        algorithm = choose_algorithm()
        expected  = get_expected_hash()

        try:
            computed, elapsed = compute_hash(filepath, algorithm)
            display_result(filepath, algorithm, computed, expected, elapsed)
        except PermissionError:
            print(f"\n  {RD}Permission denied — cannot read the file.{R}\n")
        except Exception as e:
            print(f"\n  {RD}Error: {e}{R}\n")

        print()
        again = input(f"  {YL}Verify another file? [Y/n]: {R}").strip().lower()
        if again == "n":
            print(f"\n  {GR}Goodbye!{R}\n")
            break
        print("\n" + "─" * 72 + "\n")


if __name__ == "__main__":
    main()
