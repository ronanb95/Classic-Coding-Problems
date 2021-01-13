package strings_and_arrays;

public class PermutationsV2 {

	public static void main(String[] args) {
		
		System.out.println(checkPermu("god", "dog"));
		System.out.println(checkPermu(" god", "dog"));
		System.out.println(checkPermu("nanor", "ronan"));

	}
	
	public static Boolean checkPermu(String s1, String s2) {
		
		if(s1.length() != s2.length())
			return false;
		
		int s1Count = 0;
		int s2Count = 0;
		
		for(int i = 0; i < s1.length(); i++) {
			int s1Value = s1.charAt(i);
			int s2Value = s2.charAt(i);
			s1Count += s1Value;
			s2Count += s2Value;
		}
		
		return (s1Count == s2Count);
	}

}
