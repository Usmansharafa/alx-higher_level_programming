#include "lists.h"

/**
 * insert_node - Inserts a node in a sorted linked list
 * @head: Pointer to linked list
 * @number: Number element of node
 * Return: Pointer to new node or NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
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
	if (number < node->n)
	{
		*head = new;
		new->next = node;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;
	
	return (new);
}
