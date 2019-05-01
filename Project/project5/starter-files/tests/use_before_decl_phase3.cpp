#include <cassert>
#include "defs.h"
#include "ref.h"
#include "array.h"
#include "library.h"
#include "expr.h"

namespace _uc {

  #include "use_before_decl.cpp"

  void test_default() {
    _UC_TYPE(baz) var0 = _uc_make_object<_UC_TYPE(baz)>();
    _UC_TYPE(baz) var0b = _uc_make_object<_UC_TYPE(baz)>();
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    assert(var0->_UC_VAR(s) == _UC_PRIMITIVE(string){});
    _UC_TYPE(foo) var1 = _uc_make_object<_UC_TYPE(foo)>();
    _UC_TYPE(foo) var1b = _uc_make_object<_UC_TYPE(foo)>();
    assert(var1 == var1b);
    assert(!(var1 != var1b));
    assert(var1->_UC_VAR(b) == _UC_TYPE(baz){});
  }

  void test_non_default_with_defaults() {
    _UC_TYPE(baz) var0 = _uc_make_object<_UC_TYPE(baz)>(_UC_PRIMITIVE(string){});
    assert(var0->_UC_VAR(s) == _UC_PRIMITIVE(string){});
    _UC_TYPE(foo) var1 = _uc_make_object<_UC_TYPE(foo)>(_UC_TYPE(baz){});
    assert(var1->_UC_VAR(b) == _UC_TYPE(baz){});
  }

  void test_non_default_with_non_defaults() {
    _UC_PRIMITIVE(string) arg0_0 = "foo1";
    _UC_PRIMITIVE(string) arg0_0c = "foo2";
    _UC_TYPE(baz) var0 = _uc_make_object<_UC_TYPE(baz)>(arg0_0);
    _UC_TYPE(baz) var0b = _uc_make_object<_UC_TYPE(baz)>(arg0_0);
    _UC_TYPE(baz) var0c = _uc_make_object<_UC_TYPE(baz)>(arg0_0c);
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    assert(var0 != var0c);
    assert(!(var0 == var0c));
    assert(var0->_UC_VAR(s) == arg0_0);
    _UC_TYPE(baz) arg1_0 = _uc_make_object<_UC_TYPE(baz)>();
    _UC_TYPE(baz) arg1_0c = _uc_make_object<_UC_TYPE(baz)>();
    _UC_TYPE(foo) var1 = _uc_make_object<_UC_TYPE(foo)>(arg1_0);
    _UC_TYPE(foo) var1b = _uc_make_object<_UC_TYPE(foo)>(arg1_0);
    _UC_TYPE(foo) var1c = _uc_make_object<_UC_TYPE(foo)>(arg1_0c);
    assert(var1 == var1b);
    assert(!(var1 != var1b));
    assert(var1->_UC_VAR(b) == arg1_0);
  }

}

int main() {
  _uc::test_default();
  _uc::test_non_default_with_defaults();
  _uc::test_non_default_with_non_defaults();
  return 0;
}
