char	*ft_strcpy(char *s1, char *s2);

int main()
{
	char s1[100] = "Hello";
	char s2[100] = "World";
	ft_strcpy(s1, s2);
	printf("%s\n", s1);
}