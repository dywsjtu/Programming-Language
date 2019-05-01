void main(string[] args)(int i, float f) {
  i = 3;
  f = 4.0;
  println("" + (i == i));
  println("" + (f != f));
  println("" + (i == f));
  println("" + (i != f));
  println("" + (new foo(3) == new foo(3)));
  println("" + (new foo(3) != new foo(3)));
  println("" + (new foo(3) == new foo(4)));
  println("" + (new foo(3) != new foo(4)));
  println("" + (new foo(3) == null));
  println("" + (new foo(3) != null));
  println("" + (new foo { new foo(3) } == new foo { new foo(3) }));
  println("" + (new foo { new foo(3) } != new foo { new foo(4) }));
  println("" + (new foo { new foo(3) } != new foo { new foo(3),
                                                    new foo(4) }));
  println("" + (new foo { new foo(3) } == null));
  println("" + (new foo { new foo(3) } != null));
}

struct foo(int x);
