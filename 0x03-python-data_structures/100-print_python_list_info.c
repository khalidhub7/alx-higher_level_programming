#include <python.h>
/**
 * print_python_list_info - print info about python list
 * @p: py object list
 */
void print_python_list_info(pyobject *p)
{
	int size, alloc, i;
	pyobject *obj;

	size = py_size(p);
	alloc = ((pylistobject*)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: =", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
