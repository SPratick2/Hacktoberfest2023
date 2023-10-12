public class arrayFibonacciSeries {
    public static void main(String[] args) {
        int n = 10; // Number of Fibonacci numbers to generate

        System.out.println("Fibonacci Series (First " + n + " numbers):");
        int[] fibonacciSeries = generateFibonacci(n);
        
        for (int i = 0; i < n; i++) {
            System.out.print(fibonacciSeries[i] + " ");
        }
    }

    public static int[] generateFibonacci(int n) {
        int[] fibonacciSeries = new int[n];
        
        if (n >= 1) {
            fibonacciSeries[0] = 0;
        }
        if (n >= 2) {
            fibonacciSeries[1] = 1;
        }
        
        for (int i = 2; i < n; i++) {
            fibonacciSeries[i] = fibonacciSeries[i - 1] + fibonacciSeries[i - 2];
        }
        
        return fibonacciSeries;
    }
}
