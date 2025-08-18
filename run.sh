#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")"

# Run the main.py file using Poetry
poetry run python pdf_statements_unlock/main.py

# Keep the terminal open
echo "Press any key to exit..."
read -n 1 -s
