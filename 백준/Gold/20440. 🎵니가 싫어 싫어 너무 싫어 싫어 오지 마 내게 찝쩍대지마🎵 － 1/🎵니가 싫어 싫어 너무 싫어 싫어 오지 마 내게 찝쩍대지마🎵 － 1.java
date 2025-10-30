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
        
        int e = 0; 

        // ⭐ 핵심: "모든 입장이 끝날 때까지"가 아니라 "모든 퇴장이 끝날 때까지"
        while (index_x < N) {
            
            // "입장" 이벤트가 다음 차례인지, "퇴장" 이벤트가 다음 차례인지 결정
            
            // Case 1: 입장 이벤트가 다음 차례
            // (아직 입장할 모기가 남았고, 다음 입장 시간이 다음 퇴장 시간보다 빠를 때)
            if (index_e < N && TE[index_e] < TX[index_x]) {
                
                if (count == max_count - 1) {
                    e = TE[index_e]; 
                }
                
                count++;
                
                if (count > max_count) {
                    max_count = count;
                    max_e = TE[index_e]; 
                    e = TE[index_e];     
                }
                index_e++;
                
            // Case 3: 입장/퇴장 동시
            // (아직 입장할 모기가 남았고, 다음 입장/퇴장 시간이 같을 때)
            } else if (index_e < N && TE[index_e] == TX[index_x]) {
                
                // 1. 퇴장 먼저 처리
                if (count == max_count && e == max_e) {
                    max_x = TX[index_x]; 
                }
                
                // 2. 입장 처리 (e 갱신 안 함 -> 연속 구간)
                
                index_e++;
                index_x++;

            // Case 2: 퇴장 이벤트가 다음 차례
            // (다음 입장 시간이 다음 퇴장 시간보다 늦거나, 더 이상 입장할 모기가 없을 때)
            } else {
                
                if (count == max_count && e == max_e) {
                    max_x = TX[index_x]; 
                }
                count--;
                index_x++;
            }
        }

        // ⭐ 요청대로 그 "두 번째" while 루프는 삭제했습니다.

        System.out.println(max_count);
        System.out.println(max_e + " " + max_x);
    }
}