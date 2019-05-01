#include <cassert>
#include "defs.h"
#include "ref.h"
#include "array.h"
#include "library.h"
#include "expr.h"

namespace _uc {

  #include "equality.cpp"

  void test_default() {
    _UC_TYPE(bar) var0 = _uc_make_object<_UC_TYPE(bar)>();
    _UC_TYPE(bar) var0b = _uc_make_object<_UC_TYPE(bar)>();
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    _UC_TYPE(foo) var1 = _uc_make_object<_UC_TYPE(foo)>();
    _UC_TYPE(foo) var1b = _uc_make_object<_UC_TYPE(foo)>();
    assert(var1 == var1b);
    assert(!(var1 != var1b));
    assert(var1->_UC_VAR(x) == _UC_PRIMITIVE(int){});
  }

  void test_non_default_with_defaults() {
    _UC_TYPE(bar) var0 = _uc_make_object<_UC_TYPE(bar)>();
    _UC_TYPE(foo) var1 = _uc_make_object<_UC_TYPE(foo)>(_UC_PRIMITIVE(int){});
    assert(var1->_UC_VAR(x) == _UC_PRIMITIVE(int){});
  }

  void test_non_default_with_non_defaults() {
    _UC_TYPE(bar) var0 = _uc_make_object<_UC_TYPE(bar)>();
    _UC_TYPE(bar) var0b = _uc_make_object<_UC_TYPE(bar)>();
    _UC_TYPE(bar) var0c = _uc_make_object<_UC_TYPE(bar)>();
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    _UC_PRIMITIVE(int) arg1_0 = 1;
    _UC_PRIMITIVE(int) arg1_0c = 2;
    _UC_TYPE(foo) var1 = _uc_make_object<_UC_TYPE(foo)>(arg1_0);
    _UC_TYPE(foo) var1b = _uc_make_object<_UC_TYPE(foo)>(arg1_0);
    _UC_TYPE(foo) var1c = _uc_make_object<_UC_TYPE(foo)>(arg1_0c);
    assert(var1 == var1b);
    assert(!(var1 != var1b));
    assert(var1 != var1c);
    assert(!(var1 == var1c));
    assert(var1->_UC_VAR(x) == arg1_0);
  }

}

int main() {
  _uc::test_default();
  _uc::test_non_default_with_defaults();
  _uc::test_non_default_with_non_defaults();
  return 0;
}
