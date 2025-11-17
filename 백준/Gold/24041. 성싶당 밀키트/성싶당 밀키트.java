// (패키지명은 환경에 맞게 수정하세요)

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static int N, K;
    static long G; // G와 총 세균 합은 long 범위여야 함
    static long[] S, L; // S와 L 값도 10^9까지 가능
    static int[] O;

    public static void main(String[] args) throws IOException {
        // 1. 입력 (Input)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        G = Long.parseLong(st.nextToken()); // G를 long으로 받음
        K = Integer.parseInt(st.nextToken());

        S = new long[N]; // long 배열
        L = new long[N]; // long 배열
        O = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            S[i] = Long.parseLong(st.nextToken()); // long으로 읽기
            L[i] = Long.parseLong(st.nextToken()); // long으로 읽기
            O[i] = Integer.parseInt(st.nextToken());
        }

        // 2. 처리 (Processing)
        // Parametric Search (이분 탐색)
        // 날짜 x를 1씩 증가시키는 대신, 1 ~ 20억 범위에서 이분 탐색
        long left = 1;
        // L_i와 G가 10^9 단위. S_i=1, L_i=1, G=10^9 이면 x = 10^9+1 까지 가능.
        // S_i=1, L_i=10^9, G=10^9 이면 x = 2*10^9 까지 가능.
        long right = 2_000_000_001L; // 넉넉하게 20억 + 1
        long ans = 0; // 가능한 최대 날짜 (정답)

        while (left <= right) {
            long midDay = (left + right) / 2; // 이번에 검사할 날짜 (x)

            if (check(midDay)) {
                // [핵심] midDay가 가능하다면
                ans = midDay;       // 일단 답으로 저장하고
                left = midDay + 1;  // 더 늦은 날(더 큰 x)도 가능한지 탐색
            } else {
                // [핵심] midDay가 불가능(세균 초과)하다면
                right = midDay - 1; // 더 이른 날(더 작은 x)을 탐색
            }
        }

        // 3. 출력 (Output)
        System.out.println(ans);
    }

    /**
     * @param day : 검사하고자 하는 날짜 x
     * @return : K개를 뺐을 때 G 이하로 먹을 수 있으면 true, 아니면 false
     */
    static boolean check(long day) {
        // [핵심 로직] 님이 짠 PQ 로직을 그대로 사용 (단, long 타입 주의)
        long totalGerms = 0;
        // 세균 수를 내림차순(Max Heap)으로 정렬할 우선순위 큐
        // 세균 수가 int 범위를 넘을 수 있으므로 PriorityQueue<Long> 사용
        PriorityQueue<Long> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < N; i++) {
            // S_i * max(1, x - L_i)
            // S[i] * (day - L[i]) 계산 시 int 오버플로우 발생 가능 -> long으로 계산
            long germs = S[i] * Math.max(1, day - L[i]);
            totalGerms += germs;

            if (O[i] == 1) { // 뺄 수 있는 재료(O_i=1)라면
                pq.add(germs);
            }
        }

        // 1. K개를 하나도 안 빼도 G 이하인가?
        if (totalGerms <= G) {
            return true;
        }

        // 2. G를 넘는다면, K개까지 세균이 많은 순서대로 빼본다
        int removeCount = 0;
        while (removeCount < K && !pq.isEmpty()) {
            totalGerms -= pq.poll(); // 세균 수가 가장 많은 놈을 뺀다
            removeCount++;

            if (totalGerms <= G) {
                return true; // 빼는 도중에 G 이하가 되면 성공
            }
        }

        // 3. K개를 다 뺐는데도 G보다 크면 실패
        return (totalGerms <= G);
    }
}