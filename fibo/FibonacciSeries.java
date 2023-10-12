public class FibonacciSeries {
    public static void main(String[] args) {
        int n = 10; // Number of Fibonacci numbers to generate
        generateFibonacci(n);
    }

    public static void generateFibonacci(int n) {
        long first = 0;
        long second = 1;

        System.out.println("Fibonacci Series (First " + n + " numbers):");

        for (int i = 0; i < n; i++) {
            System.out.print(first + " ");
            long next = first + second;
            first = second;
            second = next;
        }
    }
}
