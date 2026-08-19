public class firstact {
    static void displaySpecs(String brand, String processor,
        int RAM, String storage){
            System.out.println("BRAND: " + brand);
            System.out.println("PROCESSOR: " + processor);
            System.out.println("RAM: " + RAM);
            System.out.println("STORAGE: " + storage);
        }

    public static void main(String[] args) {
        System.out.println("-- LAPTOP #1 --");
        displaySpecs("Asus ROG Zephyrus", "AMD Ryzen", 16, "1TB");
        System.out.println("\n-- LAPTOP #2 --");
        displaySpecs("HP Dragonfly Pro", "AMD Ryzen", 16, "512 GB");
    }
}