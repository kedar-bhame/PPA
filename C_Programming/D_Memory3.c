#include <stdio.h>
#include <stdlib.h>

#if defined(_WIN32)
    #include <malloc.h>
    #define GET_ALLOCATED_SIZE(ptr) _msize(ptr)
#elif defined(__linux__)
    #include <malloc.h>
    #define GET_ALLOCATED_SIZE(ptr) malloc_usable_size(ptr)
#elif defined(__APPLE__)
    #include <malloc/malloc.h>
    #define GET_ALLOCATED_SIZE(ptr) malloc_size(ptr)
#endif

int main() {
    int count = 4;
    int *p = (int *) malloc(count * sizeof(int)); // Request 40 bytes (10 * 4)

    if (p != NULL) {
        size_t actual_size = _msize(p);
        
        printf("Requested size : %zu bytes\n", count * sizeof(int));
        printf("Actual OS size : %zu bytes\n", actual_size);

        free(p);
    }
    return 0;
}