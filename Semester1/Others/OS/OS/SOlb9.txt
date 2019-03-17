#include <stdio.h>
#include <pthread.h>
#define MAX_NUM 100;

void*f(void*a)
{
	int k=*(int*)a;
	printf("Eu sunt thread-ul %d\n",k);
}

int main()
{
	pthread_t t[MAX_NUM];
	int i;
	for (i=0;i<MAX_NUM,i++)
	{
		pthread_create(&t[i],NULL,f,&i);	
	}
	for (i=0;i<MAX_NUM,i++)
	{
		pthread_join(&t[i],NULL); //asteapta terminarea 					  tuturor thread-urilor
	}
	return 0;
}