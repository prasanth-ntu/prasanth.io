#!/bin/bash

echo "🚀 Building slideshow..."
node build-slideshow.js

if [ $? -eq 0 ]; then
    echo "✅ Build completed successfully!"
    echo "🌐 Open index.html in your browser to view the presentation"
else
    echo "❌ Build failed!"
    exit 1
fi 