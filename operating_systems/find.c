// includes

void usage()
{
}

void find(char *path, char *expression)
{
    // open the directory
    // read the directory
    // for each entry in the directory
    // if the entry is a directory
    // if the entry is a file
    // if the entry matches the expression
    // print the entry
    // close the directory
}

int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        usage();
        return 1;
    }
    find(argv[1], argv[2]);
    return 0;
}