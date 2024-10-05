
# app/__init__.py

# Importing classes to make them accessible directly from the package
from .operations import Addition, Subtraction, Multiplication, Division

# Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"

# Optional: Initialize any resources or settings
def initialize_app():
    # Placeholder for any initialization code
    print("App initialized")
