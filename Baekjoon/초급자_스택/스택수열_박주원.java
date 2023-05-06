import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class 스택수열_박주원 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		Stack<Integer> st = new Stack<>();
		ArrayList<String> result = new ArrayList<>();
		
		int n = sc.nextInt();
		int[] a = new int[n + 1];
		int m = 1;
		
		for(int i = 1; i <= n; i++) {
			a[i] = sc.nextInt();
		}
		
		for(int i = 1; i <= n; i++) {
			st.push(i);
			result.add("+");
			while(!st.empty() && st.peek() == a[m]) {
				st.pop();
				result.add("-");
				m++;
			}
		}
		
		if(st.empty()) {
			for(String s : result) {
				System.out.println(s);
			}
		}else {
			System.out.println("NO");
		}
	}

}
