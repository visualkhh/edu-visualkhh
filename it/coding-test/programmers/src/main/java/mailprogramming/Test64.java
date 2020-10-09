package mailprogramming;

import java.util.Arrays;

/**
 * 사이즈가 m인 배열 X와 사이즈가 n인 배열 Y가 주어집니다.
 * 두 배열은 모두 정렬된 상태입니다.
 * 배열 X에는 정확히 n개의 비어있는 셀이 있다고 할 때,
 * 배열 Y의 원소를 X 배열로 합치며 원소들을 정렬 시키시오.
 *
 * @Input
 * X = [0, 2, 0, 3, 0, 5, 6, 0, 0] (비어있는 셀은 0으로 표현되었음)
 * Y = [1, 8, 9, 10, 15]
 *
 * @Output
 * X = [1, 2, 3, 5, 6, 8, 9, 10, 15]
 */
public class Test64 {

    public void solution(int[] x, int[] y) {
        // z = x와 y의 큰 length값으로 큰배열을 잡는다
//        int[] z = new int[x.length];

        // X를 돌며 0을 체크한다
        for (int i = 0; i < x.length; i++) {
            // 0부분일때 Y에서 가져와 z 넣는다  Y배열 가져간 부분을 0 체크한다
            if(x[i] == 0) {
                for (int j = 0; j < y.length; j++) {
                    if(y[j] != 0) {
                        x[i] = y[j];
                        y[j] = 0;
                        break;
                    }
                }
            }
        }

        Arrays.sort(x);
        for (int i = 0; i < x.length; i++) {
            System.out.print(" " + x[i]);
        }
        // 정렬한다.

    }
    public static void main(String[] args) {
        new Test64().solution(new int[]{0, 2, 0, 3, 0, 5, 6, 0, 0} , new int[]{1, 8, 9, 10, 15});
    }
}
