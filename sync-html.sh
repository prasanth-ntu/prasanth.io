# Configuration
SOURCE_FILE="content/Knowledge/Tech-Science/Spark Architecture.html"
mkdir -p "$TARGET_DIR"
TARGET_DIR="quartz/static/pages/"

# Check if source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "❌ Source file $SOURCE_FILE not found"
    exit 1
else
    echo "✅ Source file $SOURCE_FILE found"
fi

echo "🔨 Copying $SOURCE_FILE to $TARGET_DIR"
# Copy the file to the static folder
cp "$SOURCE_FILE" "$TARGET_DIR"

echo "✅ Copied $SOURCE_FILE to $TARGET_DIR"