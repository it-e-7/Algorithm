import java.util.Scanner;
import java.util.Stack;

public class 쇠막대기_박주원 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String input = sc.next();
		int result = 0;
		Stack<Integer> stack = new Stack();

		for (int i = 0; i < input.length(); i++) {
			if (input.charAt(i) == '(') {
				stack.push(i);
			} else if (stack.pop() == i - 1) {
				result += stack.size();
			} else {
				result += 1;
			}
		}
		System.out.println(result);
	}
}
