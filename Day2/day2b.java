import java.io.BufferedReader;
import java.io.FileReader;

class day2b {
    static int processGame(String line) {

        int gameNumber = Integer.parseInt(line.split(":")[0].split(" ")[1]);
        String[] splits = line.split(": ")[1].split("; ");
        int lg = -1;
        int lb = -1;
        int lr = -1;
        for (String game : splits) {
            int gr = 0;
            int gg = 0;
            int gb = 0;
            for (String pair : game.split(", ")) {
                String color = pair.split(" ")[1];
                int count = Integer.parseInt(pair.split(" ")[0]);
                if (color.equals("blue")){
                    gb += count;
                } else if (color.equals("green")) {
                    gg += count;
                } else {
                    gr += count;
                }
            }
            lg = Math.max(gg, lg);
            lr = Math.max(gr, lr);
            lb = Math.max(lb, gb);
            System.out.printf("%s\nLowest red:%d\nLowest green:%d\nLowest blue:%d\n", line, lr, lg, lb);
        }
        
            return lb * lr * lg;
        

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