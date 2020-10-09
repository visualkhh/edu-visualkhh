package mailprogramming;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.stream.Collectors;

/**
 * 정렬된 양수(positive integer) 배열이 주어지면, 배열 원소들의 합으로 만들수 없는 가장 작은 양수를 구하시오.
 * 단, 시간복잡도는 O(n) 이여야 합니다.
 * Given an array of positive integers, find the smallest positive integer that cannot be created by adding elements in the array.
 *
 * @input: [1, 2, 3, 8]
 * @output: 7
 *
 * // 1 = 1
 * // 2 = 2
 * // 3 = 3
 * // 4 = 1 + 3
 * // 5 = 2 + 3
 * // 6 = 1 + 2 + 3
 * // 7 = 불가능
 */
public class Test28 {

    int[] data;

    public Test28(int[] data) {
        this.data = data;
        printArray("init", this.data);
    }

    public int[] solution() {
        for (int i = 0; i < 100; i++) {
//            for (int groupSize = 0; groupSize < 6; groupSize++) {
//
//            }
//            int groupSize = 2;
            for (int j = 0; j < this.data.length; j++) {
                this.sum(i, j, 1);

            }

        }
        return null;
    }

    public List<Integer> sum(int sIndex, int eIndex, int groupSize) {
        int groupSum = this.groupSum(sIndex, eIndex);
        System.out.println("groupSum " +groupSum);
        int[] first = Arrays.copyOfRange(this.data, 0, sIndex);
        int[] second = Arrays.copyOfRange(this.data, eIndex, this.data.length);
//        this.printArray("first", first);
//        this.printArray("second", second);

        int aLen = first.length;
        int bLen = second.length;
        int[] result = new int[aLen + bLen];

        System.arraycopy(first, 0, result, 0, aLen);
        System.arraycopy(second, 0, result, aLen, bLen);
//        this.printArray("result", result);

        List<Integer> data = new ArrayList<>();
        int gSum = 0;
        for (int i = 0; i < result.length; i++) {
            int n = i + 1;
            gSum += result[i];
            if(n % groupSize == 0 || n == result.length) {
                data.add(gSum);
                gSum = 0;
            } else {
            }

        }
//        data.add(groupSum);
        printArray("groups", data.stream().mapToInt(i->i).toArray());
        return data;
    }

    public int groupSum(int sIndex, int eIndex) {
        int sum = 0;
        for (int i = sIndex; i <= eIndex; i++) {
            sum += this.data[i];
        }
        return sum;
    }


    public void printArray(String title, int[] x){
        System.out.println(title);
        for (int i = 0; i < x.length; i++) {
            System.out.print(" " + x[i]);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] solution = new Test28(new int[]{1, 5, 4, 6, 9, 2, 3, 8}).solution();
//        for (int i = 0; i < solution.length; i++) {
//            System.out.print(" " + solution[i]);
//        }
    }
}
