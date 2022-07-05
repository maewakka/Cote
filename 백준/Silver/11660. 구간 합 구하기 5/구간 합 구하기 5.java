import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] firstLine = reader.readLine().split(" ");
        int N = Integer.parseInt(firstLine[0]);
        int M = Integer.parseInt(firstLine[1]);

        int[][] array = new int[N+1][N+1];
        int[][] sum_array = new int[N+1][N+1];
        int answer = 0;

        for(int i=1; i<N+1; i++) {
            String[] Line = reader.readLine().split(" ");
            for(int j=1; j<N+1; j++) {
                array[i][j] = Integer.parseInt(Line[j-1]);
            }
        }

        for(int x=1; x<N+1; x++) {
            for(int y=1; y<N+1; y++) {
                sum_array[x][y] = sum_array[x-1][y] + sum_array[x][y-1] - sum_array[x-1][y-1] + array[x][y];
            }
        }

        for(int i=0; i<M; i++) {
            String[] Line = reader.readLine().split(" ");
            int x1 = Integer.parseInt(Line[0]);
            int x2 = Integer.parseInt(Line[1]);
            int y1 = Integer.parseInt(Line[2]);
            int y2 = Integer.parseInt(Line[3]);

            answer = sum_array[y1][y2] - sum_array[y1][x2-1] - sum_array[x1-1][y2] + sum_array[x1-1][x2-1];
            writer.write(Integer.toString(answer));
            writer.newLine();
        }

        writer.flush();
        writer.close();

    }
}