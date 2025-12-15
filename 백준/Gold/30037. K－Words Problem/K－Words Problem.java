import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        if (line == null || line.trim().isEmpty()) return;
        
        int N = Integer.parseInt(line.trim());

        while (N-- > 0) {
            String sentence = br.readLine();
            if (sentence == null) break;

            // 1. 문장을 단어 리스트로 변환
            String[] tokens = sentence.trim().split(" ");
            ArrayList<String> words = new ArrayList<>(Arrays.asList(tokens));

            // 2. [Rule 2] "Word of Korea" -> "K-Word" (앞에서부터)
            int i = 0;
            while (i <= words.size() - 3) {
                String prevW = words.get(i);      // Word
                String ofW = words.get(i + 1);    // of
                String koreaW = words.get(i + 2); // Korea

                String[] prevParts = splitPunct(prevW);
                String[] koreaParts = splitPunct(koreaW);

                boolean isMatch = true;

                // 조건 체크
                if (!ofW.equals("of")) isMatch = false;
                else if (!koreaParts[0].equals("Korea")) isMatch = false;
                else if (!prevParts[1].isEmpty()) isMatch = false; // 앞 단어에 문장부호 있으면 안됨

                if (isMatch) {
                    String newMain = capitalize(prevParts[0]);
                    // Korea 뒤에 있던 문장부호(koreaParts[1])를 가져와 붙임
                    String newWord = "K-" + newMain + koreaParts[1];

                    words.set(i, newWord);
                    words.remove(i + 2); // Korea 삭제
                    words.remove(i + 1); // of 삭제
                    
                    // 성공 시 인덱스 유지 (중첩 적용 가능성)
                } else {
                    i++;
                }
            }

            // 3. [Rule 1] "Korea Word" -> "K-Word" (뒤에서부터)
            i = words.size() - 2;
            while (i >= 0) {
                String koreaW = words.get(i);
                String nextW = words.get(i + 1);

                if (koreaW.equals("Korea")) {
                    String[] nextParts = splitPunct(nextW);

                    String newMain = capitalize(nextParts[0]);
                    // 뒤 단어의 문장부호(nextParts[1]) 유지
                    String newWord = "K-" + newMain + nextParts[1];

                    words.set(i, newWord);
                    words.remove(i + 1);
                }
                i--;
            }

            // 4. 결과 바로 출력 (String.join 사용)
            System.out.println(String.join(" ", words));
        }
    }

    // [헬퍼] 단어를 {알맹이, 문장부호} 로 분리
    static String[] splitPunct(String s) {
        if (s.isEmpty()) return new String[]{"", ""};
        char last = s.charAt(s.length() - 1);
        if ("!?,.".indexOf(last) != -1) {
            return new String[]{s.substring(0, s.length() - 1), String.valueOf(last)};
        }
        return new String[]{s, ""};
    }

    // [헬퍼] 첫 글자 대문자화
    static String capitalize(String s) {
        if (s == null || s.isEmpty()) return s;
        if (Character.isLowerCase(s.charAt(0))) {
            return Character.toUpperCase(s.charAt(0)) + s.substring(1);
        }
        return s;
    }
}