import java.util.Scanner;

public class 막대기_박주원 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] arr = new int[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		
		int cnt = 1;
		int max = arr[N - 1];
		
		for(int i = N - 2; i >= 0; i--) {
			if(max < arr[i]) {
				max = arr[i];
				cnt++;
			}
		}
		System.out.println(cnt);
	}

}
