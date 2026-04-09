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
        
        // 1. 배열의 크기는 우리가 '가진' 랜선의 개수인 K로 해야 합니다.
        int[] lens = new int[K]; 

        for(int i = 0; i < K; i++) lens[i] = Integer.parseInt(br.readLine());
        
        long high = (long) Math.pow(2,32);
        long low = 1; // 2. 0으로 나누는 에러 방지를 위해 최소 길이는 1로 시작
        long max_size = 0;
        
        while (true){
            long mid = (high+low)/2;
            long num = 0;
            
            // 3. 자를 때도 '가진' 랜선 K개만 잘라야 합니다.
            for(int i = 0; i < K; i++){ 
                num += lens[i]/mid;
            }
            
            if(num < N) {
                high = mid-1;
            } else {
                max_size = Math.max(max_size, mid);
                low = mid+1;
            }
            
            // 4. low와 high가 같을 때도 꼭 검사해야 하므로 '>' 일 때 break 합니다.
            if(low > high) break; 
        }
        System.out.println(max_size);
    }
}