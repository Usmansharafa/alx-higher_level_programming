#include "lists.h"

/*
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @head: Pointer to list to be checked
 * Return: 1 if there is a cycle, else 0
 */
int check_cycle(listint_t *head)
{
	listint_t *fast;
	listint_t *slow;

	if (head == NULL)
		return (0);
	fast = head->next;
	slow = head;
	while (fast && fast->next && slow)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}