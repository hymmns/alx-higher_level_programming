#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head node
 * @number: number value
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));

	if (node == NULL)
	{
		return (NULL);
	}

	node->n = number;
	node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		node->next = *head;
		*head = node;

		return (node);
	}

	listint_t *current = *head;

	while (current->next != NULL && current->next->n <= number)
	{
		current = current->next;
	}

	node->next = current->next;
	current->next = node;

	return (node);
}
