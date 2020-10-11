package test;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 자연수 N을 주어지면  오른참순, 내림차순 처리하고  그 두수를 합쳐라.
 * @예
 * 2613 = 7557
 * 33285 108690
 *
 */
public class Test1 {

    public int solution(int N) {
        String s = Integer.toString(N);
        System.out.println(s);
        char[] chars = s.toCharArray();
        List<Character> charList = new ArrayList<>();
        for (char c: chars) {
            charList.add(c);
        }
        System.out.println(charList);

        List<Character> up = charList.stream().sorted((a, b) -> a.compareTo(b)).collect(Collectors.toList());
        List<Character> down = charList.stream().sorted((a, b) -> b.compareTo(a)).collect(Collectors.toList());
        System.out.println(up);
        System.out.println(down);

        String ups = up.stream().map(it -> it.toString()).collect(Collectors.joining());
        String downs = down.stream().map(it -> it.toString()).collect(Collectors.joining());
        System.out.println(ups);
        System.out.println(downs);

        int upInt = Integer.parseInt(ups);
        int downInt = Integer.parseInt(downs);
        int result = upInt + downInt;
        return result;
    }

    public static void main(String[] args) {
//        int x = new Test1().solution(2613);
        int x = new Test1().solution(1212121451);
        System.out.println("no such number -> " + x);
    }
}
