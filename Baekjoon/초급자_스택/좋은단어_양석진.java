import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 좋은단어_양석진 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int ans = 0;
        while(n-- > 0) {
            Stack<Character> stack = new Stack<>();
            String str = br.readLine();
            boolean isGood = true;

            int len = str.length();
            for(int i = 0; i < len; i++) {
                char ch = str.charAt(i);
                if(stack.isEmpty()) {
                    stack.push(ch);
                }else {
                    if(stack.peek() == ch) {
                        stack.pop();
                    }else {
                        stack.push(ch);
                    }
                }
            }
            if(stack.isEmpty()) ans += 1;
        }
        System.out.println(ans);
    }
}