public class Main {
    public static void main(String[] args) {
       Laptop laptop1 = new Laptop();
       System.out.println("-- LAPTOP #1 --");
       laptop1.displaySpecs("Asus ROG Zephyrus", "AMD Ryzen", 16, "1TB");

       Laptop laptop2 = new Laptop();
       System.out.println("\n-- LAPTOP #2 --");
       laptop2.displaySpecs("HP Dragonfly Pro", "AMD Ryzen", 16, "512 GB");
   }

}
