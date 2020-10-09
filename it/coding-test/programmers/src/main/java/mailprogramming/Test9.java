package mailprogramming;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.stream.Collectors;

/**
 * 정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오. 단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.
 * Given an integer array, move all the 0s to the right of the array without changing the order of non-zero elements.
 *
 * @Input: [0, 5, 0, 3, -1]
 * @Output: [5, 3, -1, 0, 0]
 *
 * @Input: [3, 0, 3]
 * @﻿Output: [3, 3, 0]
 */
public class Test9 {

    public int[] solution(int[] x) {
        int[] y = new int[x.length];
        for (int i = 0; i < x.length; i++) {
            if(x[i] != 0) {
                for (int j = 0; j < y.length; j++) {
                    if(y[j] == 0) {
                        y[j] = x[i];
                        break;
                    }
                }
            }
        }
        return y;
    }

    public int[] solution1(int[] x) {
        Stack<Integer> st = new Stack<Integer>();
        Stack<Integer> zeroSt = new Stack<Integer>();
        for (int i = 0; i < x.length; i++) {
            if (x[i] != 0) {
                st.push(x[i]);
            } else {
                zeroSt.push(x[i]);
            }
        }
        List<Integer> data = new ArrayList<>();
        data.addAll(st);
        data.addAll(zeroSt);
        return data.stream().mapToInt(Integer::intValue).toArray();
    }

    public int[] solution2(int[] x) {
        List<Integer> list = Arrays.stream(x).boxed().collect(Collectors.toList());
        List<Integer> st = list.stream().filter(it -> it != 0).collect(Collectors.toList());
        List<Integer> zeroSt = list.stream().filter(it -> it == 0).collect(Collectors.toList());
        st.addAll(zeroSt);
        return st.stream().mapToInt(Integer::intValue).toArray();
    }

    public int[] solution3(int[] x) {
        List<Integer> list = Arrays.stream(x).boxed().collect(Collectors.toList());
        List<Integer> collect = list.stream().filter(it -> it != 0).collect(Collectors.toList());
        Integer[] integers = collect.toArray(new Integer[x.length]);
        return Arrays.stream(integers).mapToInt((i) -> null == i ? 0 : i.intValue()).toArray();
    }

    public static void main(String[] args) {
        int[] solution = new Test9().solution3(new int[]{0, 2, 0, 3, 0, 5, 6, 0, 0});
        for (int i = 0; i < solution.length; i++) {
            System.out.print(" " + solution[i]);
        }
    }
}
