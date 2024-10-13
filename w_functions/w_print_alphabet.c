#include <unistd.h>

void w_ft_print_alphabet(void)
{
	char c = 'a';
	while (c <= 'z')
	{
		write(1, &c, 1);
		c++;
	}
	write(1, "\n", 1);
}