#include "lists.h"

/**
 * insert_node - Inserts a node in a sorted linked list
 * @head: Pointer to linked list
 * @number: Number element of node
 * Return: Pointer to new node or NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *before;
	listint_t *after;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!*head)
	{
		*head = new;
		return (new);
	}
	before = *head;
	after = *head;
	after = after->next;
	if (before->n > number && after->n > number)
	{
		new->next = before;
		return (new);
	}
	while (before && after && after->next)
	{
		if (before->n < number && after->n < number)
		{
			before = before->next;
			after = after->next;
		}
		else
		{
			before->next = new;
			new->next = after;
			break;
		}
	}
	return (new);
}
