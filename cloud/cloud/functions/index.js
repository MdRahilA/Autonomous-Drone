// cloud/functions/index.js
// Minimal Firestore trigger: on mission create → set ACTIVE + seed plan.

const functions = require("firebase-functions");
const admin = require("firebase-admin");

if (!admin.apps.length) {
  admin.initializeApp();
}
const db = admin.firestore();

exports.onMissionCreate = functions.firestore
  .document("missions/{missionId}")
  .onCreate(async (snap, context) => {
    const missionId = context.params.missionId;
    const missionRef = db.collection("missions").doc(missionId);

    // 1) Mark mission ACTIVE (if not already)
    await missionRef.set(
      {
        status: "ACTIVE",
        updatedAt: admin.firestore.FieldValue.serverTimestamp(),
      },
      { merge: true }
    );

    // 2) Simple initial assignment (placeholder)
    await missionRef.set(
      {
        assigned: {
          scout: "drone-scout-01",
          carrier: "drone-carrier-01",
        },
      },
      { merge: true }
    );

    // 3) Write a log entry
    await missionRef.collection("logs").add({
      timestamp: admin.firestore.FieldValue.serverTimestamp(),
      level: "INFO",
      source: "planner",
      message: "Mission initialized with default Scout/Carrier assignment.",
    });

    return null;
  });
