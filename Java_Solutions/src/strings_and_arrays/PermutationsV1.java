package strings_and_arrays;
import java.util.Arrays;

public class PermutationsV1 {
	
	public static void main(String [] args) {
		
		System.out.println(checkPermu("god", "dog"));
		System.out.println(checkPermu("ronan","onran"));
		System.out.println(checkPermu("ronan","onXan"));
		
	}
	
	public static Boolean checkPermu (String s1, String s2) {
		
		if(s1.length() != s2.length())
			return false;
		
		char ch1 []  = s1.toCharArray();
		char ch2 []  = s2.toCharArray();
		
		Arrays.sort(ch1);
		Arrays.sort(ch2);
		
		return (Arrays.equals(ch1,ch2));
	}

}


