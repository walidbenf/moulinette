#include <stdio.h>

char *ft_strrev(char *str);

int	main(void)
{
	char str[] = "12345";
	printf("%s\n", str);
	printf("%s\n", ft_strrev(str));
}