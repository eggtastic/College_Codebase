package fruitvendor;
import fruit.Fruit;
import java.util.ArrayList;

public class FruitVendor {
    private String vendorName;
    private double earnings;
    public ArrayList<Fruit> inventory = new ArrayList<>();

    public FruitVendor(String vendorName, double earnings) {
        this.vendorName = vendorName;
        this.earnings = earnings;
    }

    public String getVendorName() {
        return vendorName;
    }

    public double getEarnings() {
        return earnings;
    }

    public void addFruit(Fruit fruit) {
        inventory.add(fruit);
    }
    public Fruit findFruit(String fname) {
        for (Fruit f : inventory){
            if(f.getName().equalsIgnoreCase(fname)) {
               return f;
            }
        }
        return null;
    }

    public String sellFruit (String fruit, int qty, double price, double change) {
        Fruit f = findFruit(fruit);
        if (f == null) {
            return "Sorry! "+fruit+" is out of stock!";
        }

        if (qty<=0) {
            return "Please choose a fruit we have QTY. of.";
        }

        if (qty > f.getStock()) {
            return "Sorry! We don't have enough of that stocked for " + fruit;
        }

        f.setStock(f.getStock() - qty);
        double totalPrice = qty * f.getPrice();
        earnings += totalPrice;

        return String.format("Sold %-10s " +fruit+"QTY (%d pcs)" + totalPrice +" %.2f");
    }
}
