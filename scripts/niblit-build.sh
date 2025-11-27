#!/bin/bash
set -e

PROJECT="$HOME/NiblitAIOS"

echo "🔧 Running NiblitAIOS build & structure validator..."

REQUIRED_DIRS=(
    "$PROJECT/NiblitCore"
    "$PROJECT/Niblit-Modules"
    "$PROJECT/Niblit-Hardware"
    "$PROJECT/Niblit-UI"
    "$PROJECT/Niblit-Data"
    "$PROJECT/Niblit-Public"
)

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        echo "📁 Creating missing folder: $dir"
        mkdir -p "$dir"
    else
        echo "✔️ Found: $dir"
    fi
done

echo "🔍 Validating Python path..."
python3 -c "import sys; print('PYTHONPATH OK:', '$PROJECT' in sys.path)"

echo "🔧 Build validation complete!"
