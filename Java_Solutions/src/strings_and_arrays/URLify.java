package strings_and_arrays;

public class URLify {
	
	public static void main(String [] args) {
		
		urlify("Ronan Byrne");
		urlify("Ronan Byrne ");
		
	}
	
	public static String urlify(String s) {
		
		int whiteSpaceCount = 0;
		
		for (int i = 0; i < s.length(); i++) {
			if(s.charAt(i) == ' ')
				whiteSpaceCount += 3;
		}
		
		char [] changedCharList = new char [whiteSpaceCount + s.length()];
		
		int index = 0;
		for (int i = 0; i < s.length(); i++) {
			
			if (s.charAt(i) != ' ') {
				changedCharList[index] = s.charAt(i);
				index ++;
			} else {
				changedCharList[index] = '%';
				changedCharList[index+1] = '2';
				changedCharList[index+2] = '0';
				index = index +3;
			}	
				
		}
		
		String URL = new String(changedCharList);
		
		System.out.println(URL);
		
		return URL;
	}
	

}

