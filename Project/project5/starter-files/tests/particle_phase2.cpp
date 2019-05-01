#include <cassert>
#include "defs.h"
#include "ref.h"
#include "array.h"
#include "library.h"
#include "expr.h"

namespace _uc {

  #include "particle.cpp"

  void test() {
    _UC_FUNCTION(apply_force)(_UC_TYPE(particle){},
                              _UC_TYPE(particle){});
    _UC_PRIMITIVE(float) var1 = _UC_FUNCTION(box_size)();
    _UC_PRIMITIVE(float) var2 = _UC_FUNCTION(cutoff_radius)();
    _UC_PRIMITIVE(float) var3 = _UC_FUNCTION(density)();
    _UC_ARRAY(_UC_PRIMITIVE(float)) var4 = _UC_FUNCTION(initial_x_positions)();
    _UC_ARRAY(_UC_PRIMITIVE(float)) var5 = _UC_FUNCTION(initial_x_velocities)();
    _UC_ARRAY(_UC_PRIMITIVE(float)) var6 = _UC_FUNCTION(initial_y_positions)();
    _UC_ARRAY(_UC_PRIMITIVE(float)) var7 = _UC_FUNCTION(initial_y_velocities)();
    _UC_FUNCTION(main)(_UC_ARRAY(_UC_PRIMITIVE(string)){});
    _UC_ARRAY(_UC_TYPE(particle)) var9 = _UC_FUNCTION(make_particles)(_UC_PRIMITIVE(int){});
    _UC_PRIMITIVE(float) var10 = _UC_FUNCTION(mass)();
    _UC_PRIMITIVE(float) var11 = _UC_FUNCTION(max)(_UC_PRIMITIVE(float){},
                                                   _UC_PRIMITIVE(float){});
    _UC_PRIMITIVE(float) var12 = _UC_FUNCTION(min_radius_squared)();
    _UC_FUNCTION(move_particle)(_UC_TYPE(particle){});
    _UC_PRIMITIVE(int) var14 = _UC_FUNCTION(num_particles)();
    _UC_PRIMITIVE(int) var15 = _UC_FUNCTION(num_steps)();
    _UC_FUNCTION(print_particle_positions)(_UC_ARRAY(_UC_TYPE(particle)){});
    _UC_FUNCTION(simulate)(_UC_PRIMITIVE(int){});
    _UC_PRIMITIVE(float) var18 = _UC_FUNCTION(time_interval)();
  }

}

int main() {
  _uc::test();
  return 0;
}
