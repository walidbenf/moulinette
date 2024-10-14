#include <unistd.h>

void w_ft_print_reverse_alphabet(void)
{
	char c = 'z';
	while (c >= 'a')
	{
		write(1, &c, 1);
		c--;
	}
	write(1, "\n", 1);
}