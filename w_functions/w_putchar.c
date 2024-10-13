#include <unistd.h>

void w_ft_putchar(char c)
{
	write(1, &c, 1);
}