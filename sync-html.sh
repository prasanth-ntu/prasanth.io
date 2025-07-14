# Configuration
SOURCE_FILE="content/Knowledge/Tech-Science/Spark Architecture.html"
TARGET_DIR="static/pages/"

# Check if source file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "❌ Source file $SOURCE_FILE not found"
    exit 1
fi


# Copy the file to the static folder
cp "$SOURCE_FILE" "$TARGET_DIR"