#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if singly linked list is a cycle
 * Return: 0 if no cycle, 1 cycle found
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	if (!list)
		return (0);

	while (1)
	{
		/*traverse through nodes as long as linked list node exists*/
		if (ptr1->next != NULL && ptr1->next->next != NULL)
		{
			ptr1 = ptr1->next->next;
			ptr2 = ptr2->next;

			if (ptr1 == ptr2) /*if nodes match, cycle found*/
			return (1);
		}
		else
	        return (0);
	}

}
