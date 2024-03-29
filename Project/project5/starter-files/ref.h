#pragma once

/**
 * ref.h
 *
 * This file provides the implementation for uC references, as well as
 * operations on them.
 */

#include <memory>
#include "defs.h"

namespace _uc {

  // The class type representing a uC reference. It is built on top of
  // std::shared_ptr, which performs reference counting. The latter is
  // not used directly, since operations such as == are defined
  // differently in uC than they are in C++.
  template<class T>
  struct _uc_reference : std::shared_ptr<T> {
    _uc_reference() {}
    _uc_reference(std::nullptr_t n) : std::shared_ptr<T>(n) {}
    template<class Y>
    explicit _uc_reference(Y *ptr) : std::shared_ptr<T>(ptr) {}
    _uc_reference(const std::shared_ptr<T> &sp) : std::shared_ptr<T>(sp) {}
    _uc_reference(std::shared_ptr<T> &&sp) : std::shared_ptr<T>(sp) {}
  };

  // A function template to construct a uC object and wrap it in a uC
  // reference.
  template<class T, class... Args>
  T _uc_make_object(Args&&... args) {
    return T(std::make_shared<typename T::element_type>(args...));
  }

  // Comparisons between two uC references. Two uC references are
  // equal if they are both null, or if the underlying objects have
  // the same contents.
  template<class T>
  bool operator==(const _uc_reference<T> &p1, const _uc_reference<T> &p2) {
    if (p1 == nullptr) {
      return p2 == nullptr;
    } else if (p2 == nullptr) {
      return false;
    }
    return *p1 == *p2;
  }

  template<class T>
  bool operator!=(const _uc_reference<T> &p1, const _uc_reference<T> &p2) {
    return !(p1 == p2);
  }

  // Comparisons between uC references and null-pointer literals.
  template<class T>
  bool operator==(const _uc_reference<T> &p, std::nullptr_t) {
    return static_cast<const std::shared_ptr<T> &>(p) == nullptr;
  }

  template<class T>
  bool operator==(std::nullptr_t, const _uc_reference<T> &p) {
    return static_cast<const std::shared_ptr<T> &>(p) == nullptr;
  }

  template<class T>
  bool operator!=(const _uc_reference<T> &p, std::nullptr_t) {
    return static_cast<const std::shared_ptr<T> &>(p) != nullptr;
  }

  template<class T>
  bool operator!=(std::nullptr_t, const _uc_reference<T> &p) {
    return static_cast<const std::shared_ptr<T> &>(p) != nullptr;
  }

} // namespace _uc
