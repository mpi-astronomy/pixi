import os
import platform
import sys

def main():
    print("=== Reproducibility Check ===")
    print(f"OS/Platform: {platform.platform()}")
    print(f"Python: {sys.version.split()[0]}")
    
    print("\nEnvironment Variables (via [activation]):")
    print(f"OBSERVATORY_CODE: {os.environ.get('OBSERVATORY_CODE', 'NOT SET')}")
    print(f"DATA_DIR: {os.environ.get('DATA_DIR', 'NOT SET')}")

    if os.environ.get('OBSERVATORY_CODE') == "XYZ":
        print("\nSUCCESS: Environment variables loaded correctly.")
    else:
        print("\nFAILURE: Environment variables missing.")

if __name__ == "__main__":
    main()
