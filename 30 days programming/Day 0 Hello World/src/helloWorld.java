import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
/**
 * @author maimansham
 * In this challenge, we review some basic concepts that will 
 * get you started with this series. You will need to use the 
 * same (or similar) syntax to read input and write output in
 * challenges throughout HackerRank. Check out the Tutorial tab
 * for learning materials and an instructional video! 
 *
 */
public class helloWorld {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// Create a Scanner object to read input from stdin.
		Scanner scan = new Scanner(System.in); 
				
		// Read a full line of input from stdin and save it to our variable, inputString.
		String inputString = scan.nextLine(); 

		// Close the scanner object, because we've finished reading 
		// all of the input from stdin needed for this challenge.
		scan.close(); 
		      
		// Print a string literal saying "Hello, World." to stdout.
		System.out.println("Hello, World.");
		      
		// TODO: Write a line of code here that prints the contents of inputString to stdout.
		System.out.println(inputString);

	}

}
