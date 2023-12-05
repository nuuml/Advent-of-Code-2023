import java.io.BufferedReader;
import java.io.FileReader;

class day2a {
    static int processGame(String line) {
        int mr = 12;
        int mg = 13;
        int mb = 14;
        int gameNumber = Integer.parseInt(line.split(":")[0].split(" ")[1]);
        boolean possible = true;
        String[] splits = line.split(": ")[1].split("; ");
        for (String game : splits) {
            int gr = 0;
            int gg = 0;
            int gb = 0;
            for (String pair : game.split(", ")) {
                System.out.println(pair);
                String color = pair.split(" ")[1];
                System.out.println(pair.split(" ")[1]);
                int count = Integer.parseInt(pair.split(" ")[0]);
                if (color.equals("blue")){
                    gb += count;
                } else if (color.equals("green")) {
                    gg += count;
                } else {
                    gr += count;
                }
            }
            System.out.printf("%d Red, %d Green, %d Blue \n", gr, gg, gb);
            if ((gg> mg) || (gr > mr) || (gb > mb)) {
                possible = false;
            }
        }
        if (possible) {
            // System.out.println("Possible");
            return gameNumber;
        }
                System.out.println(line);

                    System.out.println("Impossible");

        return 0;
    }


    public static void main(String[] args) throws Exception{
        int red = 12;
        int green = 13;
        int blue = 14;
        int sum = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("day2.txt"))) {
            for (String line; (line = br.readLine()) != null;) {
                sum += processGame(line);
                System.out.println(sum);
            }
        }
    }

}