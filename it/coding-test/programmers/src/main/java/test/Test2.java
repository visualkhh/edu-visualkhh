package test;


import java.util.Arrays;

/**
 *
 */
public class Test2 {

    public String solution(String encrypted_text, String key, int rotation) {
        System.out.println("encrypted_text:" + encrypted_text + "  key:"+ key + "  rotation:" + rotation);
        char[] alphabet = {
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        };
        char[] keyChars = key.toCharArray();
        char[] enRoChars = encrypted_text.toCharArray();
        char[] enChars = new char[enRoChars.length];
        //회전
        for (int i = 0; i < enRoChars.length; i++) {
            char jumpChar = jump(enRoChars, rotation + i);
            enChars[i] = jumpChar;
        }
        System.out.println(Arrays.toString(enChars));
        // 빼자
        char[] rData = new char[enChars.length];
        for (int i = 0; i < enChars.length; i++) {
            char enChar = enChars[i];
            char keyChar = keyChars[i];
            int enCharOrder = charToOrder(enChar);
            int keyCharOrder = charToOrder(keyChar);
            int i1 = enCharOrder - keyCharOrder;
            i1 = i1-1;
            char jump = jump(alphabet, i1);
            rData[i] = jump;
//            System.out.print(jump+ ", ");
        }

        return new String(rData);
    }

    public char jump(char[] datas, int jump) {
        int i = jump % datas.length;
        if(i < 0 ){
            i = datas.length + i;
        }
        return datas[i];
    }

    public int charToOrder(char c)  {
        return c - 97;
    }


    public static void main(String[] args) {
        // 글자 11
        //result: hellopython
        String x = new Test2().solution(
                "qyyigoptvfb",
                "abcdefghijk"
                , 3);
        System.out.println("--> " + x);
    }
}
