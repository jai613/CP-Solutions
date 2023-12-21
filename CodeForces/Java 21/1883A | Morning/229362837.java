 
import java.lang.Math;
import java.util.Scanner;
 
public class Main {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for (int i = 0; i < t; i++) {
            String s = input.next();
            int ans = 0;
            for (int x = 0; x < s.length() - 1; x++) {
                char X = s.charAt(x);
                char Y = s.charAt(x + 1);
                int xx = (X == '0') ? 10 : Integer.parseInt(String.valueOf(X));
                int yy = (Y == '0') ? 10 : Integer.parseInt(String.valueOf(Y));
                ans = ans + Math.abs(xx - yy) + 1;
            }
            char first = s.charAt(0);
            int f = (first == '0') ? 10 : Integer.parseInt(String.valueOf(first));
            System.out.println(ans + f);
        }
    }
}
 