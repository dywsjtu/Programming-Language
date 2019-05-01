def gen_comparison_op(typename, op):
    """Generates a C++ overloaded comparison operator for the given
    type and operator. typename must be a string representing the uC
    name of the type. op must be one of the strings '<', '<=', '==',
    '!=', '>', '>='.
    """
    skeleton = 'bool operator{0}(_UC_TYPE({1}) lhs, ' \
               '_UC_TYPE({1}) rhs) {{\n' \
               '  return _UC_FUNCTION({1}_compare)(lhs, rhs) {0} 0;\n' \
               '}}'
    print(skeleton.format(op, typename))

if __name__ == '__main__':
    gen_comparison_op('foo', '<=')
