
import sys
import os

# Add the current directory to sys.path so we can import 'backend'
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    print(f"Attempting to import backend.council from {current_dir}")
    import backend.council
    print("SUCCESS: backend.council imported successfully.")
except Exception as e:
    print(f"FAILURE: Could not import backend.council. Error: {e}")
    sys.exit(1)
