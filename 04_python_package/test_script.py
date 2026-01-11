import sys

print(f"Python version: {sys.version}")

try:
    import fastadd
    print("Successfully imported fastadd")
    
    # Run the internal test function
    result = fastadd.test()
    print(f"Test result: {result}")
    
    # Verify fast_add
    val = fastadd.fast_add(10, 20)
    print(f"fast_add(10, 20) = {val}")
    
except ImportError as e:
    print(f"Failed to import fastadd: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
