import java.util.HashMap;
class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> map = new HashMap<>();
        String answer = "";
        for(String c : completion){
            if(map.containsKey(c)){
                int value = map.get(c);
                map.replace(c, value + 1);
            }
            else{
                map.put(c, 1);
            }
        }
        for(String p : participant){
            if(map.containsKey(p)){
                int value = map.get(p);
                if(value > 1)
                    map.replace(p, value - 1);
                else if(value == 1)
                    map.remove(p);
            }
            else
                answer = p;
        }
        
        return answer;
    }
}