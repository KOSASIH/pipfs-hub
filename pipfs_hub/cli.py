import argparse

from pipfs_hub.fs import list_packages


def main() -> None:
    """Entry point for the pipfs-hub CLI."""
    parser = argparse.ArgumentParser(description="pipfs-hub CLI")
    parser.add_argument("root_dir", help="Root directory for pip packages")
    args = parser.parse_args()

    try:
        packages = list_packages(args.root_dir)
        print(packages)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
