#include "kernel/types.h"
#include "user/user.h"

int main()
{
    int p[2];
    char our_byte = 'P';

    pipe(p);
    int pid = fork();
    if (pid > 0)
    {
        write(p[1], &our_byte, 1);
        int my_pid = getpid();
        char recieved_byte;
        read(p[0], &recieved_byte, 1);
        printf("%d: received pong %c\n", my_pid, recieved_byte);
    }
    else
    {
        char the_byte;
        read(p[0], &the_byte, 1);
        int my_pid = getpid();
        printf("%d: received ping %c\n", my_pid, the_byte);
    }
}