#include <cassert>
#include "defs.h"
#include "ref.h"
#include "array.h"
#include "library.h"
#include "expr.h"

namespace _uc {

  #include "particle.cpp"

  void test_default() {
    _UC_TYPE(particle) var0 = _uc_make_object<_UC_TYPE(particle)>();
    _UC_TYPE(particle) var0b = _uc_make_object<_UC_TYPE(particle)>();
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    assert(var0->_UC_VAR(x) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(y) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(x_vel) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(y_vel) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(x_acc) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(y_acc) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(id) == _UC_PRIMITIVE(int){});
  }

  void test_non_default_with_defaults() {
    _UC_TYPE(particle) var0 = _uc_make_object<_UC_TYPE(particle)>(_UC_PRIMITIVE(float){},
                                                                  _UC_PRIMITIVE(float){},
                                                                  _UC_PRIMITIVE(float){},
                                                                  _UC_PRIMITIVE(float){},
                                                                  _UC_PRIMITIVE(float){},
                                                                  _UC_PRIMITIVE(float){},
                                                                  _UC_PRIMITIVE(int){});
    assert(var0->_UC_VAR(x) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(y) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(x_vel) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(y_vel) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(x_acc) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(y_acc) == _UC_PRIMITIVE(float){});
    assert(var0->_UC_VAR(id) == _UC_PRIMITIVE(int){});
  }

  void test_non_default_with_non_defaults() {
    _UC_PRIMITIVE(float) arg0_0 = 1.1;
    _UC_PRIMITIVE(float) arg0_0c = 2.1;
    _UC_PRIMITIVE(float) arg0_1 = 3.1;
    _UC_PRIMITIVE(float) arg0_1c = 4.1;
    _UC_PRIMITIVE(float) arg0_2 = 5.1;
    _UC_PRIMITIVE(float) arg0_2c = 6.1;
    _UC_PRIMITIVE(float) arg0_3 = 7.1;
    _UC_PRIMITIVE(float) arg0_3c = 8.1;
    _UC_PRIMITIVE(float) arg0_4 = 9.1;
    _UC_PRIMITIVE(float) arg0_4c = 10.1;
    _UC_PRIMITIVE(float) arg0_5 = 11.1;
    _UC_PRIMITIVE(float) arg0_5c = 12.1;
    _UC_PRIMITIVE(int) arg0_6 = 13;
    _UC_PRIMITIVE(int) arg0_6c = 14;
    _UC_TYPE(particle) var0 = _uc_make_object<_UC_TYPE(particle)>(arg0_0,
                                                                  arg0_1,
                                                                  arg0_2,
                                                                  arg0_3,
                                                                  arg0_4,
                                                                  arg0_5,
                                                                  arg0_6);
    _UC_TYPE(particle) var0b = _uc_make_object<_UC_TYPE(particle)>(arg0_0,
                                                                   arg0_1,
                                                                   arg0_2,
                                                                   arg0_3,
                                                                   arg0_4,
                                                                   arg0_5,
                                                                   arg0_6);
    _UC_TYPE(particle) var0c = _uc_make_object<_UC_TYPE(particle)>(arg0_0c,
                                                                   arg0_1c,
                                                                   arg0_2c,
                                                                   arg0_3c,
                                                                   arg0_4c,
                                                                   arg0_5c,
                                                                   arg0_6c);
    assert(var0 == var0b);
    assert(!(var0 != var0b));
    assert(var0 != var0c);
    assert(!(var0 == var0c));
    assert(var0->_UC_VAR(x) == arg0_0);
    assert(var0->_UC_VAR(y) == arg0_1);
    assert(var0->_UC_VAR(x_vel) == arg0_2);
    assert(var0->_UC_VAR(y_vel) == arg0_3);
    assert(var0->_UC_VAR(x_acc) == arg0_4);
    assert(var0->_UC_VAR(y_acc) == arg0_5);
    assert(var0->_UC_VAR(id) == arg0_6);
  }

}

int main() {
  _uc::test_default();
  _uc::test_non_default_with_defaults();
  _uc::test_non_default_with_non_defaults();
  return 0;
}
