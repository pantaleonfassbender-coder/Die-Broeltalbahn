"""Lädt und skaliert die Tafeln nach assets/plates/<id>.jpg und <id>_t.jpg.

    python tools/make-plates.py            # alle Tafeln
    python tools/make-plates.py karte_tal

Commons-Dateien werden über die API in der angegebenen Breite geholt und, wo
angegeben, beschnitten (Rahmen in Promille). Nur gemeinfreie oder CC0-Vorlagen.
"""
import io
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "assets" / "plates"
UA = {"User-Agent": "Mozilla/5.0 (research; Die Broeltalbahn)"}
KARTE = "File:Karte des Deutschen Reiches (5820430c) (5820431c) Detail Siegtal Bröltal.webp"

PLATES = {
    # Modul 1: Das Erz
    "karte_tal": ("commons", KARTE, 3840, (130, 0, 1000, 900)),
    "karte_broel": ("commons", KARTE, 3840, (380, 120, 800, 860)),
    "karte_huette": ("commons", KARTE, 3840, (110, 280, 420, 760)),
}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()


def commons_url(title, width):
    q = urllib.parse.urlencode({"action": "query", "titles": title, "prop": "imageinfo",
                                "iiprop": "url", "iiurlwidth": width, "format": "json"})
    data = json.loads(get("https://commons.wikimedia.org/w/api.php?" + q))
    page = next(iter(data["query"]["pages"].values()))
    return page["imageinfo"][0]["thumburl"]


def make(pid):
    kind, src, width, box = PLATES[pid]
    im = Image.open(io.BytesIO(get(commons_url(src, width) if kind == "commons" else src))).convert("RGB")
    if box:
        W, H = im.size
        im = im.crop((W * box[0] // 1000, H * box[1] // 1000, W * box[2] // 1000, H * box[3] // 1000))
    big = im.copy()
    big.thumbnail((1800, 1600))
    big.save(DEST / f"{pid}.jpg", quality=85, optimize=True)
    t = im.copy()
    t.thumbnail((360, 480))
    t.save(DEST / f"{pid}_t.jpg", quality=82, optimize=True)
    print(pid, big.size, t.size)


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    for pid in sys.argv[1:] or PLATES:
        make(pid)
