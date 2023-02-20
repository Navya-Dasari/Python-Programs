#include<stdio.h>
void main()
{
	int i,n,h,ele;
	scanf("%d",&n);
	i=1;
	h=0;
	while(i<=n)
	{
		scanf("%d",&ele);
		if(i==1)h=ele;
		if(ele<h)
		h=ele;
		i++;
	}
	printf("\nLowest %d",h);
}
