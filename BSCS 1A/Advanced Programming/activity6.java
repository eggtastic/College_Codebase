import java.util.Scanner;

public class Lim_activity6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("-- ATTENDANCE CHECKER-- \n");

        // array size
        System.out.print("Number of Students: ");
        int size = sc.nextInt();
        int[] studentID = new int[size];
        sc.nextLine();

        System.out.print("\n");

        // seat logic
        int seat = 1;

        int increaseSize = 0;
        int reducedID = size - 1;

        for (int i= 0; i < studentID.length; i++){
            System.out.print("Seat "+ seat + " -> ID: ");
            studentID[i] = sc.nextInt();
            seat += 1;
        }

        System.out.print("\nRemove a student?: ");
        int studentRemove = sc.nextInt();
        studentID[studentRemove-1] = 0;

        int a = 0;
        seat = 1;

        for (int b= 0; a < studentID.length-1; b++){
            if (studentID[b] == 0) {
                continue;
            }
            else {
                a ++;
                System.out.print("Seat "+ (a) + " -> ID: " + studentID[b] + "\n");
            };
        }

    }
}

