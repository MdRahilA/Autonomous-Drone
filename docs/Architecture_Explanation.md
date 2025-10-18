# Architecture Explanation – Dual-Drone NIDAR

## 1. Overview
The NIDAR platform combines two drones and three software layers (mobile, cloud, web) to coordinate rapid-response missions.

## 2. Flow
1. The **user** raises an SOS via the mobile app.
2. The **cloud function** creates a mission document and assigns drones.
3. The **scout drone** scans the area and uploads detections.
4. The **carrier drone** delivers the payload safely.
5. The **admin dashboard** visualizes mission status and telemetry.

## 3. Communication
- Cloud → Drones: Firestore or MQTT updates.
- Drones → Cloud: Telemetry logs (JSON).
- Cloud → Dashboard: Real-time mission stream.
- Dashboard → Admin: Mission visualization.
