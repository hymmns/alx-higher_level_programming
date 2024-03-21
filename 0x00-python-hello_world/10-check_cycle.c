#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the node
 * 
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *marked, *current;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list;
	marked = current->next;

	while (current != NULL && marked->next != NULL && marked->next->next != NULL)
	{
		if (current == marked)
			return (1);

		current = current->next;
		marked = marked->next->next;
	}

	return (0);
}
