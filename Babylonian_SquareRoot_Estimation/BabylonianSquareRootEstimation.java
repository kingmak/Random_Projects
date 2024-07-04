import java.lang.Math;
import java.util.Scanner;
import java.text.DecimalFormat;

public class BabylonianSqrtEstimate {
	
	public static void main(String[] args) {
		
		DecimalFormat Decimal = new DecimalFormat("#.0000000000");
		Scanner Input = new Scanner(System.in);
		double Guess, Num, Perfect, Old;		
		String OutString = "";
		int Count = 0;
		
		System.out.print("The Number to Square Root: ");
		Num = Double.parseDouble(Input.nextLine());		
		if (Num < 0) {
			System.out.println("Your Number Cannot be Less Then Zero");
			System.exit(-1);	
		}
		
		System.out.print("Initial Guess: ");
		Guess = Double.parseDouble(Input.nextLine());
		Old = Guess;
		if (Guess == 0) {
			System.out.println("Your Guess Cannot be Zero");
			System.exit(-1);
		}
		if (Guess < 0) {
			Guess = Math.abs(Guess);
		}
		
		Perfect = Math.sqrt(Num);
		while (Guess != Perfect) {
			Guess = ((Num / Guess) + Guess) / 2;
			Count += 1;
		}

		if (Old > 0) {
			OutString = "%nAccording to the Babylonians Sqrt(%s) = %s (%d cycles)";
		}
		if (Old < 0) {
			OutString = "%nAccording to the Babylonians Sqrt(%s) = -%s (%d cycles)";
		}
		System.out.printf(OutString, Decimal.format(Num), Decimal.format(Guess), Count);
		Input.close();
	}
}
