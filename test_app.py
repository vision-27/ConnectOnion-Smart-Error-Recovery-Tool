#!/usr/bin/env python3
"""
Test application that will fail with common errors
This is used to demonstrate the error recovery tool
"""

# This will cause a ModuleNotFoundError if requests is not installed
import requests
import json

def main():
    print("🚀 Starting test application...")
    
    # This will fail if requests is not installed
    response = requests.get("https://httpbin.org/json")
    data = response.json()
    
    print("✅ Application started successfully!")
    print(f"📊 Received data: {data}")

if __name__ == "__main__":
    main()
