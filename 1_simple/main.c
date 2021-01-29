#include <stdio.h>
#include <string.h>


int main(int argc, char* argv[]){
	if (argc == 2){
		if(strcmp("Piotr_Kw1@tkowski", argv[1])){
			printf("Wrong password\n");
		}
		else{
			printf("ACCES GRANTED\n");
		}
	}
	else{
		printf("Usage:\n 1_simple <key>\n");
	}

	return 0;
}
