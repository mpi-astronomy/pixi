import pandas as pd
import numpy as np
from colorama import Fore, Style

def main():
    print(Fore.YELLOW + "=== Legacy Environment ===" + Style.RESET_ALL)
    print(f"Pandas version: {pd.__version__}")
    print(f"NumPy version: {np.__version__}")
    
    # Check for older pandas behavior
    if int(pd.__version__.split('.')[0]) < 2:
        print(Fore.GREEN + "✓ Running in expected legacy environment" + Style.RESET_ALL)
    else:
        print(Fore.RED + "⚠ Unexpected version! Are you in the right env?" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
