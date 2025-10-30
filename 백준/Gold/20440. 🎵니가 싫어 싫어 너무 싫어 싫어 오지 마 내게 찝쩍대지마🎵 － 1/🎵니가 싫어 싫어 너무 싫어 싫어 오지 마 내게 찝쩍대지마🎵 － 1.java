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

        while (index_x < N) {

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

            } else if (index_e < N && TE[index_e] == TX[index_x]) {

                if (count == max_count && e == max_e) {
                    max_x = TX[index_x];
                }


                index_e++;
                index_x++;


            } else {

                if (count == max_count && e == max_e) {
                    max_x = TX[index_x];
                }
                count--;
                index_x++;
            }
        }

        System.out.println(max_count);
        System.out.println(max_e + " " + max_x);
    }
}