# drone/scout/main.py
"""
Scout Drone – starter template.
Simulates area scan and sends fake detections (prints + writes to local JSON log).
Later you'll replace `send_event()` with Firebase/MQTT/MAVLink publishing.
"""

import json, math, os, random, time
from datetime import datetime, timezone
from pathlib import Path

MISSION_ID = os.getenv("MISSION_ID", "demo-mission-001")
LOG_DIR = Path("drone/scout/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Center point (replace with real GPS)
BASE_LAT, BASE_LON = 17.3850, 78.4867  # example: Hyderabad

def jitter(coord, meters):
    """Roughly offset lat/lon by meters (very approximate)."""
    lat, lon = coord
    dlat = meters / 111_111.0
    dlon = meters / (111_111.0 * math.cos(math.radians(lat)))
    return lat + random.uniform(-dlat, dlat), lon + random.uniform(-dlon, dlon)

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def send_event(event: dict):
    """
    For now we just append to a local JSONL log and print.
    Later: publish to Firestore/REST/MQTT.
    """
    line = json.dumps(event, ensure_ascii=False)
    with open(LOG_DIR / f"{MISSION_ID}.jsonl", "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)

def main():
    print(f"[SCOUT] Mission: {MISSION_ID}")
    print("[SCOUT] Starting area scan simulation… Ctrl+C to stop.")
    seq = 0
    try:
        while True:
            seq += 1
            lat, lon = jitter((BASE_LAT, BASE_LON), meters=random.randint(5, 40))
            event = {
                "missionId": MISSION_ID,
                "type": "detection",
                "seq": seq,
                "timestamp": now_iso(),
                "position": {"lat": round(lat, 6), "lon": round(lon, 6)},
                "payload": {
                    "thermalHotspot": bool(random.random() < 0.35),
                    "confidence": round(random.uniform(0.55, 0.98), 2),
                },
                "source": "scout",
            }
            send_event(event)
            time.sleep(1.2)
    except KeyboardInterrupt:
        print("\n[SCOUT] Stopped.")

if __name__ == "__main__":
    main()
