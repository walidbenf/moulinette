int		ft_strlen(char *str)
{
	int i = 0;
	while (str[i] != '\0')
		++i;
	return (i);
}

char	*ft_strrev(char *str)
{
	int left = 0;
	int right = ft_strlen(str) - 1;
	char swap;

	while (left < right)
	{
		swap = str[left];
		str[left] = str[right];
		str[right] = swap;
		++left;
		--right;
	}
	return (str);
}