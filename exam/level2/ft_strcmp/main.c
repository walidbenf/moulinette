#include <stdio.h>
#include <string.h>

int ft_strcmp(const char *s1, const char *s2);

int		main(void)
{
	char a[] = "Apples!";
	char b[] = "Apples!";
	char c[] = "Apples!!";
	char d[] = "Appled!";

	printf("%d, %d\n", ft_strcmp(a, b), strcmp(a, b));
	printf("%d, %d\n", ft_strcmp(a, c), strcmp(a, c));
	printf("%d, %d\n", ft_strcmp(a, d), strcmp(a, d));
}