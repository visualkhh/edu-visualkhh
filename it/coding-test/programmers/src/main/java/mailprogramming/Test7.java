package mailprogramming;

import java.util.Arrays;

/**
 * 주어진 string 에 모든 단어를 거꾸로 하시오.
 * Reverse all the words in the given string.
 * 예제)
 * @Input: “abc 123 apple”
 * @Output: “cba 321 elppa”
 */
public class Test7 {

    public void solution(String str) {
        String[] split = str.split(" ");

        for (int i = 0; i < split.length; i++) {
            split[i] = new StringBuilder(split[i]).reverse().toString();
        }
        System.out.println(Arrays.toString(split));

    }
    public static void main(String[] args) {
        new Test7().solution("abc 123 apple");
    }
}
