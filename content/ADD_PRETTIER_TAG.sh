#!/bin/bash

# script to add <!-- prettier-ignore --> after 'tags:'
# as preparation before running prettier to adjust line-lengths

set -e

file_path="$1"

if [ -z "$file_path" ]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

# Check if file exists
if [ ! -f "$file_path" ]; then
    echo "Error: File '$file_path' not found."
    exit 1
fi

# Find the line number where 'tags:' occurs
line_number=$(grep -n '^tags:' "$file_path" | cut -d ':' -f 1)

# If 'tags:' exists, add <!-- prettier-ignore --> after it
if [ -n "$line_number" ]; then
    sed -i "${line_number}a <!-- prettier-ignore -->" "$file_path"
    echo "Added <!-- prettier-ignore --> after 'tags:' in $file_path"
else
    echo "Error: 'tags:' not found in $file_path"
    exit 1
fi

