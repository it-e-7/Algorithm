import java.io.*;
import java.util.Stack;

public class 단어순서뒤집기_양석진 {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        Stack<String> stack = new Stack<>();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            String w = br.readLine();
            String[] temp = w.split(" ");
            for (int j = 0; j < temp.length; j++) {
                stack.push(temp[j]);
            }
            sb.append("Case #" + (i+1) + ": ");
            for (int j = 0; j < temp.length; j++) {
                sb.append(stack.pop()).append(" ");
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }
}
