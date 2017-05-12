Title: GCC: How To Suppress a Warning in a Single Line of Code
Category: General
Date: 2017-05-04 17:45
Modified: 2017-05-12 21:00
Slug: gcc-suppress-single-warning

TIL that GCC [allows][u1] to suppress a given type of warnings in a single line of
code. Here is an example:

```cpp
InMemoryStorage::InMemoryStorage() {
    if(pthread_rwlock_init(&_rwlock, NULL) != 0)
        throw std::runtime_error("pthread_rwlock_init() failed");
}

InMemoryStorage::~InMemoryStorage() {
    if(pthread_rwlock_destroy(&_rwlock) != 0) {
        // suppress 'throw will always call terminate() [-Wterminate]'
        #pragma GCC diagnostic push
        #pragma GCC diagnostic ignored "-Wterminate"
        throw std::runtime_error("pthread_rwlock_destroy() failed");
        #pragma GCC diagnostic pop
    }   
}
```

I think that using this feature was justified in this specific case. Thank you,
GCC, for warning me that throwing an exception in a destructor will cause a
program to terminate. However, it still looks like something I want. If
`pthread_rwlock_destroy` fails, it means that something is most likely to be
very wrong (memory corruption or something like this).

[u1]: https://gcc.gnu.org/onlinedocs/gcc/Diagnostic-Pragmas.html
