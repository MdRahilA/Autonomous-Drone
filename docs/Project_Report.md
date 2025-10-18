# Dual-Drone NIDAR Project Report

## Abstract
The Dual-Drone NIDAR system enables coordinated drone missions for rapid disaster response.  
The system consists of a Scout Drone for mapping and detection, a Carrier Drone for payload delivery, a mobile SOS app, and a Firebase-based backend that manages missions in real-time.

---

## Problem Statement
In disaster-affected regions, communication breakdown and blocked roads delay emergency relief.  
Our goal is to deploy a **dual-drone AI system** that can autonomously detect survivors and deliver essential items directly to the site.

---

## Objectives
- Automate **SOS → Mission → Drone Dispatch** pipeline.  
- Enable **AI-assisted detection** of victims or hotspots.  
- Establish reliable **cloud-to-drone communication**.  
- Build a **user-friendly mobile & web interface** for monitoring.

---

## System Components
1. **Scout Drone** – AI-powered scanning for survivors or obstacles.  
2. **Carrier Drone** – Payload delivery and autonomous return.  
3. **Cloud Backend** – Manages missions via Firebase Firestore.  
4. **Mobile App** – Sends SOS alerts with GPS location.  
5. **Web Dashboard** – Displays real-time telemetry and logs.

---

## Tools & Technologies
| Layer | Tech Stack |
|-------|-------------|
| Drone | Python, MAVLink, OpenCV, YOLOv8 |
| Cloud | Firebase, Node.js, Firestore |
| Mobile | Flutter, Dart, Google Maps SDK |
| Dashboard | React / HTML / JS |
| AI | Object Detection (Planned) |

---

## Workflow
1. User sends **SOS alert** via mobile app.  
2. Cloud backend triggers **mission initialization**.  
3. Scout drone scans area → sends detection logs.  
4. Carrier drone is dispatched → payload delivered.  
5. Admin monitors mission from dashboard.

---

## Results (Prototype Stage)
✅ Cloud-triggered drone scripts simulated successfully.  
✅ Web dashboard UI integrated with demo mission logs.  
✅ SOS mobile app functional (frontend completed).

---

## Future Scope
- Full Firebase integration with real drones.  
- Edge-AI for thermal detection.  
- 3D mapping and autonomous navigation.

---

## Contributors
**Mohammed Adnan** – Project Lead, AI & Cloud  
**AI Decoded** – Development & System Design
