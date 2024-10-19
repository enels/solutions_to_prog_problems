#include <stdio.h>


int main(void)
{
	void miniMaxSum(int, int*);

	int arr[] = {256741038, 623958417, 467905213, 714532089, 938071625};

	miniMaxSum(5, arr);
}

void miniMaxSum(int arr_count, int* arr) {

	unsigned long long min = 0, max = 0;
    	unsigned long long tmp;

    unsigned long long sum[arr_count];

    // initialize the sum array to zeros
    for (int i = 0; i < arr_count; i++) {

        sum[i] = 0;
    }

    for (int i = 0; i < arr_count; i++) {

        for (int j = 0; j < arr_count; j++) {

            if (j == i)
                ;
            else {
                sum[i] += arr[j];
            }
        }
    }

    // sort the array, sum
    for (int i = 0; i < arr_count - 1; i++) {

        for (int j = i+1; j < arr_count; j++) {
            if (sum[i] > sum[j]) {
                tmp = sum[i];
                sum[i] = sum[j];
                sum[j] = tmp;
            }
        }
    }

    min = sum[0];
    max = sum[arr_count - 1];

    printf("%llu %llu\n", min, max);
}
