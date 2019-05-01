#pragma once

/**
 * library.h
 *
 * This file provides the implementation for built-in uC types and
 * functions.
 */

#include <iostream>
#include <cstdint>
#include <string>
#include <cmath>
#include "defs.h"

// A macro for defining a numerical conversion function.
#define _UC_NUM_CONV(target, src)                               \
  static _UC_PRIMITIVE(target)                                  \
    _UC_FUNCTION(src ## _to_ ## target)(_UC_PRIMITIVE(src) i) { \
    return static_cast<_UC_PRIMITIVE(target)>(i);               \
  }

// A macro for defining a function to convert a built-in type to a
// string.
#define _UC_STR_CONV(src)                                       \
  static _UC_PRIMITIVE(string)                                  \
    _UC_FUNCTION(src ## _to_string)(_UC_PRIMITIVE(src) i) {     \
    return std::to_string(i);                                   \
  }

// A macro for defining a function to convert from a string to a
// built-in type.
#define _UC_FROM_STR(target, func)                                      \
  static _UC_PRIMITIVE(target)                                          \
    _UC_FUNCTION(string_to_ ## target)(_UC_PRIMITIVE(string) i) {       \
    return func(i);                                                     \
  }

namespace _uc {

  // Type aliases for built-in types.
  using _UC_PRIMITIVE(int) = std::int32_t;
  using _UC_PRIMITIVE(long) = std::int64_t;
  using _UC_PRIMITIVE(float) = double;
  using _UC_PRIMITIVE(boolean) = bool;
  using _UC_PRIMITIVE(string) = std::string;
  using _UC_PRIMITIVE(void) = void;

  // Numerical conversions.
  _UC_NUM_CONV(int, long);
  _UC_NUM_CONV(int, float);
  _UC_NUM_CONV(long, int);
  _UC_NUM_CONV(long, float);
  _UC_NUM_CONV(float, int);
  _UC_NUM_CONV(float, long);

  // Conversions to string.
  _UC_STR_CONV(int);
  _UC_STR_CONV(long);
  _UC_STR_CONV(float);

  // Conversions from string.
  _UC_FROM_STR(int, std::stol);
  _UC_FROM_STR(long, std::stoll);
  _UC_FROM_STR(float, std::stod);

  // Boolean conversions.
  static _UC_PRIMITIVE(string)
    _UC_FUNCTION(boolean_to_string)(_UC_PRIMITIVE(boolean) i) {
    return i ? "true" : "false";
  }

  static _UC_PRIMITIVE(boolean)
    _UC_FUNCTION(string_to_boolean)(_UC_PRIMITIVE(string) i) {
    return i == "false" ? false : true;
  }

  // Built-in length() function. Takes a string and returns its length.
  static _UC_PRIMITIVE(int) _UC_FUNCTION(length)(_UC_PRIMITIVE(string) s) {
    return static_cast<_UC_PRIMITIVE(int)>(s.length());
  }

  // Built-in substr() function. Takes a string, a start, and a length
  // and returns the corresponding substring.
  static _UC_PRIMITIVE(string) _UC_FUNCTION(substr)(_UC_PRIMITIVE(string) s,
                                                    _UC_PRIMITIVE(int) start,
                                                    _UC_PRIMITIVE(int) len) {
    return s.substr(start, len);
  }

  // Built-in ordinal() function. Takes a single-character string and
  // returns the ASCII value of the character.
  static _UC_PRIMITIVE(int) _UC_FUNCTION(ordinal)(_UC_PRIMITIVE(string) s) {
    if (s.length() != 1) {
      return -1;
    }
    return static_cast<_UC_PRIMITIVE(int)>(s[0]);
  }

  // Built-in character() function. Takes an ASCII value and returns a
  // a single-character string corresponding to that value. Returns an
  // empty string if the value is outside the range [1, 127].
  static _UC_PRIMITIVE(string) _UC_FUNCTION(character)(_UC_PRIMITIVE(int) c) {
    if (c < 1 || c > 127) {
      return _UC_PRIMITIVE(string)();
    }
    return _UC_PRIMITIVE(string)() + static_cast<char>(c);
  }

  // Built-in pow() function. Raises a number to the power of another.
  static _UC_PRIMITIVE(float) _UC_FUNCTION(pow)(_UC_PRIMITIVE(float) a,
                                                _UC_PRIMITIVE(float) b) {
    return std::pow(a, b);
  }

  // Built-in sqrt() function. Computes the square root of a number.
  static _UC_PRIMITIVE(float) _UC_FUNCTION(sqrt)(_UC_PRIMITIVE(float) i) {
    return std::sqrt(i);
  }

  // Built-in ceil() function. Rounds a number to the next highest
  // integer value.
  static _UC_PRIMITIVE(float) _UC_FUNCTION(ceil)(_UC_PRIMITIVE(float) i) {
    return std::ceil(i);
  }

  // Built-in floor() function. Rounds a number to the next lowest
  // integer value.
  static _UC_PRIMITIVE(float) _UC_FUNCTION(floor)(_UC_PRIMITIVE(float) i) {
    return std::floor(i);
  }

  // Built-in print() function. Takes a string and prints it to
  // standard out, without a trailing newline.
  static void _UC_FUNCTION(print)(_UC_PRIMITIVE(string) i) {
    std::cout << i;
  }

  // Built-in println() function. Takes a string and prints it to
  // standard out, with a trailing newline.
  static void _UC_FUNCTION(println)(_UC_PRIMITIVE(string) i) {
    std::cout << i << std::endl;
  }

  // Built-in peekchar() function. Returns the next character in
  // standard in. Returns an empty string if the stream is at EOF.
  static _UC_PRIMITIVE(string) _UC_FUNCTION(peekchar)() {
    char c[2] = { static_cast<char>(std::cin.peek()) };
    if (std::cin.eof()) {
      return "";
    } else {
      return _UC_PRIMITIVE(string)(c);
    }
  }

  // Built-in readchar() function. Returns the next character in
  // standard in, removing it from the stream. Returns an empty string
  // if the stream is at EOF.
  static _UC_PRIMITIVE(string) _UC_FUNCTION(readchar)() {
    auto result = _UC_FUNCTION(peekchar)();
    std::cin.get();
    return result;
  }

  // Built-in readline() function. Returns the line in standard in,
  // including the trailine newline if there is one. Returns an empty
  // string if the stream is at EOF.
  static _UC_PRIMITIVE(string) _UC_FUNCTION(readline)() {
    _UC_PRIMITIVE(string) result;
    std::getline(std::cin, result);
    if (std::cin && !std::cin.eof()) {
      result.push_back('\n');
    }
    return result;
  }

} // namespace _uc

#undef _UC_NUM_CONV
#undef _UC_STR_CONV
#undef _UC_FROM_STR
#undef _UC_INIT
