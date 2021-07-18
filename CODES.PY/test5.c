#include<stdio.h>
int arraycall(int *ar)
{
	for(int i=0;i<5;i++)
	{
		printf("%d",*ar);
		*ar +1;
	}
	
	return 1;
}
void main()
{
	int ar[5]={33,40,44,1,8};
	arraycall(ar);
}
