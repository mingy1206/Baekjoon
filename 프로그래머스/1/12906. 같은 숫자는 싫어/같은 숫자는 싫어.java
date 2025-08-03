import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
		List<Integer> li = new ArrayList<>();
		int before = -1;
		
		for (int i : arr) {
			if(before == i) continue;
			else {
				li.add(i);
				before = i;
			}
		}
		int len = li.size();
		int[] answer = new int[len];
		for(int i = 0; i < len; i++)
			answer[i] = li.get(i);
			
		return answer;
	}
}