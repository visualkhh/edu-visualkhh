package mailprogramming;

import java.util.Arrays;

/**
 * 정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오.
 * 단, 시간복잡도 O(n) 여야 합니다.
 * Given an array of integers and a target integer, find two indexes of the array element that sums to the target number.
 *
 * @Input: [2, 5, 6, 1, 10], 타겟 8
 * @Output: [0, 2] // 배열[0] + 배열[2] = 8
 */
public class Test5 {

    public void solution(int target, int[] datas) {

        for (int i = 0; i < datas.length; i++) {
            for (int j = 0; j < datas.length; j++) {
                if(i == j) {
                    continue;
                }
                if(datas[i] + datas[j] == target) {
                    System.out.println("i_index["+i+"]="+datas[i]+"  j_index["+j+"]="+datas[j] + " , sum="+target);
                    return;
                }
            }
        }
    }
    public static void main(String[] args) {
        new Test5().solution(8, new int[]{2, 5, 6, 1, 10});
    }
}
