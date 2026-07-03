#!/bin/bash

# Navigate to the project root (parent of this scripts/ directory)
cd "$(dirname "$0")/.."

# Unlock all PDFs in private_data/files using Poetry
poetry run python scripts/unlock_files.py

# Keep the terminal open
echo "Press any key to exit..."
read -n 1 -s
