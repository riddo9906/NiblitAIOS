#!/bin/bash
set -e

cd ~/NiblitAIOS

echo "🔄 Syncing with GitHub..."

git add .
MESSAGE="Project sync: $(date +'%Y-%m-%d %H:%M:%S')"

git commit -m "$MESSAGE" || echo "ℹ️ Nothing to commit."

git pull origin main --no-edit || true
git push origin main

echo "✔️ NiblitAIOS is synced to GitHub!"
