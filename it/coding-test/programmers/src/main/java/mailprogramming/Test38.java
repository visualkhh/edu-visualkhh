package mailprogramming;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 1~N 까지 있는 정수 배열에 원소 하나가 없어졌습니다. 없어진 원소의 값을 구하시오.
 * Given an integer array of 1~N except one number, find the missing integer.
 */
public class Test38 {

    public void solution(int end, int[] array) {
        int i = (end + 1) * end / 2;
        int r = i - Arrays.stream(array).sum();
        System.out.println(r);
    }
    public static void main(String[] args) {
        new Test38().solution(10, new int[]{1, 2, 3, 4, 5, 6, 7, 9, 10});
    }
}
