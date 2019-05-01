void main(string[] args)(foo f, bar b, baz z) {
  f = new foo();
  b = new bar();
  z = new baz();
  println("" + f.x);
  println("" + (b.f == null));
  println("" + (b.a == null));
}

struct foo(int x);

struct bar(foo f, int x, string[] a);

struct baz();
