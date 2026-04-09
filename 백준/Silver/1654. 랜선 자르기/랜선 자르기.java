import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        
        int[] lens = new int[K]; // N이 아니라 K개의 랜선을 가지고 있음
        long high = 0; // 가지고 있는 랜선 중 최장 길이를 찾기 위함
        
        for(int i = 0; i < K; i++) {
            lens[i] = Integer.parseInt(br.readLine());
            if(high < lens[i]) {
                high = lens[i]; // 입력과 동시에 최댓값 찾기
            }
        }
        
        long low = 1; // 길이는 최소 1이어야 함 (0으로 나누기 방지)
        long max_size = 0;
        
        // 이분 탐색의 가장 정석적인 형태
        while (low <= high) {
            long mid = (low + high) / 2;
            long count = 0; // 잘라낸 랜선의 총 개수
            
            for(int i = 0; i < K; i++){ // N이 아니라 K개의 랜선을 자름
                count += lens[i] / mid;
            }
            
            // 핵심: 범위를 어떻게 줄일 것인가?
            if(count >= N) { 
                // 원하는 개수 이상을 만들었다면, 길이를 더 늘려봐도 되는지 확인
                max_size = mid;   // 일단 정답 후보로 저장
                low = mid + 1;    // 길이를 늘린다 (오른쪽 탐색)
            } else {
                // 개수가 부족하다면, 길이를 무조건 줄여야 함
                high = mid - 1;   // 길이를 줄인다 (왼쪽 탐색)
            }
        }
        
        System.out.println(max_size);
    }
}