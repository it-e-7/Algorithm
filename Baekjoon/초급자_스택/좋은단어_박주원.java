import java.util.Scanner;
import java.util.Stack;

public class 좋은단어_박주원 {

	public static void main(String[] args) {
		
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int cnt = 0;
		
		for(int i = 0; i < N; i++) {
			String str = sc.next();
			Stack<Character> stack = new Stack<>();
			
			for(int j = 0; j < str.length(); j++) {
				char ch = str.charAt(j);
				if(stack.isEmpty() || stack.peek() != ch) {
					stack.push(ch);
				}else {
					stack.pop();
				}
			}
			
			if(stack.isEmpty()) {
				cnt++;
			}
		}
		System.out.println(cnt);
	}

}
