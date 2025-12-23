# Configuration
TARGET_DIR="quartz/static/pages/"
SOURCE_FILES=(
  "content/Knowledge/Tech-Science/Spark Architecture.html"
  "content/Knowledge/Tech-Science/Docker Architecture.html"
)

mkdir -p "$TARGET_DIR"

# Check if source files exist
for SOURCE_FILE in "${SOURCE_FILES[@]}"; do
  if [ ! -f "$SOURCE_FILE" ]; then
      echo "❌ Source file $SOURCE_FILE not found"
      exit 1
  else
      echo "✅ Source file $SOURCE_FILE found"
  fi
done

# Copy files to the static folder
for SOURCE_FILE in "${SOURCE_FILES[@]}"; do
  echo "🔨 Copying $SOURCE_FILE to $TARGET_DIR"
  cp "$SOURCE_FILE" "$TARGET_DIR"
  echo "✅ Copied $SOURCE_FILE to $TARGET_DIR"
done