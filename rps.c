
#include <stdio.h>

void	get_input(char *input)
{
	printf("Rock, Paper or Scissors?\n");
	if (scanf("%19s", input) != 1)
		input[0] = '\0';
}

int	ft_strcmp(const char *s1, const char *s2)
{
	int	i;

	i = 0;
	while (s1[i] != '\0' && s1[i] == s2[i])
		i++;
	return ((unsigned char)s1[i] - (unsigned char)s2[i]);
}

int	is_valid_input(const char *input)
{
	const char	*valid[3] = {"Rock", "Paper", "Scissors"};
	int			i;

	i = 0;
	while (i < 3)
	{
		if (ft_strcmp(input, valid[i]) == 0)
			return (1);
		i++;
	}
	return (0);
}

int	main(void)
{
	char	input[20];

	get_input(input);
	if (is_valid_input(input))
		printf("You picked %s\n", input);
	else
		printf("Invalid input.\n");
	return (0);
}
