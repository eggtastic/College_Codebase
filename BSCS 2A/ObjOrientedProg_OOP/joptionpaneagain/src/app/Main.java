package app;
import javax.swing.JOptionPane;
import javax.swing.*;

import fruit.Fruit; // how i imported from another class

public class Main {
    public static void main(String[] args) {
        JOptionPane.showMessageDialog(null, // parentComponent
                "Welcome to the Fruit Shop!", // message
                "WELCOME SIGN...", // title
                JOptionPane.INFORMATION_MESSAGE
        );

        String fruit1 = JOptionPane.showInputDialog(
                null,
                "Enter preferred fruit #1: "
        );
        String fruit2 = JOptionPane.showInputDialog(
                null,
                "Enter preferred fruit #2: "
        );
        String fruit3 = JOptionPane.showInputDialog(
                null,
                "Enter preferred fruit #3: "
        );

        Fruit fruit_1 = new Fruit(fruit1, 50, 2);
        Fruit fruit_2 = new Fruit(fruit2, 20, 1);
        Fruit fruit_3 = new Fruit(fruit3, 30, 3);

        JOptionPane.showMessageDialog(
                null,
                "Alright, pard'ner, they're in stock! Take your pick: \n" + "1. " +fruit_1.getName().toUpperCase()+ " - "+fruit_1.getPrice()+" - "+fruit_1.getStock(),
                "FRUIT SHOP!",
                JOptionPane.INFORMATION_MESSAGE
        );
    }
}
