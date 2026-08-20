import java.util.Random;

public class MultiDimensional_Arrays {
    public static void main(String[] args) {
        Random rand = new Random();

        int[][] array2 = {{0, 2, 1},{3, 4, 5}};

        System.out.println(array2[0][2]);

        ///////////////////////////////////////////

        int[][][] array3 = 
        {
            {
                {6, 8, 9},
                {0, 2, 1}
            },

            {
                {3, 4, 5},
                {10, 20, 30}
            }
        };

        System.out.println(array3[1][0][2]);

        ///////////////////////////////////////////

        int[][][][] array4 = 
        {
            {
                {
                    {6, 8, 9},
                    {0, 2, 1}
                },
                {
                    {3, 4, 5},
                    {10, 20, 30}
                }
            },
            {
                {
                    {23, 18, 91},
                    {15, 21, 11}
                },
                {
                    {31, 454, 45},
                    {111, 21, 40}
                }
            }
        };

        System.out.println(array4[1][1][1][0]); // output 111
        System.out.println(array4[1][0][0][1]); // output 18

        // int d1 = rand.nextInt(array4.length);
        // int d2 = rand.nextInt(array4[d1].length);
        // int d3 = rand.nextInt(array4[d2].length);
        // int d4 = rand.nextInt(array4[d3].length);

        // System.out.println("OUTPUT:"+ d1+" "+ d2+" "+ d3 +" "+ d4);
        // System.out.println(array4[d1][d2][d3][d4]);

        // do {
        //     System.out.println(array4[d1][d2][d3][d4]);
        // } while (array4.length <= 0);
        
        for (int i = 1; i <= 4; i++){
            int d1 = rand.nextInt(array4.length);
            int d2 = rand.nextInt(array4[d1].length);
            int d3 = rand.nextInt(array4[d2].length);
            int d4 = rand.nextInt(array4[d3].length);

            System.out.print(array4[d1][d2][d3][d4] + " ");
        }
    }

}
