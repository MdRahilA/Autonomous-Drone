# Firestore Structure (Dual-Drone NIDAR)

## Collections

### `missions/{missionId}`
Top-level mission document.
```json
{
  "status": "NEW | ACTIVE | COMPLETE | CANCELLED",
  "createdAt": "<serverTimestamp>",
  "createdBy": "<uid or 'nidar-app'>",
  "sos": {
    "lat": 0.0,
    "lon": 0.0,
    "note": "optional notes"
  },
  "assigned": {
    "scout": "drone-scout-01",
    "carrier": "drone-carrier-01"
  }
}
