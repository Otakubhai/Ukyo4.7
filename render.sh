#!/usr/bin/env bash
# This script is used by Render.com to start the service

# Exit on error
set -o errexit

pip install -r requirements.txt
python merged_bot.py
