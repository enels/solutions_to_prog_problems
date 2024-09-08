#include <stdio.h>
#include <stdlib.h>

// program to reverse an array
int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }
    
    int *arr2 = (int *)malloc(num * sizeof(int));
    
    for (int i = 0; i < num; i++) {
        
        *(arr2 + num - i - 1) = *(arr + i);
    }
    
    arr = arr2;


    /* Write the logic to reverse the array. */

    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}

