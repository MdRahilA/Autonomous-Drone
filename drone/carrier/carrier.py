# drone/carrier/main.py
"""
Carrier Drone – starter template.
Simulates following a route and performing a payload drop.
For now it logs JSON lines locally. Later, swap send_event() to Firestore/MQTT.
"""

import json, math, os, random, time
from datetime import datetime, timezone
from pathlib import Path

MISSION_ID = os.getenv("MISSION_ID", "demo-mission-001")
LOG_DIR = Path("drone/carrier/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Start / target (replace with real GPS)
START_LAT, START_LON = 17.3850, 78.4867
TARGET_LAT, TARGET_LON = 17.3870, 78.4895

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def send_event(event: dict):
    line = json.dumps(event, ensure_ascii=False)
    with open(LOG_DIR / f"{MISSION_ID}.jsonl", "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)

def interpolate_route(start, end, steps=12):
    lat1, lon1 = start
    lat2, lon2 = end
    for i in range(steps + 1):
        t = i / steps
        yield (lat1 + t * (lat2 - lat1), lon1 + t * (lon2 - lon1))

def main():
    print(f"[CARRIER] Mission: {MISSION_ID}")
    print("[CARRIER] Following safe corridor simulation… Ctrl+C to stop.")

    # 1) Takeoff status
    send_event({"missionId": MISSION_ID, "type": "status", "state": "TAKEOFF", "timestamp": now_iso(), "source": "carrier"})

    # 2) En-route positions
    for lat, lon in interpolate_route((START_LAT, START_LON), (TARGET_LAT, TARGET_LON), steps=14):
        send_event({
            "missionId": MISSION_ID,
            "type": "telemetry",
            "timestamp": now_iso(),
            "source": "carrier",
            "position": {"lat": round(lat, 6), "lon": round(lon, 6)},
            "battery": round(random.uniform(62, 97), 1),
            "speed_mps": round(random.uniform(6.0, 10.0), 1),
        })
        time.sleep(0.9)

    # 3) Payload drop
    send_event({
        "missionId": MISSION_ID,
        "type": "payload",
        "action": "DROP",
        "timestamp": now_iso(),
        "source": "carrier",
        "position": {"lat": TARGET_LAT, "lon": TARGET_LON},
        "photoUrl": None,  # later: Firebase Storage link
        "result": "SUCCESS",
    })

    # 4) Return-to-launch
    send_event({"missionId": MISSION_ID, "type": "status", "state": "RTL", "timestamp": now_iso(), "source": "carrier"})
    print("[CARRIER] Completed simulation.")

if __name__ == "__main__":
    main()
