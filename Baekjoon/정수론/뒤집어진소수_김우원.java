import java.util.Scanner;

public class 뒤집어진소수_김우원 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        System.out.println(isSosu(N) && isFlipSosu(N) ? "yes" : "no");
    }

    private static boolean isFlipSosu(long n) {
        String[] flipNum = {"0","1","2","e","e","5","9","e","8","6"};
        char[] origin = String.valueOf(n).toCharArray();

        StringBuilder sb = new StringBuilder();
        for (int i = origin.length - 1; i >= 0; i--) {
            sb.append(flipNum[origin[i] - '0']);
        }

        try {
            long flip = Long.parseLong(sb.toString());
            return isSosu(flip);
        } catch (Exception e) {
            return false;
        }
    }

    private static boolean isSosu(long n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return n != 1;
    }

}
