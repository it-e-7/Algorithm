import java.io.*;
import java.util.*;

public class 촌수계산_서명현 {

    static int n;
    static int start;
    static int end;
    static int[][] cousinMap;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken());
        end = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(br.readLine());

        cousinMap = new int[n + 1][n + 1];
        visited = new int[n + 1];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            cousinMap[x][y] = 1;
            cousinMap[y][x] = 1;
        }
        bfs();
        System.out.println(visited[end] - 1);
    }

    private static void bfs() {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = 1;
        while (!queue.isEmpty()) {
            int p = queue.poll();
            for (int i = 1; i < n + 1; i++) {
                if (cousinMap[p][i] == 1 && visited[i] == 0) {
                    queue.offer(i);
                    visited[i] = visited[p] + 1;
                }
            }
        }
    }
}
