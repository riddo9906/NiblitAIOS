#!/bin/bash

echo "🚀 Starting Niblit Core..."

python3 - <<EOF
from NiblitCore.core import core
core.init()
EOF
