void main(string[] args)() {
  println(args);
}

int get_value()(int x) {
  return x;
}

void main2(string[] args)() {
  args[0] = null;
}

void main3(string[] args)() {
  args >> null;
}

void main4(string[] args)() {
  println(new foo().s);
}

struct foo(string s);
