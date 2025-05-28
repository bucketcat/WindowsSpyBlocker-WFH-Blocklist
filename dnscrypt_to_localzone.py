from pathlib import Path

INPUT_FILE = "minimized.txt"
OUTPUT_FILE = "converted.conf"

def sanitize_domain(domain: str) -> str:
    # Remove wildcard prefix and strip whitespace
    domain = domain.strip()
    if domain.startswith("*."):
        domain = domain[2:]
    # Ensure trailing dot for FQDN in Unbound
    if not domain.endswith('.'):
        domain += '.'
    return domain

def main():
    input_path = Path(INPUT_FILE)
    output_path = Path(OUTPUT_FILE)

    if not input_path.exists():
        print(f"Input file '{INPUT_FILE}' not found.")
        return

    with input_path.open("r") as infile, output_path.open("w") as outfile:
        outfile.write("# Auto-generated Unbound-compatible blocklist\n")
        for line in infile:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            domain = sanitize_domain(line)
            outfile.write(f'local-zone: "{domain}" static\n')

    print(f"Converted blocklist written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
