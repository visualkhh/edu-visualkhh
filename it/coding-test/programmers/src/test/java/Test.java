public class Test {
    public static void main(String[] args) {
        int x = 1;
        for (int i = 0; i < 10; i++) {
            int num = i + 1;
            System.out.println(num + "\t" + Math.pow(2, i)+ "\t" + x);
            x = x * 2;
        }
    }
}
