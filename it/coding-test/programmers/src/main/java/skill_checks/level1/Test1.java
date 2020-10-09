package skill_checks.level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
 * 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
 * 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
 *
 * @제한사항  두 수는 1이상 1000000이하의 자연수입니다.
 * @예 자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.
 */
public class Test1 {
    public int[] solution(int n, int m) {
        int[] answer = {};
        return answer;
    }

    /* 약수 = 나누어 떨어지는값 (0제외)*/
    public List<Integer> 약수(int target) {
        List<Integer> data = new ArrayList<>();
        for (int i = 1; i <= target ; i++) {
            if ( (target % i) == 0 ) {
                data.add(i);
            }
        }
        return data;
    }
    // 공약수는 두 개 이상의 자연수의 공통된 약수에요
    // 공배수는 두 개 이상의 자연수의 공통된 배수에요
    public List<Integer> 공약수(List<Integer> a, List<Integer> b) {
        return duplicate(Arrays.asList(a, b));
    }

    // 배수
    public List<Integer> 배수(int data, int limit) {
        Integer[] datas = new Integer[limit];
        for (int i = 0; i < datas.length; i++) {
            datas[i] = data * (i + 1);
        }
        return Arrays.asList(datas);
    }
    public List<Integer> duplicate(List<List<Integer>> datas) {
        List<Integer> data = new ArrayList<>();
        List<Integer> criteria = datas.get(0);
        for (int i = 1; i < datas.size() ; i++) {
            for (int c = 0; c < criteria.size(); c++) {
                if(datas.get(i).contains(criteria.get(c))) {
                    data.add(criteria.get(c));
                }

            }
        }
        return data;
    }

    public static void main(String[] args) {
        Test1 solution = new Test1();
//        List<Integer> data = new Solution().약수(18);
        List<Integer> data1 = solution.약수(12);
        List<Integer> data2 = solution.약수(18);
        List<Integer> duplicate = solution.duplicate(Arrays.asList(data1, data2));

        System.out.println(data1);
        System.out.println(data2);
        System.out.println(duplicate);
//        System.out.println(solution.공약수(data1, data2));
    }
}
