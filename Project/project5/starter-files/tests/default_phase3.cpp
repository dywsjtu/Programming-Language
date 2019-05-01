#include <cassert>
#include "defs.h"
#include "ref.h"
#include "array.h"
#include "library.h"
#include "expr.h"

namespace _uc {

  #include "default.cpp"

  void test_default() {
    _UC_TYPE(bar) var0 = _uc_make_object<_UC_TYPE(bar)>();
    _UC_TYPE(bar) var0b = _uc_make_object<_UC_TYPE(bar)>();
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    assert(var0->_UC_VAR(f) == _UC_TYPE(foo){});
    assert(var0->_UC_VAR(x) == _UC_PRIMITIVE(int){});
    assert(var0->_UC_VAR(a) == _UC_ARRAY(_UC_PRIMITIVE(string)){});
    _UC_TYPE(baz) var1 = _uc_make_object<_UC_TYPE(baz)>();
    _UC_TYPE(baz) var1b = _uc_make_object<_UC_TYPE(baz)>();
    assert(var1 == var1b);
    assert(!(var1 != var1b));
    _UC_TYPE(foo) var2 = _uc_make_object<_UC_TYPE(foo)>();
    _UC_TYPE(foo) var2b = _uc_make_object<_UC_TYPE(foo)>();
    assert(var2 == var2b);
    assert(!(var2 != var2b));
    assert(var2->_UC_VAR(x) == _UC_PRIMITIVE(int){});
  }

  void test_non_default_with_defaults() {
    _UC_TYPE(bar) var0 = _uc_make_object<_UC_TYPE(bar)>(_UC_TYPE(foo){},
                                                        _UC_PRIMITIVE(int){},
                                                        _UC_ARRAY(_UC_PRIMITIVE(string)){});
    assert(var0->_UC_VAR(f) == _UC_TYPE(foo){});
    assert(var0->_UC_VAR(x) == _UC_PRIMITIVE(int){});
    assert(var0->_UC_VAR(a) == _UC_ARRAY(_UC_PRIMITIVE(string)){});
    _UC_TYPE(baz) var1 = _uc_make_object<_UC_TYPE(baz)>();
    _UC_TYPE(foo) var2 = _uc_make_object<_UC_TYPE(foo)>(_UC_PRIMITIVE(int){});
    assert(var2->_UC_VAR(x) == _UC_PRIMITIVE(int){});
  }

  void test_non_default_with_non_defaults() {
    _UC_TYPE(foo) arg0_0 = _uc_make_object<_UC_TYPE(foo)>();
    _UC_TYPE(foo) arg0_0c = _uc_make_object<_UC_TYPE(foo)>();
    _UC_PRIMITIVE(int) arg0_1 = 1;
    _UC_PRIMITIVE(int) arg0_1c = 2;
    _UC_ARRAY(_UC_PRIMITIVE(string)) arg0_2 = _uc_make_array<_UC_PRIMITIVE(string)>();
    _UC_ARRAY(_UC_PRIMITIVE(string)) arg0_2c = _uc_make_array<_UC_PRIMITIVE(string)>();
    _UC_TYPE(bar) var0 = _uc_make_object<_UC_TYPE(bar)>(arg0_0,
                                                        arg0_1,
                                                        arg0_2);
    _UC_TYPE(bar) var0b = _uc_make_object<_UC_TYPE(bar)>(arg0_0,
                                                         arg0_1,
                                                         arg0_2);
    _UC_TYPE(bar) var0c = _uc_make_object<_UC_TYPE(bar)>(arg0_0c,
                                                         arg0_1c,
                                                         arg0_2c);
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    assert(var0 != var0c);
    assert(!(var0 == var0c));
    assert(var0->_UC_VAR(f) == arg0_0);
    assert(var0->_UC_VAR(x) == arg0_1);
    assert(var0->_UC_VAR(a) == arg0_2);
    _UC_TYPE(baz) var1 = _uc_make_object<_UC_TYPE(baz)>();
    _UC_TYPE(baz) var1b = _uc_make_object<_UC_TYPE(baz)>();
    _UC_TYPE(baz) var1c = _uc_make_object<_UC_TYPE(baz)>();
    assert(var1 == var1b);
    assert(!(var1 != var1b));
    _UC_PRIMITIVE(int) arg2_0 = 3;
    _UC_PRIMITIVE(int) arg2_0c = 4;
    _UC_TYPE(foo) var2 = _uc_make_object<_UC_TYPE(foo)>(arg2_0);
    _UC_TYPE(foo) var2b = _uc_make_object<_UC_TYPE(foo)>(arg2_0);
    _UC_TYPE(foo) var2c = _uc_make_object<_UC_TYPE(foo)>(arg2_0c);
    assert(var2 == var2b);
    assert(!(var2 != var2b));
    assert(var2 != var2c);
    assert(!(var2 == var2c));
    assert(var2->_UC_VAR(x) == arg2_0);
  }

}

int main() {
  _uc::test_default();
  _uc::test_non_default_with_defaults();
  _uc::test_non_default_with_non_defaults();
  return 0;
}
