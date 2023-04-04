import java.io.*;
import java.util.*;

public class 두수의합_서명현 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            set.add(Integer.parseInt(st.nextToken()));
        }
        int sum = Integer.parseInt(br.readLine());
        int result = 0;
        for (int s : set) {
            if (set.contains(sum - s)) {
                result++;
            }
        }
        System.out.println(result / 2);
    }
}
