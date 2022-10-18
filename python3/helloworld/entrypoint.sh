#!/bin/bash
set -x -E -u -o pipefail -e

echo "Entrypoint.sh: Starting Helloworld"
exec python3 main.py