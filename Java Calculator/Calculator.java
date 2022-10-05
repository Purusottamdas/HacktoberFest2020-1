// Fix the Code or Make it better.

import java.util.Scanner;

public class Calculator {
    //we can also use this to declear main in java "just for fun guys".
    //public static void main(String ...args){}
    //public static void main(String []args){}
    
    public static void main(String ...args) {

        Scanner reader = new Scanner(System.in);
        System.out.print("Enter two numbers: ");

        double first = reader.nextDouble();
        double second = reader.nextDouble();

        System.out.print("Enter an operator (+, -, *, /): ");
        char operator = reader.next().charAt(0);

        double result;

        switch(operator)
        {
            case '+':
                result = first + second;
                break;

            case '-':
                result = first - second;
                break;

            case '*':
                result = first * second;
                break;

            case '/':
                result = first / second;
                break;

            // operator doesn't match any case constant (+, -, *, /)
            default:
                System.out.printf("Error! operator is not correct");
                //return;
        }
        //Here we are using formated printing in java similar as C language.
        System.out.printf("%.1f %c %.1f = %.1f", first, operator, second, result);
    }
}
