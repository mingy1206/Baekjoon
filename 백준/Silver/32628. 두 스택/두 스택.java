import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static long min_value;
    private static long[] A;
    private static long[] B;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        A = new long[N];
        B = new long[N];
        min_value = Long.MAX_VALUE;

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            long val = Long.parseLong(st.nextToken());
            if(i==0) A[i] = val;
            else A[i] = A[i-1] + val;
        }
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            long val = Long.parseLong(st.nextToken());
            if(i==0) B[i] = val; // 수정: B[i]
            else B[i] = B[i-1] + val; // 수정: B[i], B[i-1]
        }

        // N >= 1 이므로 N=0 예외처리 불필요
        poping(N, K);

        System.out.println(min_value);
    }

    public static void poping(int N, int K){
        // i : A 스택에서 뽑는 개수 (0 ~ K개)
        for(int i = 0; i <= K; i++){
            int j = K - i; // j : B 스택에서 뽑는 개수

            // 경계 조건 체크
            if(i > N || j > N || j < 0) {
                continue;
            }

            // A에서 i개 뽑고 남은 합
            long sumA;
            if (i == N) {
                sumA = 0; // A를 모두 비움
            } else {
                // A[N-i-1]은 A1 ~ A(N-i) 까지의 합
                sumA = A[N - i - 1]; 
            }

            // B에서 j개 뽑고 남은 합
            long sumB;
            if (j == N) {
                sumB = 0; // B를 모두 비움
            } else {
                // B[N-j-1]은 B1 ~ B(N-j) 까지의 합
                sumB = B[N - j - 1];
            }

            long maxRemain = Math.max(sumA, sumB);
            min_value = Math.min(min_value, maxRemain);
        }
    }
}