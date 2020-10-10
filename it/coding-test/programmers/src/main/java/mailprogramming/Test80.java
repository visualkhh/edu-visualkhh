package mailprogramming;

import java.util.Arrays;

/**
 * 사전 순서 상 가장 앞의 문자열 회전 (Lexicographically minimal string rotation)은
 * 주어진 문자열을 돌려서 (맨 앞의 문자가 맨 뒤로 가거나, 맨 뒤의 문자가 맨 뒤로 가도록 변경) (연속된 두글)
 * 만들 수 있는 문자열 중 사전 순서 상 가장 앞에 오는 문자열을 찾는 문제입니다.
 *
 * 주어진 문자열을 회전시켜 사전 순서 상 가장 앞의 문자열을 찾으시오.
 * @Input: bbaaccaadd
 * @Output: aaccaaddbb
 */
public class Test80 {

    public void solution(String str) {
//        String[] split = str.split("/([a-z]{2})/gm");
//        String[] split = str.split("[0-9]{1}");
        System.out.println(str.replaceAll("([a-z]){2}", "$1--"));
        String[] split = str.replaceAll("[a-z]{1}", "--").split("--");

//        for (int i = 0; i < split.length; i++) {
//            split[i] = new StringBuilder(split[i]).reverse().toString();
//        }
        System.out.println(Arrays.toString(split));

    }
    public static void main(String[] args) {
        new Test80().solution("bbvbaa0c1c9aadd");
    }
}
