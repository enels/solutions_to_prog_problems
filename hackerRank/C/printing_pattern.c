#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    int count = n * 2 - 1;
    int mid = count / 2;
    int value, row, equal;
    
    for ( int i = 0; i < count; i++ ) {
        
        value = n - i;
        equal = 0; 
            
            for ( int j = 0; j < count; j++ ) {

		    if (i == 0 || j == 0 || i == count - 1 || j == count - 1)
			    printf("%i ", n);
		    else {
			    if (j >= i)
				printf("%i ", value);
		    }
		   

		    

	    }
	    printf("\n");

    }        

        
    return 0;
}
