import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
 
        List<int[]> queue = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int num = scanner.nextInt();
            queue.add(new int[]{num, i});
        }
 
        while (queue.size() != 1) {
            if (queue.get(0)[0] > m) {
                int[] w = queue.remove(0);
                queue.add(new int[]{w[0] - m, w[1]});
            } else {
                queue.remove(0);
            }
        }
 
        System.out.println(queue.get(0)[1] + 1);
    }
}