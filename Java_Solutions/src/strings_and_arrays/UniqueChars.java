package strings_and_arrays;
import java.util.Arrays;

public class UniqueChars {

	public static void main(String[] args) {
		
		System.out.println(checkUni("Ronan"));
		System.out.println(checkUni("abcd"));
		System.out.println(checkUni("abcdd"));
	}
	
	public static boolean checkUni (String s) {
		
		if(s.length() > 128)
			return false;
		
		Boolean [] charsSeen = new Boolean [128];
		
		for(int i = 0; i < s.length(); i++) {
			
			int index = s.charAt(i);
			
			if (charsSeen[index] != null) {
				return false;
			}
			
			charsSeen[index] = true;
		}
		
		return true;
	}

}
