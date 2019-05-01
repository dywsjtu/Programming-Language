#include <iostream>
#include <vector>

using std::cout;
using std::endl;

namespace _Q1c {
  template<typename T>
  struct A {
    using type = int;
    static const bool value = true;
  };

  template<typename T>
  struct A<std::vector<T>> {
    static const bool value = false;
  };

  template<typename T>
  bool func(T a, typename A<T>::type b = 0) {
    return true;
  }
}

void Q1c() {
  using namespace _Q1c;
  //cout << A::value << endl;
  cout << A<int>::value << endl;
  cout << A<std::vector<int>>::value << endl;
  cout << func(3) << endl;
  //func(std::vector<int>()) << endl;
}

namespace _Q3c {
  struct A {
    int x;
    virtual void foo() { cout << "A::foo()" << endl; }
    void baz() { cout << "A::baz()" << endl; }
  };

  struct B : A {
    virtual void bar() { cout << "B::bar()" << endl; }
    virtual void foo() { cout << "B::foo()" << endl; }
    void baz() { cout << "B::baz()" << endl; }
  };

  struct C : B {
    int z;
    virtual void baz() { cout << "C::baz()" << endl; }
  };
}

void Q3c() {
  using namespace _Q3c;
  C c;
  A* ptr = &c;

  c.baz();                 // prints: ____________________________

  ptr->baz();              // prints: ____________________________

  c.foo();                 // prints: ____________________________

  ptr->foo();              // prints: ____________________________
}

template<typename T>
class Counter {
  T count = {}; // value initialize the count
public:
  T get() const {
    return count;
  }
  void add(const T &x) {
    count += x;
  }
  template<typename U>
  void add(const Counter<U> &other) { 
    add(other.get());
  }
};

void Q4b() {
  Counter<int> c1;
  Counter<double> c2;
  c1.add(3);
  std::cout << c1.get() << std::endl;
  c2.add(-4);
  c2.add(-2.2);
  std::cout << c2.get() << std::endl;
  c1.add(c2);
  std::cout << c1.get() << std::endl;
  c2.add(c1);
  std::cout << c2.get() << std::endl;
}

int main() {
  cout << std::boolalpha;
  Q1c();
  Q3c();
  Q4b();
}
