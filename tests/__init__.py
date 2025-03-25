import os
import sys

# Path modification to import 'Source' (dir above this one) Packages for test files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import Packages for testing
import main
import tools