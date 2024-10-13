#include <stdio.h>

// Declare the function from putchar.c
void ft_putchar(char c);

int main() {
	// Test the ft_putchar function    
    // Test letters
    ft_putchar('A');
    ft_putchar('B');
    ft_putchar('C');
    ft_putchar('\n');
    
    // Test digits
    ft_putchar('1');
    ft_putchar('2');
    ft_putchar('3');
    ft_putchar('\n');
    
    // Test special characters
    ft_putchar('!');
    ft_putchar('@');
    ft_putchar('#');
    ft_putchar('\n');
    
    // Test a longer string
    const char *str = "Hello, World!";
    while (*str) {
        ft_putchar(*str++);
    }
    ft_putchar('\n');

    return 0;
}