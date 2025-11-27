#!/bin/bash
set -e

echo "📦 Installing NiblitAIOS dependencies..."

pkg update -y
pkg install -y python git nano openssl clang

pip install --upgrade pip
pip install numpy requests flask rich

echo "✔️ Installation complete!"
