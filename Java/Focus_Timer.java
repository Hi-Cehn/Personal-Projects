import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

import javax.security.auth.callback.ConfirmationCallback;

public class Focus_Timer {
    public static String input;
    public static Boolean confirmFlag;
    public static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Would you like to start the focus timer?");
        System.out.println("Please enter Yes to start, or No to terminate the program.");
        input = scanner.nextLine();

        if (input.equals("No")) {
            System.exit(0);
        }

        confirmFlag = InputScanner(input);
        ConfirmLoop(confirmFlag);
    }
    
    public static boolean InputScanner (String input) {
        if (input.equals("Yes")) {
            return true;
        } else {
            return false;
        }
    }

    public static void ConfirmLoop (Boolean confirmFlag) {
        if (confirmFlag) {
            Focus();
        } else {
            System.out.println("Invalid input. Please try again.");
            System.out.println("Would you like to start the focus timer?");
            System.out.println("Please enter Yes to start, or No to terminate the program.");
            input = scanner.nextLine();

            if (input.equals("No")) {
                System.exit(0);
            }
            
            confirmFlag = InputScanner(input);
            ConfirmLoop(confirmFlag);
        }
    }

    public static void Focus () {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");

        LocalTime sWorkTime = LocalTime.now();
        System.out.println("Current time: " + sWorkTime.format(formatter));

        try {
            Thread.sleep(30000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        LocalTime eWorkTime = LocalTime.now();
        System.out.println("Current time: " + eWorkTime.format(formatter));
        System.out.println("It has been 30 seconds since you started this program.");
        System.out.println("Please go rest for 30 seconds before executing this program again.");

        try {
            Thread.sleep(30000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        LocalTime eRestTime = LocalTime.now();
        System.out.println("Current time: " + eRestTime.format(formatter));
        System.out.println("It has been 30 seconds since you started this program.");
    }
}
