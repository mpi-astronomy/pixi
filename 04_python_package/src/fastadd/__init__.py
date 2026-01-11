try:
    from .cexample import fast_add
except ImportError:
    # Fallback if C extension not compiled/available
    print("Warning: C extension not found. fast_add will not be available.")

def test():
    print("Testing fastadd...")
    result = fast_add(1.5, 2.5)
    print(f"C extension fast_add(1.5, 2.5) = {result}")
    return "Success"
