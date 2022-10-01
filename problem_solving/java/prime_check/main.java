import java.util.Scanner;

public class PrimeCheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Hello. Enter a whole number: ");
        int arg = sc.nextInt();
        String result = isPrimeNumber(arg) ? (arg + " is a prime number.") : (arg + " is a not a prime number.");
        System.out.println(result);
    }

    private static boolean isPrimeNumber(int arg)
    {
       if (arg <= 1)
            return false;
       for (int i = 2; i <= arg / 2; i++)
           if ((arg % i) == 0)
               return false;
       return true;
    }
}