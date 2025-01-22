void	ft_swap(int *a, int *b);

int main() {
	int a = 5;
	int b = 10;
	ft_swap(&a,&b);
	printf("a: %d\nb: %d\n", a, b);
}