#include <cassert>
#include "defs.h"
#include "ref.h"
#include "array.h"
#include "library.h"
#include "expr.h"

namespace _uc {

  #include "use_before_decl.cpp"

  void test() {
    _UC_FUNCTION(bar)(_UC_TYPE(foo){});
    _UC_FUNCTION(main)(_UC_ARRAY(_UC_PRIMITIVE(string)){});
  }

}

int main() {
  _uc::test();
  return 0;
}
