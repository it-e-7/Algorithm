import java.io.*;
import java.util.*;

public class 바이러스_서명현 {

    static int n;
    static int[][] computer;
    static boolean[] visited;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        computer = new int[n + 1][n + 1];
        visited = new boolean[n + 1];
        count = 0;
        StringTokenizer st;

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            computer[x][y] = 1;
            computer[y][x] = 1;
        }
        bfs();
        System.out.println(count);
    }

    private static void bfs() {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        visited[1] = true;
        while (!queue.isEmpty()) {
            Integer p = queue.poll();
            for (int i = 1; i < n + 1; i++) {
                if (computer[p][i] == 1 && !visited[i]) {
                    queue.offer(i);
                    visited[i] = true;
                    count++;
                }
            }
        }
    }
}
