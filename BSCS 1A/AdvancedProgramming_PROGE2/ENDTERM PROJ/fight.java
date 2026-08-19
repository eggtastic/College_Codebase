import javax.swing.*;
import java.util.Scanner;
import java.util.Random;

public class fight {
    boolean isnormal = false;
    int spatk_chosen = 0;

    static void failSP () {
        JOptionPane.showMessageDialog(
                null, // parentComponent
                "Not enough SP POINTS! You GUARD instead...", // message
                "SP DEFICIENCY", // title
                JOptionPane.PLAIN_MESSAGE
        );
    }

   static void showFight() {
    builder builder = new builder();
       shop shop = new shop();

       boolean encounter = true;
       boolean player_isguarding = false;
       boolean enemy_isguarding = false;
       int spattacked = 0;
       int player_HP = 20;
       int player_dmg = 0;
       int enemy_HP = 10;
       int enemy_dmg = 0;
       int sp_points = 3;
       String result = "";
       Scanner sc = new Scanner(System.in);


       // d20 generation: start
       Random random = new Random();
       int[] d20 = new int[20];


       for (int i = 0; i < d20.length; i++) {
           d20[i]=i;
       }
       // enemy RNG
       int[] enemy_RNG = new int[2];


       while (encounter) {
           int choice = Integer.parseInt(JOptionPane.showInputDialog(
                   null, // parentComponent
                   "1. Normal Attack!" + "\n2. Special Attack!" + "\n3. Guard!" + "\nWhat do you do!?: ",
                   "-- FIGHT --", // title
                   JOptionPane.INFORMATION_MESSAGE
           ));


           switch(choice){
               case 1:
                   System.out.println("\nChose: NORMAL ATK!");
                   int player_index = random.nextInt(d20.length);
                   System.out.println("Rolled: " + d20[player_index]);
                   if (d20[player_index] > 10) {
                       JOptionPane.showMessageDialog(
                               null, // parentComponent
                               "ROUGE: AUUUGH-!", // message
                               "Gracious Response: HIT!", // title
                               JOptionPane.INFORMATION_MESSAGE
                       );
                       result = "Passed!";
                       player_dmg = 4;
                   } else {
                       JOptionPane.showMessageDialog(
                               null, // parentComponent
                               "ROUGE: Haha! You're too slow!", // message
                               "Gracious Response: MISS!", // title
                               JOptionPane.INFORMATION_MESSAGE
                       );
                       result = "Missed!";
                       player_dmg = 0;
                   }
                   System.out.println("Result: " + result);
                   System.out.println("Damage: " + player_dmg);
                   break;


               case 2:
                   int spatk_choice = Integer.parseInt(JOptionPane.showInputDialog(
                           null, // parentComponent
                           "1. Hurricane Supremo! (SP: 2)" + "\n2. Linguistic Specularity! (SP: 3)" + "\n3. Throw Rock at You. (SP: 5)" + "\nChoose your special attack! ",
                           "-- Chose: SPECIAL ATK! --", // title
                           JOptionPane.INFORMATION_MESSAGE
                   ));


                   switch (spatk_choice){
                       case 1:
                        if (sp_points > 2) {
                            sp_points -= 2;
                            JOptionPane.showMessageDialog(
                                   null, // parentComponent
                                   "ROUGE looks very, very intimidated suddenly."
                                   + "\nROUGE: W-Wait, hold on--", // message
                                   "HURRICANE SUPREMO Chosen!", // title
                                   JOptionPane.PLAIN_MESSAGE
                           );
                           int spatk_index1 = random.nextInt(d20.length);
                           System.out.println("Rolled: " + d20[spatk_index1]);
                           if (d20[spatk_index1] > 5) {
                            result = "CRITICAL HIT!";
                               player_dmg = 20;
                               System.out.println("ROUGE: x _ x");
                               encounter = false;
                           } else {
                               result = "Missed!";
                               System.out.println("ROUGE: ... What? Was that just a little wind?");
                               player_dmg = 0;
                           }
                        } else {
                            failSP();
                           player_isguarding = true;
                        }
                           break;
                       case 2:
                        if (sp_points > 3) {
                            sp_points -= 3;
                            JOptionPane.showMessageDialog(
                                   null, // parentComponent
                                   "ROUGE looks at you confused as you pull out a book.", // message
                                   "LINGUISTIC SPECULARITY Chosen!", // title
                                   JOptionPane.PLAIN_MESSAGE
                           );
                           int spatk_index2 = random.nextInt(d20.length);
                           System.out.println("Rolled: " + d20[spatk_index2]);
                           if (d20[spatk_index2] > 10) {
                            result = "CRITICAL HIT!";
                               System.out.println("ROUGE: Huh, what is that--");
                               player_dmg = 25;
                               System.out.println("ROUGE: x _ x");
                               encounter = false;
                           } else {
                               result = "Missed!";
                               System.out.println("ROUGE: ... What? Were you literally just reading?");
                               player_dmg = 0;
                           } 
                        } else {
                            failSP();
                           player_isguarding = true;
                        }
                           break;
                       case 3:
                        if (sp_points > 5) {
                           JOptionPane.showMessageDialog(
                                   null, // parentComponent
                                   "ROUGE is shaking like a leaf.", // message
                                   "THROW ROCK AT YOU Chosen!", // title
                                   JOptionPane.PLAIN_MESSAGE
                           );
                           int spatk_index3 = random.nextInt(d20.length);
                           System.out.println("Rolled: " + d20[spatk_index3]);
                           if (d20[spatk_index3] > 18) {
                            result = "CRITICAL HIT!";
                               System.out.println("ROUGE: W-Wait, hold on--");
                               player_dmg = 99;
                               System.out.println("ROUGE: x _ x");
                               encounter = false;
                           } else {
                               result = "Missed!";
                               System.out.println("ROUGE: ... What? Was that a pebble?");
                               player_dmg = 0;
                           }
                        } else {
                            failSP();
                           player_isguarding = true;
                        }
                           break;
                       default:
                           break;
                   }


                   break;
               case 3:
                   System.out.println("\nChose: GUARD!");
                   System.out.println("For the enemy's next attack, DMG is ignored!");
                   System.out.println("You gain +2 SP for guarding.");
                   sp_points += 2;
                   player_isguarding = true;
                   break;
               default:
                   System.out.println("INVALID INPUT! Try again!");
                   break;


           }


           // enemy reacts
           System.out.println("\nEnemy reacts!?\n");


           if (spattacked == 1) {
               JOptionPane.showMessageDialog(
                       null, // parentComponent
                       "ROUGE: Watch this!" + "\nThe enemy unleashes their SPECIAL ATK!", // message
                       "OH NO! SP ATK!", // title
                       JOptionPane.PLAIN_MESSAGE
               );
               enemy_dmg = 7;
               System.out.println("Damage: " + enemy_dmg);
               spattacked = 0;
           } else {
               int rng_index = random.nextInt(enemy_RNG.length);
               System.out.println("Rolled: " + enemy_RNG[rng_index]);


               if (rng_index == 0) {
                   System.out.println("ROUGE: Have at it, fool!");
                   System.out.println("\nEnemy chose NORMAL ATK!");


                   int enemy_index = random.nextInt(d20.length);
                   System.out.println("They Roll: " + d20[enemy_index]);
                   if (d20[enemy_index] > 10) {
                       result = "Passed!";
                       System.out.println("ROUGE: Huzzah!");
                       enemy_dmg = 5;
                   } else {
                       result = "Missed!";
                       System.out.println("ROUGE: ...Oops.");
                       enemy_dmg = 0;
                   }
                   System.out.println("Result: " + result);
                   System.out.println("Damage: " + enemy_dmg);
               } else {
                   System.out.println("\nEnemy chose SPECIAL ATK!");
                   if (spattacked == 0) {
                       JOptionPane.showMessageDialog(
                               null, // parentComponent
                               "ROUGE starts a SPECIAL ATK...! You might want to duck...", // message
                               "SP ATK in next turn...!", // title
                               JOptionPane.PLAIN_MESSAGE
                       );
                       spattacked += 1;
                   }
               }
           }




           // displaying results of encounter
           if (player_isguarding) {
               if (enemy_dmg > 0) {
                   System.out.println("\nYou were GUARDING! DMG ignored!");
                   enemy_dmg = 0;
                   player_isguarding = false;
               } else {
                   System.out.println("\nGUARDING! No DMG done though, so you just stood there...");
                   player_isguarding = false;
               }
           } else {
               enemy_HP -= player_dmg;
           }
           if (enemy_isguarding) {
               if (player_dmg > 0) {
                   System.out.println("\nBut enemy was GUARDING! DMG ignored...");
                   enemy_isguarding = false;
               } else {
                   System.out.println("\nGUARDING! No DMG done though, so enemy just stood there, lol...");
                   enemy_isguarding = false;
               }
           } else {
               player_HP -= enemy_dmg;
           }


           System.out.println("\nEnemy HP Left: " + enemy_HP);
           System.out.println("Player HP Left: " + player_HP);


           // win/lose condition
           if (player_HP <= 0) {
               encounter = false;
               JOptionPane.showMessageDialog(
                       null, // parentComponent
                       "ROUGE: Cope." + "\nDEFEATED. Try again!", // message
                       "OUTCOME MESSAGE", // title
                       JOptionPane.INFORMATION_MESSAGE
               );
           } else if (enemy_HP <= 0) {
               encounter = false;
               builder.Stat_Points += 10;
               JOptionPane.showMessageDialog(
                       null, // parentComponent
                       "ROUGE: I’ll see you down there in a bit"
               + "\nVICTORY. Well done! Gain +5 Coins and +10 Stat Points.", // message
              "OUTCOME MESSAGE", // title
              JOptionPane.INFORMATION_MESSAGE
      );
      shop.gold += 5;
  } else if (enemy_HP <= 0 && player_HP <= 0) {
      encounter = false;
      JOptionPane.showMessageDialog(
              null, // parentComponent
              "DRAW !!! Incredible!", // message
              "OUTCOME MESSAGE", // title
              JOptionPane.INFORMATION_MESSAGE
      );
  }
}


}
}




