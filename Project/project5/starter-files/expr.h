#pragma once

/**
 * expr.h
 *
 * This file includes function template overloads for polymorphic
 * operations, specifically accessing the length field of an object
 * and adding two values together.
 */

#include "array.h"

namespace _uc {

  // Basic template for accessing the length field of a non-array
  // object.
  template<class T>
  auto _uc_length_field(T ref) -> decltype(ref->_UC_VAR(length)) & {
    return ref->_UC_VAR(length);
  }

  // add your overloads here

  // define your overloads for _uc_add() here

} // namespace _uc
