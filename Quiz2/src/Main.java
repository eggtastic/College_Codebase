import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        char retry='y';
        while (retry=='y') {
            Random randomizer = new Random();
            Scanner scanning = new Scanner(System.in);
            int[] inputs = new int[4];
            int i = 0;
            do {
                System.out.print("Enter value for index " + i + ": ");
                int num = scanning.nextInt();
                inputs[i] = num;
                i++;
            } while (i < 4);
            System.out.println("Array: " + inputs[0] + " " + inputs[1] + " " + inputs[2] + " " + inputs[3]);
            int index = randomizer.nextInt(0, 4);
            int number = randomizer.nextInt(0, 4);
            System.out.print("Guess the number: ");
            int guess1 = scanning.nextInt();
            if (guess1==inputs[number]){
                System.out.println("Congratulations! You guessed the number!");
            } else {
                System.out.println("Wrong Number!");
            }
            System.out.print("Guess the index: ");
            int guess2 = scanning.nextInt();
            if (guess2==index){
                System.out.println("Congratulations! You guessed the index!");
            } else {
                System.out.println("Wrong index!");
            }
            int go_ahead=0;
            while (go_ahead==0) {
                System.out.print("Would you like to play again? (y/n): ");
                String input=scanning.next();
                retry=input.charAt(0);
                if (retry=='y' || retry=='Y' || retry=='n' || retry=='N'){
                    go_ahead=1;
                } else {
                    System.out.println("Invalid Input. Please state Y or N");
                }
            }

        }
    }
}