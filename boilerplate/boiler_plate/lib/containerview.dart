import 'package:flutter/material.dart';
import 'dart:math' as math;

class ContainerView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Container View"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: LayoutBuilder(
          builder: (context, constraints) {
            final isDesktop = constraints.maxWidth >= 768;
            final boxSize = isDesktop ? 150.0 : 120.0;

            return Stack(
              children: List.generate(6, (index) {
                final angle = (index / 6) * 360;
                final distance = isDesktop ? 100.0 : 80.0;
                final x = distance * math.cos(angle * math.pi / 180);
                final y = distance * math.sin(angle * math.pi / 180);

                return Positioned(
                  left: constraints.maxWidth / 2 + x - boxSize / 2,
                  top: constraints.maxHeight / 2 + y - boxSize / 2,
                  child: Transform.rotate(
                    angle: angle * math.pi / 180,
                    child: Container(
                      width: boxSize,
                      height: boxSize,
                      padding: EdgeInsets.all(16.0),
                      decoration: BoxDecoration(
                        color: Colors.blueAccent,
                        borderRadius: BorderRadius.circular(16.0),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.3),
                            blurRadius: 8,
                            offset: Offset(4, 4),
                          ),
                        ],
                      ),
                      child: Center(
                        child: Text(
                          'Box ${index + 1}',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ),
                  ),
                );
              }),
            );
          },
        ),
      ),
    );
  }
}
