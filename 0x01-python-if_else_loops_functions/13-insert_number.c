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

	if (!head || !*head)
		return (NULL);
	before = *head;
	after = *head;
	after = after->next;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
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
