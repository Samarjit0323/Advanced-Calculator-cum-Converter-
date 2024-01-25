#include <stdio.h>
int per(int n, int r) {
	int top=1,nr=1,i=1,j=(n-r);
	for (i=1;i<=n;i++){
		top*=i;
	}
	for (j=(n-r);j>=1;j--){
		nr*=j;
	}
	int p=top/nr;
	return p;
}
int combination(int n, int r) {
	int top=1,rbot=1,nr=1,i=1,j=(n-r),l=1;
	for (i=1;i<=n;i++){
		top*=i;
	}
	for (j=(n-r);j>=1;j--){
		nr*=j;
	}
	for (l=1;l<=r;l++){
		rbot*=l;
	}
	int c=top/(nr*rbot);
	return c;
}
int main () {
	int n,r;
	char ch;
	printf("Enter choice(P=Permutation, C=Combination):");
	scanf("%c",&ch);
	printf("Enter values of n & r:");
	scanf("%d,%d",&n,&r);
	if (n>r){
		if (ch=='P') {
			int perm=per(n,r);
			printf(" n P r: %d",perm);
		}
		if (ch=='C') {
			int comb=combination(n,r);
			printf(" n C r: %d",comb);
		}
	}
	else printf("Restart Program!");
	return 0;
}
