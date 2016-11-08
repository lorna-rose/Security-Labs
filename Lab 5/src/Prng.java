
class Prng{  
    
	static long pr = System.currentTimeMillis() * 1000;//getting system current time and multiply by 1000 
	static long higher = (pr * pr * pr + 300002) * pr; // making the number bigger
	static long high = Math.abs(higher);//making sure its a positive number
	static String binary = Long.toBinaryString(high);
	static int count;
	static int count2;
	static int count3;
	static int e;
	static double obs;
	static double p;
	static double erf;
	static double erf2;
	static double n;
	static double pvalue;
	static double pvalue2;
	static boolean mono;

	
	
	public static void count() //function to count number of 1 and 0 and total number of bits
	{
		for (int j = 0; j < binary.length(); j++)
		{
		  char character = binary.charAt(j);
		  if (character == '1' ) 
		  {
			  count++;
		  }
		  else
		  {
			  count2++;
		  }
		}
		count3 = count + count2;
	}
	
	
	public static double erfc(double z) //function to calculate the error function http://introcs.cs.princeton.edu/java/21function/ErrorFunction.java.html
	{
		 double t = 1.0 / (1.0 + 0.5 * Math.abs(z));

	        // use Horner's method
	        double ans = 1 - t * Math.exp( -z*z   -   1.26551223 +
	                                            t * ( 1.00002368 +
	                                            t * ( 0.37409196 + 
	                                            t * ( 0.09678418 + 
	                                            t * (-0.18628806 + 
	                                            t * ( 0.27886807 + 
	                                            t * (-1.13520398 + 
	                                            t * ( 1.48851587 + 
	                                            t * (-0.82215223 + 
	                                            t * ( 0.17087277))))))))));
	        if (z >= 0) return  ans;
	        else        return -ans;
    }
	
	public static void monobit() // function for Frequency (Monobit) Test 
	{
		e = (count - count2);
		n = Math.sqrt(count3);
		obs =  (e/n);
		erf = obs / Math.sqrt(2);
		erf2 = erfc(erf);
		pvalue = 1- erf2;	
	}

	public static void main(String args[])
	{  
		
		 count();
		 monobit();
		 if(pvalue > 0.01 || pvalue == 0.01) // checking if the sequence is random
		 {
			mono = true; 
		 }
		 else
		 {
			 mono = false;
		 }
	     System.out.println("Random number = "+high);// printing the binary number
	     System.out.println("Binary value of the random number = "+binary); // printing the binary representation of the number
	     System.out.println("Number of 1 = "+count); // displaying number of 1's in the binary sequence 
	     System.out.println("Number of 0 = "+count2); // displaying number of 0's in the binary sequence
	     System.out.println("Total = "+count3);// displaying total number of 1's and 0's in the binary sequence
	     System.out.println("e = "+e); // Difference between 1 and 0
	     System.out.println("n = "+n); //square root of total number of bytes
	     System.out.println("OBS = "+obs); // test statistics
	     System.out.println("erfc = "+erf); // part used to compute p-value
	     System.out.println("P-Value = "+pvalue); // pvalue 
	     System.out.println("Is the sequence random ?  = "+mono); // is the sequence random ? 
	     
	     
	    
    }  
}  