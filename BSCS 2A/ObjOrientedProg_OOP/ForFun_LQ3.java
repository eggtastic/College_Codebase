import java.util.*;

public class ForFun_LQ3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random randomizer = new Random();

        char retry = 'y';
        char randomanual;

        String[] basket1 = new String[5];
        String[] basket2 = new String[7];

        while(retry=='y'){
            int f = 0;
            System.out.println("BASKET #1: FRUIT.");

            do {
                System.out.print("Enter Fruits for Basket#1, index " + f + ": ");
                String fruits = sc.nextLine();
                basket1[f] = fruits;
                f++;
            } while (basket1.length > f);

            System.out.println("FRUITS BASKET: "+Arrays.toString(basket1) + " ");

            System.out.println("BASKET #2: VIANDS.");

            int v = 0;
            do {
                System.out.print("Enter Viands for Basket#2, index " + v + ": ");
                String dishes = sc.nextLine();
                basket2[v] = dishes;
                v++;
            } while (basket2.length > v);

            System.out.println("VIANDS BASKET: "+Arrays.toString(basket2) + " ");

            // randomizer/manual
            int continues=0;
            while (continues==0) {
                System.out.print("Would you like for me to choose randomly or choose manually? (r/m): ");
                String input = sc.next();
                randomanual = input.charAt(0);
                if (randomanual == 'r' || randomanual == 'R') {
                    continues = 1;
                } else {
                    System.out.println("Invalid Input. Please state Y or N");
                }
            }

            // retry logic
            int go_ahead=0;
            while (go_ahead==0) {
                System.out.print("Would you like to refill the baskets again? (y/n): ");
                String input = sc.next();
                retry = input.charAt(0);
                if (retry == 'y' || retry == 'Y' || retry == 'n' || retry == 'N') {
                    go_ahead = 1;
                } else {
                    System.out.println("Invalid Input. Please state Y or N");
                }
            }
        }
    }
}
