import java.util.HashSet;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int N2 = nums.length/2;
        HashSet<Integer> hs = new HashSet<>();
        for(int num : nums) hs.add(num);
        int hs_len = hs.size();
        if(hs_len > N2)
            answer = N2;
        else
            answer = hs_len;

        return answer;
    }
}

   