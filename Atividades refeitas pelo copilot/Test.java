public class Test {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        // Example of a simple addition
        int a = 5;
        int b = 10;
        int sum = a + b;
        System.out.println("The sum of " + a + " and " + b + " is " + sum);

        // Example of a loop
        System.out.println("Counting from 1 to 5:");
        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
        }

        // Example of a method call
        System.out.println("Factorial of 5 is: " + factorial(5));
    }

    // Method to calculate factorial
    public static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}