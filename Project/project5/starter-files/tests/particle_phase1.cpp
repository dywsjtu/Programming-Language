#include <cassert>
#include "defs.h"
#include "ref.h"
#include "array.h"
#include "library.h"
#include "expr.h"

namespace _uc {

  #include "particle.cpp"

  void _UC_CONCAT(_UC_TYPEDEF(particle), _test)(_UC_TYPE(particle));

}

int main() {
  return 0;
}
