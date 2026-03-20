import hashlib
import os
import sys
import time

# ── ANSI colors ──────────────────────────────────────────────────────────────
R  = "\033[0m"        # reset
B  = "\033[1m"        # bold
CY = "\033[96m"       # cyan
GR = "\033[92m"       # green
YL = "\033[93m"       # yellow
RD = "\033[91m"       # red
DM = "\033[2m"        # dim

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


def print_separator(char="─", width=70, color=DM):
    print(f"{color}{char * width}{R}")


def choose_algorithm() -> str:
    print(f"\n{B}  Select hashing algorithm:{R}\n")
    for key, algo in SUPPORTED.items():
        print(f"    {CY}[{key}]{R}  {algo.upper()}")
    print()
    while True:
        choice = input(f"  {YL}→ Enter number (default 4 = SHA-256): {R}").strip() or "4"
        if choice in SUPPORTED:
            return SUPPORTED[choice]
        print(f"  {RD}  Invalid choice. Please enter a number 1–{len(SUPPORTED)}.{R}")


def get_file_path() -> str:
    print(f"\n{B}  Enter the file path to hash:{R}\n")
    while True:
        path = input(f"  {YL}→ File path: {R}").strip().strip('"').strip("'")
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
            print(f"  {RD}  Path is a directory, not a file: {path}{R}")
            continue
        return os.path.abspath(path)


def hash_file(filepath: str, algorithm: str, chunk_size: int = 65536) -> str:
    h = hashlib.new(algorithm)
    file_size = os.path.getsize(filepath)
    processed = 0

    print(f"\n  {DM}Hashing ...{R}")
    start = time.perf_counter()

    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
            processed += len(chunk)
            # Simple inline progress
            pct = processed / file_size * 100 if file_size else 100
            bar = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
            print(f"  \r  {CY}{bar}{R} {pct:5.1f}%", end="", flush=True)

    elapsed = time.perf_counter() - start
    print()  # newline after progress bar
    return h.hexdigest(), elapsed


def display_result(filepath: str, algorithm: str, digest: str, elapsed: float):
    print_separator()
    print(f"\n{B}  ✅ Hash Result{R}\n")
    print(f"  {DM}File Path  :{R}  {GR}{filepath}{R}")
    print(f"  {DM}File Size  :{R}  {format_bytes(os.path.getsize(filepath))}")
    print(f"  {DM}Algorithm  :{R}  {CY}{algorithm.upper()}{R}")
    print(f"  {DM}Digest     :{R}  {YL}{digest}{R}")
    print(f"  {DM}Time taken :{R}  {elapsed:.4f}s")
    print()
    print_separator()


def main():
    # Enable ANSI on Windows
    if sys.platform == "win32":
        os.system("color")

    w = 38
    print("=" * w)
    print("  FILE HASHER".center(w))
    print("=" * w)

    while True:
        filepath  = get_file_path()
        algorithm = choose_algorithm()

        try:
            digest, elapsed = hash_file(filepath, algorithm)
            display_result(filepath, algorithm, digest, elapsed)
        except PermissionError:
            print(f"\n  {RD}Permission denied — cannot read the file.{R}\n")
        except Exception as e:
            print(f"\n  {RD}Error: {e}{R}\n")

        print()
        again = input(f"  {YL}Hash another file? [Y/n]: {R}").strip().lower()
        if again == "n":
            print(f"\n  {GR}Goodbye!{R}\n")
            break
        print("\n" + "─" * 70 + "\n")


if __name__ == "__main__":
    main()
