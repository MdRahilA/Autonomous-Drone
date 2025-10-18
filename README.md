# Dual-Drone  (Scout + Carrier)

Coordinated dual-drone system that integrates with the **NIDAR** app to respond to SOS events.  
- **Scout**: fast VTOL/quad for rapid area scan, visual/thermal search, live map.
- **Carrier**: payload drone for delivery (first aid, radio, power), follows safe route from Scout.

> ⚠️ Research prototype — not certified for critical operations.

## 🎯 Objectives
- 1-tap SOS from NIDAR app → auto mission creation
- Real-time map from Scout (SLAM/thermal) → safe corridor
- Carrier route planning + geofenced drop zone
- Live telemetry to admin panel; audit & mission logs

## 🧱 High-Level Architecture

