#include <stdio.h>

int main()
{
    // int n;
    // printf("This is a test file!\r\nInput a number: ");
    // scanf("%d", &n);
    // printf("The number is %d", n);
    // return 0;

    char web_url[] = "http://c.biancheng.net";
    char *web_name = "c语言中文网";
    puts(web_url);
    puts(web_name);
    printf("%s\n%s", web_url, web_name);
    return 0;
}