void main(string[] args)(int i, foo f) {
  new int {};
  new foo {};
}

foo foo()() {
  return new foo();
}

struct foo(float f, foo g);
