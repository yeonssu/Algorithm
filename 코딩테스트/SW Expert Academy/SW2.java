import java.util.Arrays;
import java.util.Scanner;

public class SW2 {
    static int x;
    static int y;

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
                valueArray[i] = N.charAt(i)-'0';
            }

            for (int i = 0; i < positionalNumber; i++) {
                if(valueArray[i]>=x||valueArray[i]>y){
                    newValue[i] = valueArray[i];
                }
            }

        }
    }


}
