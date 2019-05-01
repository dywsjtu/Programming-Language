#include <cassert>
#include "defs.h"
#include "ref.h"
#include "array.h"
#include "library.h"
#include "expr.h"

namespace _uc {

  #include "length_field.cpp"

  void test_default() {
    _UC_TYPE(foo) var0 = _uc_make_object<_UC_TYPE(foo)>();
    _UC_TYPE(foo) var0b = _uc_make_object<_UC_TYPE(foo)>();
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    assert(var0->_UC_VAR(x) == _UC_PRIMITIVE(int){});
    assert(var0->_UC_VAR(length) == _UC_PRIMITIVE(string){});
  }

  void test_non_default_with_defaults() {
    _UC_TYPE(foo) var0 = _uc_make_object<_UC_TYPE(foo)>(_UC_PRIMITIVE(int){},
                                                        _UC_PRIMITIVE(string){});
    assert(var0->_UC_VAR(x) == _UC_PRIMITIVE(int){});
    assert(var0->_UC_VAR(length) == _UC_PRIMITIVE(string){});
  }

  void test_non_default_with_non_defaults() {
    _UC_PRIMITIVE(int) arg0_0 = 1;
    _UC_PRIMITIVE(int) arg0_0c = 2;
    _UC_PRIMITIVE(string) arg0_1 = "foo3";
    _UC_PRIMITIVE(string) arg0_1c = "foo4";
    _UC_TYPE(foo) var0 = _uc_make_object<_UC_TYPE(foo)>(arg0_0,
                                                        arg0_1);
    _UC_TYPE(foo) var0b = _uc_make_object<_UC_TYPE(foo)>(arg0_0,
                                                         arg0_1);
    _UC_TYPE(foo) var0c = _uc_make_object<_UC_TYPE(foo)>(arg0_0c,
                                                         arg0_1c);
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    assert(var0 != var0c);
    assert(!(var0 == var0c));
    assert(var0->_UC_VAR(x) == arg0_0);
    assert(var0->_UC_VAR(length) == arg0_1);
  }

}

int main() {
  _uc::test_default();
  _uc::test_non_default_with_defaults();
  _uc::test_non_default_with_non_defaults();
  return 0;
}
