#include "lists.h"

/**
 * reverse - Reverses a linked list
 * @head: Singly linked list
 */
listint_t * reverse(listint_t *head)
{
	listint_t *new = NULL, *next;

	while (head)
	{
		next = head->next;
		head->next = new;
		new = head;
		head = next;
	}
	return (new);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Singly linked list
 * Return: 0 if it is not a palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *first_half, *second_half;

	if (head == NULL)
		return (1);
	slow = *head;
	fast = *head;

	while (fast->next && fast->next->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	second_half = reverse(slow->next);
	first_half = *head;

	while (first_half && second_half)
	{
		if (first_half->n != second_half->n)
			return (0);
		second_half = second_half->next;
		first_half = first_half->next;
	}
	return (1);
}
