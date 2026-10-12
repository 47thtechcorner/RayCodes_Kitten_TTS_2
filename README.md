<div align="center">
  <a href="https://youtu.be/sMyTT0HY6ko">
    <img src="https://img.youtube.com/vi/sMyTT0HY6ko/0.jpg" alt="KittenTTS 2: Clone Any Voice Locally In Just 2GB Size!">
  </a>
  <h3>📺 <a href="https://youtu.be/sMyTT0HY6ko">Watch the full tutorial on YouTube</a></h3>
</div>

# 🎙️ KittenTTS 2 Video Dubber

> Zero-shot multilingual voice cloning pipeline that translates video narration into international languages while preserving the original speaker's vocal timbre.

---

## ⚡ 3-Step Workflow

| Step 1: Input | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| Provide 15s reference voice audio in `inputs/reference.wav` | KittenTTS 2 extracts acoustic latents and conditions speech synthesis | 3 Studio-quality cloned greetings in English, Hindi, and Spanish |

---

## 🌟 Key Features

* **Zero-Shot Voice Cloning:** Clones any speaker's voice using only a 15-second audio sample.
* **10+ Language Presets:** Native support for Spanish, Hindi, German, French, Italian, and more.
* **In-Context Conditioning:** Preserves original vocal timbre, pitch cadence, and speaker warmth.
* **100% Local Inference:** Runs entirely offline on your local machine with zero cloud API fees.
* **Studio Audio Quality:** Generates 24 kHz speech with natural human cadence and timbre matching.

---

## 🛠️ Tech Stack

* **AI Model:** KittenTTS 2 (`KittenML/kitten-tts-2`)
* **Framework:** `kittenml` Python runtime (Torch & CUDA accelerated)
* **Audio Processing:** `soundfile`, `torchaudio`
* **Media Normalization:** FFmpeg (24 kHz mono reference extraction)

---

## 📦 Installation & Setup

Copy and run the following command in Windows Antigravity PowerShell to install dependencies:

```powershell
pip install kittenml soundfile torchaudio
```

### Download Model Checkpoint

The official `KittenTTS("KittenML/kitten-tts-2")` engine automatically downloads and caches the verified model weights directly from Hugging Face on the first run.

If you prefer downloading model weights ahead of time:

```powershell
hf download KittenML/kitten-tts-2 --local-dir models/kitten-tts-2
```

---

## 🚀 How to Run

1. Place your 15-second speaker reference audio into `inputs/reference.wav`.
2. Run the voice cloning pipeline:

```powershell
python main.py
```

The script will generate 3 cloned greeting audio files inside the `outputs/` folder:
* `outputs/greeting_english.wav` (English hook)
* `outputs/greeting_hindi.wav` (Hindi hook)
* `outputs/greeting_spanish.wav` (Spanish hook)

---

## 📂 Project Structure

```text
Kitten TTS 2/
├── inputs/
│   └── reference.wav
├── outputs/
│   ├── greeting_english.wav
│   ├── greeting_hindi.wav
│   └── greeting_spanish.wav
├── main.py
└── README.md
```

---

## 💡 Real-World Use Cases

1. **Global YouTube Localization:** Translate tutorial and commentary videos into Spanish, German, and Hindi while retaining your distinct voice.
2. **Multilingual Audiobooks:** Convert book chapters into global editions with character emotion preservation.
3. **E-Learning & Course Creation:** Localize entire video lecture catalogs for international students without re-recording.
4. **Game Character Voiceovers:** Generate dialogue in multiple regional dialects with expressive vocal tags.
5. **Private Corporate Presentations:** Dub internal executive briefings securely without uploading voice data to cloud providers.

---

## 🔮 Future Roadmap

* **Automatic Lip Sync:** Integrate Wav2Lip for matching speaker mouth movements to translated audio.
* **Real-time Whisper Transcription:** Auto-transcribe video speech to text before translation and dubbing.
* **Live Streaming Dubber:** Sub-500ms streaming audio translation for live broadcasts.
* **Speaker Diarization:** Multi-speaker detection to clone multiple conversational voices within a single video.
* **Dynamic Prosody Editor:** Visual UI to adjust pitch contours and speech cadence per sentence.

---

## 🏷️ Keywords & Tags

`KittenTTS 2` `Voice Cloning` `Local AI` `TTS` `Text to Speech` `Zero-Shot Voice Cloning` `Multilingual TTS` `Offline Audio` `KittenML` `Speech Synthesis` `Voice Dubbing` `AI Voice`
