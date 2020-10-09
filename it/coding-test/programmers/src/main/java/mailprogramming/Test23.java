package mailprogramming;

import java.util.Arrays;

/**
 * 정수 배열과 정수 k가 주어지면 모든 원소를 k칸씩 앞으로 옮기시오.
 * Given an array and an integer K, shift all elements in the array K times.
 *
 * @input: [1, 2, 3, 4, 5], k = 2
 * @output: [3, 4, 5, 1, 2]
 *
 * @input: [0, 1, 2, 3, 4], k = 1
 * @output: [1, 2, 3, 4, 0]
 *
 * 시간복잡도와 공간복잡도를 최대한 최적화 하시오.
 */
public class Test23 {

    public void solution(int size, int[] array) {
        size = size % array.length;
        int[] first = Arrays.copyOfRange(array, 0, size);
        int[] second = Arrays.copyOfRange(array, size - 1, array.length);

        int aLen = first.length;
        int bLen = second.length;
        int[] result = new int[aLen + bLen];

        System.arraycopy(second, 0, result, 0, bLen);
        System.arraycopy(first, 0, result, bLen, aLen);
        for (int i = 0; i < result.length; i++) {
            System.out.print(" " + result[i]);
        }
    }
    public static void main(String[] args) {
        new Test23().solution(5, new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    }
}
