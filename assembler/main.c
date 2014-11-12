#include<stdio.h>
#include<stdlib.h>


void main()
{
	int a=13;
	int b=-4;
	float f=0.1;
	int c=0;
	
	c = addNumbers(a,b);
	printf("Das Ergebnis ist: %i\n",c);

}

int addNumbers(int x, int y){
	return x+y;
}
