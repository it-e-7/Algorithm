import java.io.*;
import java.util.*;

public class 수들의합2_양석진 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int size = Integer.parseInt(st.nextToken());
        int compareN = Integer.parseInt(st.nextToken());

        int[] arr = new int[size];
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int x = 0; x < size; x++) {
            arr[x] = Integer.parseInt(st2.nextToken());
        }

        int start = 0;
        int end = 0;
        int count = 0;
        int sum = 0;

        while (true) {
            if (sum >= compareN) {
                sum -= arr[start++];
            } else if (end == size) {
                break;
            } else {
                sum += arr[end++];
            }
            if (sum == compareN) {
                count++;
            }
        }
        System.out.println(count);
    }
}
