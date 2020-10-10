package mailprogramming;

import java.util.Arrays;

/**
 * 바이너리 배열(원소를 0, 1만 갖는 배열)이 주어졌을 때, 배열을 정렬하시오.
 * 단, 시간 복잡도는 O(n), 공간 복잡도는 O(1).
 * 결과는 0이 먼저 출력되고 1이 출력되어야 합니다.
 *
 * @Input: [1, 0, 1, 0, 1, 0, 0, 1]
 * @Output: [0, 0, 0, 0, 1, 1, 1, 1]
 */
public class Test59 {

    public void solution(boolean[] datas) {

        System.out.println("input: " + Arrays.toString(datas));
        for (int i = 0; i < datas.length; i++) {
            boolean f = false;
            for (int j = 0; j < datas.length -i -1; j++) {
                if(datas[j] == true && datas[j+1] == false) {
                    f = datas[j];
                    datas[j] = datas[j+1];
                    datas[j+1] = f;
                }
            }
        }

        System.out.println(Arrays.toString(datas));
    }
    public static void main(String[] args) {
        new Test59().solution(new boolean[]{true, false, true, false, true, false, false, true, false});
//        new Test59().solution(new boolean[]{true, false, true, false});
    }
}
