void main() {
  List<int> a = [7, 8, 9, 11, 12];
  int minnum = a[0];
  for (var i = 1; i < a.length; i++) {
    if (minnum > a[i]) {
      minnum = a[i];
    }
  }
  if (minnum > 1) {
    print("Answter is 1");
    minnum = 1;
  }
  if (minnum <= 0) {
    minnum = 1;
  }
  int temp = minnum;
  int forcounter = 0;

  void runforloop() {
    for (var i = 0; i < a.length; i++) {
      if (minnum == a[i]) {
        minnum++;
        continue;
      }
    }
    forcounter++;
  }

  while (forcounter <= minnum - temp) {
    runforloop();
  }
  print(minnum);
}
