import java.util.Scanner;
import javax.swing.*;


public class Main {
   public static int buyDrink(int stickers, int amount){
       int currentStickers = stickers + amount;
       return currentStickers;
   }
   public static boolean checkStatus(int stickers){
       if (stickers <= 11){
           JOptionPane.showMessageDialog(
                   null,
                   "Keep drinking... Please come again!"
           );
           return true;
       } else {
           JOptionPane.showMessageDialog(
                   null,
                   "STATUS: REWARD UNLOCKED!"
           );
           return false;
       }
   }
   public static void rewardChoices(int choice){
       String reward = "";
       switch(choice){
           case 1: reward = "Cat Pen"; break;
           case 2: reward = "Cat-Themed Notebook"; break;
           case 3: reward = "-200 OFF Voucher"; break;
           default: reward = "ERROR: INVALID";break;
       }
       JOptionPane.showMessageDialog(
               null,
               "You claimed a " + reward + "!",
               "Cafe Reward <3",
               JOptionPane.INFORMATION_MESSAGE
       );
   }
   public static void main(String[] args) {
    
       int drink = 0;
       int stickers = 0;
      
       Scanner scanner = new Scanner(System.in);
       JOptionPane.showMessageDialog(
               null,
               "Hello, welcome to Paw Cafe! <3",
               "Welcome Message",
               JOptionPane.INFORMATION_MESSAGE
       );
       do {
           String drinks = JOptionPane.showInputDialog(
                   null,
                   "What will be your order?" +
                           "\nCURRENT STICKERS: " + stickers
           );
           drink = Integer.parseInt(drinks);
           stickers = buyDrink(drink, stickers);
           checkStatus(stickers);
       } while (stickers <= 11);

       String choiceInput = JOptionPane.showInputDialog(
              null,
              "Choose your Reward:\n1. Cat Pen.\n2. Cat-Themed Notebook.\n3. -200 OFF Voucher.",
               "Cafe Rewards <3",
               JOptionPane.QUESTION_MESSAGE
       );
       rewardChoices(Integer.parseInt(choiceInput));

       JOptionPane.showMessageDialog(
                null, 
                "Thank you for visiting Paw’s Cafe. Come again!", 
                "Thank You Message",
                JOptionPane.INFORMATION_MESSAGE
        );


   }
}
