import java.util.Arrays;
import java.util.Scanner;

public class 콘테스트_박주원 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int[] w = new int[10];
		int[] k = new int[10];
		
		for(int i = 0; i < 10; i++) {
			w[i] = sc.nextInt();
		}
		
		for(int j = 0; j < 10; j++) {
			k[j] = sc.nextInt();
		}
		
		Arrays.sort(w);
		
		int wSum = 0;
		for(int i = 9; i >= 7; i--) {
			wSum += w[i];
		}
		
		Arrays.sort(k);
		
		int kSum = 0;
		for(int j = 9; j >= 7; j--) {
			kSum += k[j];
		}
		
		System.out.println(wSum + " " + kSum);
	}

}