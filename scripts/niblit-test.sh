#!/bin/bash
set -e

PROJECT="$HOME/NiblitAIOS"

echo "🧪 Running NiblitAIOS diagnostics..."

echo "🔍 Checking folder structure..."
for folder in NiblitCore Niblit-Modules Niblit-Hardware Niblit-UI Niblit-Data Niblit-Public; do
    if [ -d "$PROJECT/$folder" ]; then
        echo "✔️ $folder OK"
    else
        echo "❌ Missing: $folder"
    fi
done

echo "🔍 Testing Python imports..."
python3 - <<EOF
try:
    from NiblitCore.core import core
    print("✔️ Core import OK")
except Exception as e:
    print("❌ Core import failed:", e)
EOF

echo "🔍 Checking for Git repo..."
git -C "$PROJECT" status && echo "✔️ Git OK"

echo "✨ Diagnostics complete!"
