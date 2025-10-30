import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] TE = new int[N];
        int[] TX = new int[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            TE[i] = Integer.parseInt(st.nextToken());
            TX[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(TE);
        Arrays.sort(TX);

        int max_e = 0, max_x = 0;
        int max_count = 0;
        int count = 0;
        int index_e = 0, index_x = 0;
        
        int e = 0; // "현재" max_count 구간이 시작된 시간

        while (index_e < N) {

            // Case 1: 입장 (TE[index_e] < TX[index_x])
            if (TE[index_e] < TX[index_x]) {
                
                // count가 max_count가 되기 직전 (복귀)
                if (count == max_count - 1) {
                    e = TE[index_e]; // 현재 max_count 구간 시작점을 갱신
                }
                
                count++;
                
                // *처음* max_count 갱신
                if (count > max_count) {
                    max_count = count;
                    max_e = TE[index_e]; // "가장 빠른" 시작점(max_e)을 고정
                    e = TE[index_e];     // "현재" 시작점(e)도 갱신
                }
                index_e++;
                
            // Case 2: 퇴장 (TE[index_e] > TX[index_x])
            } else if (TE[index_e] > TX[index_x]) {
                
                // 현재 구간(e)이 "가장 빠른" 구간(max_e)인가?
                if (count == max_count && e == max_e) {
                    max_x = TX[index_x]; // "가장 빠른" 구간의 끝을 갱신
                }
                count--;
                index_x++;
                
            // Case 3: 입장과 퇴장 동시 (TE[index_e] == TX[index_x])
            } else {
                
                // 1. 퇴장 먼저 처리
                if (count == max_count && e == max_e) {
                    max_x = TX[index_x]; // "가장 빠른" 구간의 끝을 갱신 (예제1: 6)
                }
                
                // 2. 입장 처리 (e를 갱신)
                // ⭐ 버그 수정: e = TE[index_e]; <--- 이 코드를 삭제
                // (count가 불변이므로 "현재" 구간 e는 바뀌지 않음)
                
                index_e++;
                index_x++;
            }
        }

        // 모든 입장이 끝난 후, 남은 퇴장 이벤트를 처리
        while (index_x < N) {
            // 마지막 구간 처리 (예제1: 여기서 max_x가 10으로 갱신됨)
            if (count == max_count && e == max_e) {
                 max_x = TX[index_x];
            }
            count--;
            index_x++;
        }

        System.out.println(max_count);
        System.out.println(max_e + " " + max_x);
    }
}