#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>
// #include "b.h"
// #include "b.h"

#define MESSAGE

int average(int, ...);
void reverseSentence();

void readFile(FILE *fp)
{
    fp = fopen("file.txt", "r");
    int ch;
    while (1)
    {
        ch = fgetc(fp);
        if(feof(fp))
        {
            break;
        }
        printf("%c", ch);
    }
}

static char a = 'a';
static char a1 = 'a';
extern char cccc;

int main(int argc, char *argv[])
{
    // int n;
    // printf("This is a test file!\r\nInput a number: ");
    // scanf("%d", &n);
    // printf("The number is %d", n);
    // return 0;

    // char web_url[] = "http://c.biancheng.net";
    // char *web_name = "c语言中文网";
    // puts(web_url);
    // puts(web_name);
    // printf("%s\n%s", web_url, web_name);

    // printf("Average of 2,3,4 = %d\n", average(3,2,3,4));
    // printf("Average of 5,10,15 = %d\n", average(3,5,10,15));

    // char name[100];
    // char *description;
    // strcpy(name, "Zara Ali");
    // description = (char *)malloc(30 * sizeof(char));
    // if(description == NULL)
    // {
    //     puts("error");
    // }
    // else
    // {
    //     strcpy(description, "Zara ali a DPS student.");
    // }
    // description = (char *)realloc(description, 100 * sizeof(char));
    // if(description == NULL)
    // {
    //     puts("error");
    // }else
    // {
    //     strcat(description, "She is in class 10th");
    // }
    // printf("name = %s\n", name);
    // printf("description:%s\n", description);
    // free(description);

    // char *argv[2] = {"chen", "wang"};
    // puts(argv[0]);
    // puts(argv[1]);

    // int argv[2] = {1,2};
    // printf("%d\n", argv[0]);
    // printf("%d\n", argv[1]);

    // printf("Program name %s\n", argv[0]);
    // if(argc == 2){
    //     printf("The argument supplied is %s\n", argv[1]);
    // }else if (argc > 2)
    // {
    //     printf("Too many arguments supplied.\n");
    // }else
    // {
    //     printf("One argument expected.\n");
    // }      

    // reverseSentence();
    // int *p = NULL;
    // size_t sd = sizeof(12);
    // printf("%d", sizeof(sd));

    // char *p = "hello world";
    
    // p[2] = 'A';
    // a[2] = 'A';

    // char *p1 = "hello world";
    // printf("%p\n", p);
    // printf("%p", p1);
    // printf("%p\n", &a);
    // printf("%p", &a1);

    // putc(cccc, stdout);
    // int *arr = (int *)allocf();
    // arr[1] = 12;
    // for (int i = 0; i < 4; i++)
    // {
    //     printf("%d\t", arr[i]);
    // }
    // free(arr);

    // float val;
    // char str[20];
    // printf("%#x\n", &"998");
    // printf("%#x\n", &"998");
    // strcpy(str, "98993489");
    // val = atof(str);
    // printf("%s::%f\n", str, val);
    // printf("%#x\n", str);

    // char *ptr = "ww12356";
    // printf("%s", ptr);

    // char str[30] = "20.30300 this is test";
    // char *ptr;
    // double ret;
    // ret = strtod(str, &ptr);
    // printf("%f\t|%s|", ret, ptr);

    // printf("%s", B "hello");

    // FILE *fp;
    // int c;
    // fp = fopen("test.txt", "r");
    // if(fp == NULL)
    // {
    //     perror("open file error");
    //     return(-1);
    // }
    // while (1)
    // {
    //     c = fgetc(fp);
    //     if(feof(fp))
    //     {
    //         break;
    //     }
    //     printf("%c", c);
    // }
    // fclose(fp);

    // char buff[1024];
    // memset(buff, '\0', sizeof(buff));
    // fprintf(stdout, "启用全缓冲\n");
    // setvbuf(stdout, buff, _IOFBF, 1024);
    // fprintf(stdout, "这里是runoob.com\n");
    // fprintf(stdout, "该输出将保存到buff\n");
    // fflush(stdout);
    // fprintf(stdout, "这将在编程时出现\n");
    // fprintf(stdout, "最后休眠\n");
    // Sleep(5000);
    // fflush(stdout);

    // FILE *fp;
    // fpos_t position;

    // fp = fopen("test.txt", "a+");
    // fgetpos(fp, &position);
    // fputs("hello, world!", fp);
    // fsetpos(fp, &position);
    // fputs("this is new info!", fp);
    // fclose(fp);

    // FILE *fp;
    // fp = fopen("file.txt", "w+");
    // fputs("This is runoob.com", fp);
    // fseek(fp, 0, SEEK_SET);
    // fputs("cccccccccccccccccc", fp);
    // fclose(fp);

    // FILE *fp;
    // int len;
    // fp = fopen("file.txt", "r");
    // if(fp == NULL)
    // {
    //     perror("open file error");
    //     return -1;
    // }
    // fseek(fp, 0, SEEK_END);
    // len = ftell(fp);
    // fclose(fp);
    // printf("%d", len);

    // int ret;
    // ret = rename("file.txt", "newfile.txt");
    // printf("%d", ret);

    // FILE *fp;
    // int len;
    // char arr[] = "this is runoob.com";
    // fp = fopen("file.txt", "w");
    // len = fwrite(arr, sizeof(arr), 2, fp);
    // fclose(fp);
    // printf("%d", len);

    // int ret;
    // ret = remove("file.txt");
    // printf("%d", ret);

    // char str[] = "This is runoob.com";
    // FILE *fp;
    // int ch;
    // fp = fopen("file.txt", "w");
    // fputs(str, fp);
    // fclose(fp);
    // readFile(fp);
    // rewind(fp);
    // printf("\n");
    // readFile(fp);
    // fclose(fp);

    char buf[BUFSIZ];

    setbuf(stdout, buf);
    puts("This is runoob");
    Sleep(2000);
    fflush(stdout);

    return 0;
}

int average(int n, ...)
{
    va_list valist;
    int sum = 0;
    int i;
    va_start(valist, n);
    for (i = 0; i < n; i++)
    {
        sum += va_arg(valist, int);
    }
    va_end(valist);
    return sum/n;
}

void reverseSentence()
{
    char c;
    scanf("%c", &c);

    if(c != '\n')
    {
        reverseSentence();
        printf("%c", c);
    }
    
}