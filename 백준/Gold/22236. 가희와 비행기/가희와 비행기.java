import java.io.*;
import java.util.StringTokenizer;

public class Main {
    private static int d;
    private static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        d = Integer.parseInt(st.nextToken()); // 수평 거리
        m = Integer.parseInt(st.nextToken()); // mod 값

        System.out.println(solve());
    }

    private static long solve() {
        // dp[x][h] : 수평 거리 x까지 이동했을 때 고도 h에 있는 경우의 수
        long[][] dp = new long[d + 1][d + 1];
        dp[0][0] = 1; // 시작점

        for (int x = 0; x < d; x++) {
            for (int h = 0; h <= d; h++) {
                long cur = dp[x][h];
                if (cur == 0) continue;

                // 1. 상승 (h -> h + 1)
                if (h + 1 <= d) {
                    dp[x + 1][h + 1] = (dp[x + 1][h + 1] + cur) % m;
                }

                // 2. 하강 (h -> h - 1)
                if (h - 1 >= 0) {
                    // 도착 전에는 고도 0으로 내려가면 안 됨 (중간 착륙 금지)
                    if (x + 1 != d && h - 1 == 0) continue;
                    dp[x + 1][h - 1] = (dp[x + 1][h - 1] + cur) % m;
                }
            }
        }

        // 최종적으로 거리 d에서 고도 0인 경우만 유효
        return dp[d][0] % m;
    }
}
