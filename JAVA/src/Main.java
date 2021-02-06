import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static boolean premierPart1(int n) {

        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;

    }

    public static boolean premierPart2(int n) {

        for (int i = 2; i < (n / 2); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;

    }

    public static boolean premierPart3(int n) {

        for (int i = 2; i < Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;

    }

    public static void main(String[] arg) throws IOException {

        List<Integer> numbers = new ArrayList(Arrays.asList(1000003, 2000003, 4000037, 8000009, 16000057, 32000011, 64000031, 128000003, 256000001, 512000009, 1024000009, 2048000011));


        long startTime;
        long endTime;
        long durationPart1;
        long durationPart2;
        long durationPart3;
        boolean isPrime;

        FileWriter csvWriter = new FileWriter("JAVA_TP2.csv");
        csvWriter.append("nb");
        csvWriter.append(",");
        csvWriter.append("is_prime");
        csvWriter.append(",");
        csvWriter.append("T_part1");
        csvWriter.append(",");
        csvWriter.append("T_part2");
        csvWriter.append(",");
        csvWriter.append("T_part3");
        csvWriter.append("\n");

        for (Integer num : numbers) {

            startTime = System.nanoTime( );
            isPrime = premierPart1(num);
            endTime = System.nanoTime( );
            durationPart1 = (endTime - startTime);

            startTime = System.nanoTime( );
            isPrime = premierPart2(num);
            endTime = System.nanoTime( );
            durationPart2 = (endTime - startTime);

            startTime = System.nanoTime( );
            isPrime = premierPart3(num);
            endTime = System.nanoTime( );
            durationPart3 = (endTime - startTime);

            System.out.println(num.toString( ) + " " + durationPart1 + " " + durationPart2 + " " + durationPart3);

            csvWriter.append(num.toString( ));
            csvWriter.append(",");
            csvWriter.append(Boolean.toString(isPrime));
            csvWriter.append(",");
            csvWriter.append(Long.toString(durationPart1));
            csvWriter.append(",");
            csvWriter.append(Long.toString(durationPart2));
            csvWriter.append(",");
            csvWriter.append(Long.toString(durationPart3));
            csvWriter.append("\n");
        }

        csvWriter.flush( );
        csvWriter.close( );
    }
}
