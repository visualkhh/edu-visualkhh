package mailprogramming;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

/**
 * 정렬된 양수(positive integer) 배열이 주어지면, 배열 원소들의 합으로 만들수 없는 가장 작은 양수를 구하시오.
 * 단, 시간복잡도는 O(n) 이여야 합니다.
 * Given an array of positive integers, find the smallest positive integer that cannot be created by adding elements in the array.
 *
 * @input: [1, 2, 3, 8]
 * @output: 7
 * <p>
 * // 1 = 1
 * // 2 = 2
 * // 3 = 3
 * // 4 = 1 + 3
 * // 5 = 2 + 3
 * // 6 = 1 + 2 + 3
 * // 7 = 불가능
 */
public class Test28 {

    public static class RowData {
        int[] row;
        public RowData(int[] row) {
            this.row = row;
        }
        public int getSum() {
            return Arrays.stream(row).sum();
        }

        @Override
        public String toString() {
            return "RowData" +
                    "row=" + Arrays.toString(row) + ", sum:"+this.getSum();
        }
    }

    public int solution(int dest, int[] data) {

        System.out.println("intput data d:" + dest+ " " + Arrays.toString(data));

        List<RowData> container = new ArrayList<>();
        double rowCnt = Math.pow(2, data.length);

        // 경우의수 별로 array 생성 = 합
        boolean[] swRows = new boolean[data.length];
        Arrays.fill(swRows, true);

        for (int row = 1; row <= rowCnt; row++) {
            int[] newRows = new int[data.length];
            for (int j = 0; j < data.length; j++) {
                double dPow = Math.pow(2, j);
                double v = (row) % dPow;
                if(swRows[j]) {
                    newRows[j] = data[j];
                }
                if (v == 0) {
                    swRows[j] = !swRows[j];
                }
            }
            container.add(new RowData(newRows));
        }

        int r = 0;
        // 1~999까지 돌면서 경우의수의 합중에 지금것이 있는지 확인.
//        IntStream.range(0, dest).filter(it -> {
//            return container.stream().filter(cit -> it == cit.getSum()).findAny().isPresent();
//        });

        main: for (int i = 1; i <= dest; i++) {
            for (int j = 0; j < container.size(); j++) {
                if(i == container.get(j).getSum()){
                    continue main; // 있으면 continue
                }
            }
            if(r == 0) { // 없으면 리턴
                r = i;
                break;
            }
        }
        container.forEach(it -> System.out.println(it.toString()));
        return r;
    }



    public static void main(String[] args) {
//        int x = new Test28().solution(999, new int[]{1, 5, 4, 6, 9, 2, 3, 8});
        int x = new Test28().solution(999, new int[]{1, 2, 3, 8});
        System.out.println("no such number -> " + x);
    }
}
