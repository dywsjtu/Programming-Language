#pragma once

/**
 * array.h
 *
 * This file provides the implementation for uC arrays, as well as
 * operations on them.
 */

#include <iostream>
#include "library.h"
#include "ref.h"

namespace _uc {

  // Basic vector implementation that does not specialize on bool.
  template<class T>
  class vector {
    static const std::size_t INITIAL_CAPACITY = 10;
    std::size_t num_elements;
    std::size_t capacity;
    T *elements;
    void renum_elements() {
      capacity = 2 * capacity + 1;
      T *tmp = new T[capacity];
      for (std::size_t i = 0; i < num_elements; i++) {
        tmp[i] = elements[i];
      }
      delete[] elements;
      elements = tmp;
    }
  public:
    vector() :
      num_elements(0), capacity(INITIAL_CAPACITY),
      elements(new T[INITIAL_CAPACITY]) {}
    vector(const vector &rhs) :
      num_elements(rhs.num_elements), capacity(rhs.capacity),
      elements(new T[rhs.capacity]) {
      for (std::size_t i = 0; i < num_elements; i++) {
        elements[i] = rhs.elements[i];
      }
    }
    vector &operator=(const vector &rhs) {
      if (rhs == *this)
        return *this;
      delete[] elements;
      num_elements = rhs.num_elements;
      capacity = rhs.capacity;
      elements = new T[capacity];
      for (std::size_t i = 0; i < num_elements; i++) {
        elements[i] = rhs.elements[i];
      }
      return *this;
    }
    ~vector() {
      delete[] elements;
    }
    void push_back(const T &item) {
      if (num_elements == capacity)
        renum_elements();
      elements[num_elements++] = item;
    }
    T &back() {
      return elements[num_elements - 1];
    }
    const T &back() const {
      return elements[num_elements - 1];
    }
    void pop_back() {
      num_elements--;
    }
    template<class I>
    T &operator[](I i) {
      return elements[i];
    }
    template<class I>
    const T &operator[](I i) const {
      return elements[i];
    }
    std::size_t size() const {
      return num_elements;
    }
    bool operator==(const vector &rhs) const {
      if (num_elements != rhs.num_elements)
        return false;
      for (size_t i = 0; i < num_elements; i++) {
        if (elements[i] != rhs.elements[i])
          return false;
      }
      return true;
    }
    bool operator!=(const vector &rhs) const {
      if (num_elements != rhs.num_elements)
        return true;
      for (size_t i = 0; i < num_elements; i++) {
        if (elements[i] != rhs.elements[i])
          return true;
      }
      return false;
    }
  };

  // Type alias template for a uC array.
  template<class T>
  using _UC_PREFIX(array) = _uc_reference<vector<T>>;

  // Compute the length of a uC array.
  template<class A>
  _UC_PRIMITIVE(int) _uc_array_length(A array) {
    return static_cast<_UC_PRIMITIVE(int)>(array->size());
  }

  // Push an element onto a uC array, returning the array as the
  // result.
  template<class A, class T>
  A _uc_array_push(A array, T item) {
    array->push_back(item);
    return array;
  }

  // Pop an element from a uC array, assigning the value to a variable
  // and returning the array as the result. Performs bounds checking.
  template<class A, class T>
  A _uc_array_pop(A array, T &target) {
    if (_uc_array_length(array) == 0) {
      std::cerr << "Error: cannot pop from array of length 0"
                << std::endl;
      std::abort();
    }
    target = array->back();
    array->pop_back();
    return array;
  }

  // Pop an element from a uC array, discarding the value and
  // returning the array as the result. Performs bounds checking.
  template<class A>
  A _uc_array_pop(A array, std::nullptr_t) {
    if (_uc_array_length(array) == 0) {
      std::cerr << "Error: cannot pop from array of length 0"
                << std::endl;
      std::abort();
    }
    array->pop_back();
    return array;
  }

  // Construct a uC array containing the given elements. This template
  // should be explicitly instantiated when it is called, e.g.
  // _uc_make_array<_UC_PRIMITIVE(int)>(...).
  template<class T, class... Args>
  _UC_ARRAY(T) _uc_make_array(Args... args) {
    T arr[] = { static_cast<T>(args)... };
    auto vec = _uc_make_object<_uc_reference<vector<T>>>();
    for (std::size_t i = 0; i < sizeof...(args); i++) {
      _uc_array_push(vec, arr[i]);
    }
    return vec;
  }

  // Indexes into a uC array, returning the associated element.
  // Performs bounds checking.
  template<class A, class U>
  auto _uc_array_index(A array, U i) -> decltype((*array)[i]) & {
    if (i < 0 || i >= _uc_array_length(array)) {
      std::cerr << "Error: array index out of bounds: 0 <= "
                << std::to_string(i) << " < "
                << std::to_string(_uc_array_length(array))
                << std::endl;
      std::abort();
    }
    return (*array)[i];
  }

} // namespace _uc
