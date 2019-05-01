public class UtilTest {
  /**
   *  Runs some tests on Util.indexOfMax1D().
   */
  public static void main(String[] args) {
    // test Integer array
    Array<Integer> array1 = new Array<Integer>(10);
    for (int i = 0; i < 10; i++) {
      array1.set(i, i);
    }
    assert Util.indexOfMax1D(array1) == 9 : "failed on array1";

    // test Double array
    Array<Double> array2 = new Array<Double>(3);
    array2.set(1.2, 0);
    array2.set(3.1, 1);
    array2.set(2.3, 2);
    assert Util.indexOfMax1D(array2) == 1 : "failed on array2";

    // test String array
    Array<String> array3 = new Array<String>(2);
    array3.set("world", 0);
    array3.set("hello", 1);
    assert Util.indexOfMax1D(array3) == 0 : "failed on array3";
  }
}
