// mobile/app/lib/main.dart
import 'package:flutter/material.dart';

void main() => runApp(const NidarApp());

class NidarApp extends StatelessWidget {
  const NidarApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'NIDAR',
      theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.indigo),
      home: const SosHomePage(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class SosHomePage extends StatelessWidget {
  const SosHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('NIDAR – SOS')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            const Text('Dual-Drone NIDAR', style: TextStyle(fontSize: 22)),
            const SizedBox(height: 16),
            ElevatedButton.icon(
              icon: const Icon(Icons.warning_amber_rounded),
              label: const Text('SEND SOS'),
              onPressed: () async {
                // TODO: integrate Firebase -> create mission doc
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('SOS sent (demo placeholder)')),
                );
              },
              style: ElevatedButton.styleFrom(padding: const EdgeInsets.symmetric(horizontal: 28, vertical: 16)),
            ),
            const SizedBox(height: 24),
            const Text('Status: Idle (demo)', style: TextStyle(color: Colors.grey)),
          ],
        ),
      ),
    );
  }
}
