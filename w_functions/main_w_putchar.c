#include <stdio.h>

// Declare the function from w_putchar.c
void w_ft_putchar(char c);

int main() {
	// Test the w_ft_putchar function    
    // Test letters
    w_ft_putchar('A');
    w_ft_putchar('B');
    w_ft_putchar('C');
    w_ft_putchar('\n');
    
    // Test digits
    w_ft_putchar('1');
    w_ft_putchar('2');
    w_ft_putchar('3');
    w_ft_putchar('\n');
    
    // Test special characters
    w_ft_putchar('!');
    w_ft_putchar('@');
    w_ft_putchar('#');
    w_ft_putchar('\n');
    
    // Test a longer string
    const char *str = "Hello, World!";
    while (*str) {
        w_ft_putchar(*str++);
    }
    w_ft_putchar('\n');

    return 0;
}