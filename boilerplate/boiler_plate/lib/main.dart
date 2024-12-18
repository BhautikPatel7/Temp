import 'package:boiler_plate/containerview.dart';
import 'package:boiler_plate/fortuneWheel.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  MyApp({super.key});
  MySpinController speenContoler = MySpinController();
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: ContainerView(),
      // home: MySpinner(
      //   mySpinController: speenContoler,
      //   onFinished: (p0) {
      //     print("Finished");
      //   },
      //   itemList: [
      //     SpinItem(
      //         label: "First",
      //         color: Colors.black,
      //         labelStyle: TextStyle(color: Colors.green)),
      //     SpinItem(
      //         label: "seco",
      //         color: Colors.black,
      //         labelStyle: TextStyle(color: Colors.green)),
      //     SpinItem(
      //         label: "thir",
      //         color: Colors.black,
      //         labelStyle: TextStyle(color: Colors.green)),
      //     SpinItem(
      //         label: "four",
      //         color: Colors.black,
      //         labelStyle: TextStyle(color: Colors.green)),
      //     SpinItem(
      //         label: "fift",
      //         color: Colors.black,
      //         labelStyle: TextStyle(color: Colors.green)),
      //   ],
      //   wheelSize: 500,
      // ),
    );
  }
}
