package fruit;
import javax.swing.*;

public class Fruit {
    private String name;
    private double price;
    private int stock = 10;

    public Fruit(String name, double price, int stock) {
        this.name = name;
        this.price = price;
        this.stock = stock;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        if (stock < 0) {
            this.stock = 0;
            JOptionPane.showMessageDialog(null, // parentComponent
                    "ERROR: STOCK IS AT 0! Please restock.",
                    "STOCK ERROR!", // title
                    JOptionPane.ERROR_MESSAGE
            );
        } else {
            this.stock = stock;
        }
    }

    public String toString() {
        return String.format("%s-10 %.2f (%d pcs)", name, price, stock);
    }
}
