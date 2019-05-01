public class ArrayTest {
  /**
   *  Runs some tests on the Array class.
   */
  public static void main(String[] args) {
    // test 1D array
    Array<Integer> array1 = new Array<Integer>(10);
    System.out.println("rank: " + array1.rank());
    System.out.println("size: " + array1.size());
    System.out.println("shape: (" + array1.shape()[0] + ")");
    for (int i = 0; i < 10; i++) {
      array1.set(i, i);
    }
    for (int i = 0; i < 10; i++) {
      System.out.println("array1[" + i + "] = " + array1.get(i));
    }

    // test 2D array
    Array<Double> array2 = new Array<Double>(3, 4);
    System.out.println("rank: " + array2.rank());
    System.out.println("size: " + array2.size());
    System.out.println("shape: (" + array2.shape()[0] + "," +
                       array2.shape()[1] + ")");
    double counter2 = 0.1;
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 4; j++) {
        array2.set(counter2++, i, j);
      }
    }
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 4; j++) {
        System.out.println("array2[" + i + "," + j + "] = " +
                           array2.get(i, j));
      }
    }

    // test 3D array
    Array<String> array3 = new Array<String>(2, 3, 4);
    System.out.println("rank: " + array3.rank());
    System.out.println("size: " + array3.size());
    System.out.println("shape: (" + array3.shape()[0] + "," +
                       array3.shape()[1] + "," +
                       array3.shape()[2] + ")");
    int counter3 = 0;
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 3; j++) {
        for (int k = 0; k < 4; k++) {
          array3.set("i" + counter3++, i, j, k);
        }
      }
    }
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 3; j++) {
        for (int k = 0; k < 4; k++) {
          System.out.println("array3[" + i + "," + j + "," + k +
                             "] = " + array3.get(i, j, k));
        }
      }
    }
  }
}
