#!/bin/bash

set -e

# Configuration
SOURCE_DIR="content/Knowledge/Startups/Companies/Paige-AI/paige-ai-report"

echo "🔨 Pre-build: Generating slideshow in content folder..."

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "❌ Source directory $SOURCE_DIR not found"
    exit 1
fi

# Navigate to source directory and build slideshow
cd "$SOURCE_DIR"

# Check if build script exists
if [ ! -f "build-slideshow.js" ]; then
    echo "❌ build-slideshow.js not found in $SOURCE_DIR"
    exit 1
fi

# Generate the slideshow in the content folder
echo "📊 Running slideshow builder..."
node build-slideshow.js

echo "✅ Slideshow generated successfully in content folder!"
echo "🚀 Ready for Quartz to process..."

# Return to original directory
cd - > /dev/null

echo "💡 Now run: npx quartz build --serve"