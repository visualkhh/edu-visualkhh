package skill_checks.level1;

import java.util.Arrays;
import java.util.List;
import java.util.StringJoiner;
import java.util.stream.Collectors;

/**
 * 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
 * s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
 * @제한사항 str은 길이 1 이상인 문자열입니다.
 * @예 Zbcdefg -> gfedcbZ
 */

public class Test2 {

    public String solution(String s) {
        List<Character> chars = s.chars().mapToObj(c -> (char) c).collect(Collectors.toList());
//        char[] listC = s.toCharArray();
//        Character[] array = listC.toArray(new Character[listC.size()]);
        List<Character> sorted = chars.stream().sorted((a, b) -> b - a).collect(Collectors.toList());

//        Character[] characters = sorted.toArray(new Character[sorted.size()]);
//        characters
//        new String(String.valueOf()));
//        sorted.stream().collect(Collectors.joining());
//        return sorted.stream().collect(Collectors.joining(""));

//        new StringJoiner("").;

//        String[] names = new String[] {"홍길동", "임꺽정", "슈퍼맨", "배트맨", "아이언맨" };
//        List<String> nameList = Arrays.asList(names);
//        String sql1 = nameList.stream()
////                .map(name -> "'" + name + "'" )
//                .collect(Collectors.joining(","));

        return sorted.stream().map(it -> it.toString()).collect(Collectors.joining());
    }

    public static void main(String[] args) {
        String data = new Test2().solution("Zbcdefg");
        System.out.println(data);
    }
}
