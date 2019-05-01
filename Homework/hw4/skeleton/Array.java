/**
 *  A class representing a multidimensional array of objects.
 */
public class Array {
  /**
   *  Construct a multidimensional array with the given dimensions.
   *
   *  @params dims  the size of each dimension; the rank of this Array
   *                will be dims.length, which must be at least 1
   */
  public Array(int... dims) {
    assert dims.length >= 1 : "rank must be at least 1";
    this.dims = dims.clone(); // make copy of dims
    int size = 1;
    for (int i = 0; i < dims.length; i++) {
      size *= dims[i];
    }
    data = new String[size];
  }

  /**
   *  Returns the element in this Array at the given location.
   *
   *  @param indices  the index of the element in each dimension; no
   *                  bounds checking is performed
   */
  public String get(int... indices) {
    return data[indexOf(indices)];
  }

  /**
   *  Sets the element in this Array at the given location to the
   *  given value.
   *
   *  @param value    the new value of the element
   *  @param indices  the index of the element in each dimension; no
   *                  bounds checking is performed
   */ 
  public void set(String value, int... indices) {
    data[indexOf(indices)] = value;
  }

  /**
   *  Returns the rank (number of dimensions) of this Array.
   */
  public int rank() {
    return dims.length;
  }

  /**
   *  Returns the number of elements contained in this Array.
   */
  public int size() {
    return data.length;
  }

  /**
   *  Returns an array containing the size of each dimension of this
   *  Array.
   */
  public int[] shape() {
    return dims.clone();
  }

  // This method translates a multidimensional index into a linear
  // offset into the data array. Use it in get() and set().
  private int indexOf(int... indices) {
    assert indices.length == rank() :
      "Number of indices does not match rank";
    int index = 0;
    for (int i = 0; i < rank(); i++) {
      index = index * dims[i] + indices[i];
    }
    return index;
  }

  private int[] dims; // the dimensions of this Array
  private String[] data; // the elements of this Array
}
