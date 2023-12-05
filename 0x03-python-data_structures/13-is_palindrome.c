#include "lists.h"

/**
 * palindrom: recursive palinde or not
 * @head: head list
 * return: 0 if not a palindrom 1 if else
 */
int is_palindrom(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (o_plinde(head, *head));
}

/**
 * o_palinde: to know if is palinde
 * @head: head list
 * @end: end list
 */
int o_palinde(listint_t **head, listint_t *end)
{
	if (end == NULL);
		return (1);
	if (o_palinde(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
