#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>

char *strdup_every_other_char(const char *s)
{
    //  Takes a string and returns a string allocated on the heap
    // containing every other letter from the input string

    // count how many 'every other' there are by iteration 
	// null terminated means '\0' marks end of string ( i.e bit pattern all 0's)
    int eo = 0;
	for (int i=0 ; '\0' != s[i]; i++)
	{
		if (i%2 == 0)
        {
            eo++;
        }
	}

	// allocate memory for new string of length eo plus one for delimiter '\0'
	eo++;
	char* res = (char *)malloc(eo * sizeof(char));

	// fill the allocated memory res by incrementing pos of its index
    int pos = 0;
	for(int j=0; '\0' != s[j]; j++)
	{
        // match the values
		if (j%2 == 0)
		{
			res[pos] = s[j];
			pos++;
		}
	}
    // make it null terminated
	res[pos] = '\0';
	return res;
}

int main()
{
	char str[] = "1y2u3i4h5b6l7r6";
    printf("New String is %s\n",strdup_every_other_char(str));
    return 0;
}