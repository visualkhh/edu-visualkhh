package test;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 뒤로읽어도 같은 문자가 되도록 만들고 그 길이를 리턴하라.
 * @예
 * ababaaaa = 8
 * abab = 5
 * abcde = 9
 *
 */
public class Test3 {

    public int solution(String plain) {
        List<Character> chars = plain.chars().mapToObj(e->(char)e).collect(Collectors.toList());
        List<Character> rChars = new ArrayList<>(chars);
        Collections.reverse(rChars);
        System.out.println(chars);
        System.out.println(rChars);

        int index = -1;
        main: for (int i = 0; i < chars.size(); i++) {
            boolean sw = false;
            for (int j = 0; j < rChars.size() && (i+j) <chars.size(); j++) {
                Character c = chars.get(i+j);
                Character rc = rChars.get(j);
                System.out.print("\t>" + c + ","+rc);
                if(!c.equals(rc)) {
                    index = i - j;
                    break;
                } else {
                    index = i - j;
                    break main;
                }
            }
            System.out.println("--sw "+ sw + ",  "+index);
        }
        return chars.size() + index;
    }

    public static void main(String[] args) {
//        int x = new Test1().solution(2613);
//        int x = new Test3().solution("ababaaaa");
//        int x = new Test3().solution("abab");
        int x = new Test3().solution("abcde");
        System.out.println("no such number -> " + x);
    }
}
