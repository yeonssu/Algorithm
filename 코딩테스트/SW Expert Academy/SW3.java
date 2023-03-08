import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class SW3 {
    static int[] valueArray;
    static int[] newValue;

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int t = 0; t < T; t++) {
            String N = scanner.next();
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            int positionalNumber = N.length();

            valueArray = new int[positionalNumber];
            newValue = new int[positionalNumber];

            for (int i = 0; i < positionalNumber; i++) {
                valueArray[i] = N.charAt(i) - '0';
            }
            makeOverlabPermutation(2,valueArray,0);

        }
    }
    private static void makeOverlabPermutation(int r, int[] temp, int current) {
        if (r == current) {
            System.out.println(Arrays.toString(temp));
        } else {
            for (int i = 0; i < temp.length; i++) {
                temp[current] = temp[i];
                makeOverlabPermutation(r, temp, current + 1);
            }
        }
    }

}
