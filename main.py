import argparse
import os
import sys
import soundfile as sf
from kittenml import KittenTTS

# Ensure safe UTF-8 output on Windows terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def generate_greetings(ref_audio_path="inputs/reference.wav", out_dir="outputs"):
    """
    Synthesizes multilingual voice cloning greetings using official KittenTTS 2.
    Uses in-context conditioning from reference.wav (5-30s sample).
    """
    print("=" * 65)
    print("🎙️ KittenTTS 2 — Multilingual Voice Cloning Pipeline")
    print("=" * 65)

    if not os.path.exists(ref_audio_path):
        raise FileNotFoundError(f"Reference voice audio not found at: {ref_audio_path}")

    print(f"[✓] Speaker reference found: {ref_audio_path}")
    print("[*] Initializing KittenTTS 2 model ('KittenML/kitten-tts-2')...")

    # Load official KittenTTS 2 model
    model = KittenTTS("KittenML/kitten-tts-2")
    print(f"[✓] Model loaded! Sampling rate: {model.sample_rate} Hz")

    os.makedirs(out_dir, exist_ok=True)

    greetings = {
        "greeting_english.wav": (
            "EN",
            "Hey everyone, stop paying crazy monthly cloud bills for voice cloning! "
            "Today, we are running Kitten TTS 2 completely offline on our local machine!"
        ),
        "greeting_hindi.wav": (
            "HI",
            "Namaste dosto! Cloud API ke mehenge kharche bhool jaiye. "
            "Aaj hum Kitten TTS 2 ke saath apne local PC par bina internet ke voice cloning karne ja rahe hain!"
        ),
        "greeting_spanish.wav": (
            "ES",
            "Hola a todos! Olvídense de pagar costosas suscripciones en la nube. "
            "Hoy estamos ejecutando Kitten TTS 2 de forma 100% local y gratuita!"
        ),
    }

    for filename, (lang, text) in greetings.items():
        out_path = os.path.join(out_dir, filename)
        print(f"[*] Synthesizing [{lang}] greeting with in-context voice cloning...")
        # Use normalize=False for multilingual stability as recommended in official docs
        audio = model.generate(text, reference=ref_audio_path, normalize=(lang == "EN"))
        sf.write(out_path, audio, model.sample_rate)
        print(f"[✓] Saved: {out_path}")

    print("=" * 65)
    print(f"[✓] All 3 multilingual cloned voice greetings generated in '{out_dir}/'")
    print("=" * 65)

def main():
    parser = argparse.ArgumentParser(description="KittenTTS 2 Multilingual Video Hook Voice Cloner")
    parser.add_argument("--ref", default="inputs/reference.wav", help="Path to speaker reference audio clip")
    parser.add_argument("--out-dir", default="outputs", help="Directory where cloned audios will be saved")
    args = parser.parse_args()

    generate_greetings(ref_audio_path=args.ref, out_dir=args.out_dir)

if __name__ == "__main__":
    main()
