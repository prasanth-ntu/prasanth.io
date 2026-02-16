
# Whisper Setup for Local Audio Transcription (Mac M1 Pro)

## Initial Recommendation from Claude Web

For Mac M1 Pro, the best options for local Whisper transcription:

### Best Option: whisper.cpp (Recommended)
Optimized for Apple Silicon and runs much faster than the Python version:

```bash
# Install via Homebrew
brew install whisper-cpp

# Download a model (medium is good balance of speed/accuracy)
bash ./models/download-ggml-model.sh medium

# Transcribe
whisper-cpp -m models/ggml-medium.bin -f your_audio.m4a
```

### Alternative: Official OpenAI Whisper (Python)

```bash
pip install openai-whisper
whisper your_audio.m4a --model medium --language English
```

### Model Size Recommendations

- **tiny** - Fastest, least accurate
- **base** - Still fast, decent quality
- **small** - Good balance
- **medium** - Better accuracy (recommended for M1 Pro)
- **large** - Best accuracy, slower

---
## Can I use Ollama for transcription?

**No**, Ollama doesn't support speech-to-text models like Whisper. Ollama is specifically designed for running text-based LLMs (like Llama, Mistral, Gemma), not audio processing models.

### Whisper + Ollama Workflow

You can combine them:

1. Use whisper.cpp for transcription
2. Use Ollama for post-processing the transcript

```bash
# 1. Transcribe with Whisper
whisper audio.m4a --model medium > transcript.txt

# 2. Process with Ollama
ollama run llama3.2 "Summarize this transcript: $(cat transcript.txt)"
```

---

## Model Sizes Comparison

|Model|Size|
|---|---|
|**medium.en**|~1.5 GB|
|**large.en**|~2.9 GB|

`large.en` is roughly **2x the size** of `medium.en`.

**Quantized versions** (reduced size, minimal quality loss):

- `medium.en-q5_0` → 539 MB
- `medium.en-q8_0` → 823 MB

Sources:

- [whisper.cpp models README](https://github.com/ggml-org/whisper.cpp/blob/master/models/README.md)
- [Hugging Face whisper.cpp models](https://huggingface.co/ggerganov/whisper.cpp/tree/main)

---

## Setup Steps

### 1. Create dedicated folder for models

```bash
mkdir -p ~/Tools/whisper-cpp/models
```

### 2. Download models from Hugging Face

The Homebrew package doesn't include a download script, so download directly:

```bash
cd ~/Tools/whisper-cpp/models

# Download medium.en (~1.5GB)
curl -L -C - -O https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-medium.en.bin

# Download large-v3 (~3GB) - best quality multilingual
curl -L -C - -O https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3.bin

# Download large-v3-q8_0 (~1.6GB) - quantized, faster
curl -L -C - -O https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-q8_0.bin
```

The `-C -` flag allows resuming if interrupted.

**Note**: There's no `large.en` model for v3 - OpenAI stopped making English-only versions after v2. The `large-v3` multilingual model works great for English.

---

## Transcribing Audio

### Convert audio to WAV first

whisper.cpp can't read `.m4a` files directly - it needs WAV format:

```bash
# Install ffmpeg if needed
brew install ffmpeg

# Convert m4a to wav (16kHz sample rate for Whisper)
ffmpeg -i ~/Downloads/audio.m4a -ar 16000 ~/Downloads/audio.wav
```

### Run transcription

```bash
whisper-cli -m ~/Tools/whisper-cpp/models/ggml-medium.en.bin -f ~/Downloads/audio.wav
```

---

## Saving Transcription Output

By default, whisper-cli only outputs to terminal. To save:

### Option 1: Redirect to file (best for LLM input)

```bash
whisper-cli -m ~/Tools/whisper-cpp/models/ggml-medium.en.bin -f ~/Downloads/audio.wav > ~/Downloads/transcript.txt
```

### Option 2: Built-in output options

```bash
whisper-cli -m ~/Tools/whisper-cpp/models/ggml-medium.en.bin -f ~/Downloads/audio.wav -otxt
```

**Available output formats:**

- `-otxt` - Plain text
- `-osrt` - SRT subtitles (with timestamps)
- `-ovtt` - VTT subtitles
- `-ojson` - JSON format
- `-ocsv` - CSV format

Can combine multiple: `-otxt -osrt`

**For LLM summarization:** Use plain text (option 1 or `-otxt`) - no timestamp clutter, saves tokens.

---

## Speaker Diarization (Multi-Speaker Detection)

**Whisper does NOT detect different speakers** - it only transcribes audio to text.

### Options for speaker detection:

#### 1. WhisperX (best accuracy)

Combines Whisper + pyannote speaker diarization:

```bash
pip install pyannote.audio whisperx
whisperx ~/Downloads/audio.wav --model medium.en --diarize
```

Requires a free Hugging Face token for pyannote.

GitHub: [WhisperX](https://github.com/m-bain/whisperX)

#### 2. Cloud services with built-in speaker detection

- AssemblyAI
- Deepgram
- AWS Transcribe

#### 3. Manual/LLM approach

For use cases like interviews with clear turn-taking, prompt the LLM to infer speakers based on context (interviewer asks questions, interviewee answers).