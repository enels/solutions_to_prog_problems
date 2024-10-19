#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT 
*/
    int num_arr[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    
    char *input_str = (char *) malloc(1000 * sizeof(char));
    
    scanf("%s", input_str);
    
    int str_len = strlen(input_str);
    int digit;
    
    for ( int i = 0; i < str_len; i++ ) {
        
        if ( !isalpha(input_str[i]) ) {
            // convert the character integer to real integer
            digit = input_str[i] - '0';
            
            // increase the integer index in the array
            num_arr[digit]++;       
        }
    }
    
    // print out the number
    for ( int i = 0; i < 10; i++ ) {
        
        printf("%d ", num_arr[i]);
    }
    
    printf("\n");
    
    return 0;
}
