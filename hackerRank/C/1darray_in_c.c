#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, sum = 0;
    
    scanf("%d", &n);
    //scanf("\n");
    
    int *arr;
    if ( (arr = (int *)malloc(n * sizeof(int))) == NULL ) {
        printf("Error allocating memory");
    }
    
    int *arr2 = arr;
    
    for (int i = 0; i < n; i++) {
        
        scanf("%d", &arr[i]);
        //scanf("\n");
        //arr++;
        //marr = (int *)malloc(n * sizeof(int));
        
        
    }
    
    arr = arr2;
    for (int i = 0; i < n; i++) {
        
        sum += arr[i];
    }
    
    free(arr);
    
    printf("%i\n", sum);
    
    return 0;
}

