import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int total_amount = Integer.parseInt(reader.readLine());
        int n = Integer.parseInt(reader.readLine());
        int cal_amount = 0;

        for(int i=0; i<n; i++) {
            String[] split = reader.readLine().split(" ");
            cal_amount += Integer.parseInt(split[0]) * Integer.parseInt(split[1]);
        }

        if(total_amount != cal_amount) {
            System.out.println("No");
        }
        else {
            System.out.println("Yes");
        }

    }
}
