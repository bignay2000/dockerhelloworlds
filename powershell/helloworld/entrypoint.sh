#!/bin/bash
set -x -E -u -o pipefail -e

echo "Entrypoint.sh: Starting Helloworld"
pwsh -File main.ps1