#include <cassert>
#include "defs.h"
#include "ref.h"
#include "array.h"
#include "library.h"
#include "expr.h"

namespace _uc {

  #include "equality.cpp"

  void _UC_CONCAT(_UC_TYPEDEF(bar), _test)(_UC_TYPE(bar));
  void _UC_CONCAT(_UC_TYPEDEF(foo), _test)(_UC_TYPE(foo));

}

int main() {
  return 0;
}
