#include <stdio.h>
#include <windows.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>
const int MAX_X=23;
const int MAX_Y=50;
const int MAX_food=50;
const int ESC=27;
const int SPACE=32;


typedef struct Lnode{
        int x;
        int y;
        struct Lnode *next;
}Lnode,*Linklist;

typedef struct{
        Linklist front;                                                      //snake.front为食物坐标，snake.front->next为蛇尾，单链表以snake.front为首建立
        Linklist rear;                                                          //snake.rear 为蛇头
        int length;                                                                 //蛇的身长
}Queue;


Queue snake;


void gotoxy(int x,int y)                                           //找坐标 
{
        COORD wei;
        wei.X=y;
        wei.Y=x;
        SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),wei);                //windows编程
}


void wall()                                                            //创建围墙 
{
        int i, j;
        for(i=0;i<=MAX_X;i++)
        {
                if(i==0||i==MAX_X)
                {
                        for(j=0;j<=MAX_Y;j++)
                        {
                                gotoxy(i,j);
                                putchar('+');
                        }
                }
                gotoxy(i,0);
                putchar('+');
                gotoxy(i,MAX_Y);
                putchar('+');
        }
}



void help_info()                                             //输出帮助信息 
{ 
        gotoxy(8,53);
        puts("按ESC键退出,空格键暂停:");
        gotoxy(10,53);
        puts("上,下,左,右:w,s,a,d");
        gotoxy(12,53);
        puts("蛇越长,速度也会越快:");
        gotoxy(14,53);
        puts("如无法控制蛇,请关闭");
        gotoxy(15,53);
        puts("大写键盘锁定状态:");
}



void game_info()                                            //输出游戏信息 
{
        gotoxy(3,60);
        printf("当前蛇长度: %d",snake.length);
        gotoxy(5,60);
        printf(" ");
        gotoxy(5,60);
        printf("离胜利还差: %d",MAX_food-snake.length);
}



void enqueue(int x,int y)                                  //队列入队 ，不解释
{
        Linklist p;
        p=(Linklist)malloc(sizeof(Lnode));
        p->x=x;
        p->y=y;
        snake.rear->next=p;
        snake.rear=p;
        snake.rear->next=NULL;
        snake.length++;
}



void dequeue()                                         //队列出队 
{
        Linklist p=snake.front->next, q=snake.front;
        p->x=q->x;
        p->y=q->y;
        snake.front=p;
        free(q);
        snake.length--;
}



void init_snake()                                      //初始化蛇身 ，蛇在窗口左上角，起始长度为3
{
        snake.rear=snake.front=(Linklist)malloc(sizeof(Lnode));
        snake.rear->next=NULL;
        for(int i=0;i<3;i++)
        {
                enqueue(1,i+1);                                          //把(1,1) (1,2) (1,3)入队即蛇身
        }
        snake.length=3;
}



void show_food()                                         //随机出现食物 
{
        srand(time(NULL));
        Linklist p=snake.front->next, q=snake.front; 
        while(1)
        {
                q->x=rand()%(MAX_X-1)+1;
                q->y=rand()%(MAX_Y-1)+1;
                while(p)                                                         //把蛇身与食物重合的情况去掉
                {
                        if(p->x==q->x&&p->y==q->y) break;
                        p=p->next;
                }
                if(!p) break;
        }
        gotoxy(q->x,q->y);
        putchar('#');                                                    //在食物位置输出‘#’
}



void hua_snake(int i)                                     //画蛇 ，i==1输出蛇身，i==0输出蛇头
{
        Linklist p=snake.rear;
        gotoxy(p->x,p->y);
        if(i)
                putchar('*');
        else putchar('@');
}





void clear_wei()                                                         //删去蛇尾
{
        Linklist p=snake.front->next;
        gotoxy(p->x,p->y);
        putchar(' ');
        p=p->next;
        gotoxy(p->x,p->y);
        putchar('*');
}





int flag()                                                                           //判断是否撞墙或撞自己 
{
        if(snake.length>=MAX_food)
        {
                system("cls");
                gotoxy(10,20);
                puts("确定你没开WG？这么难的游戏你都赢了。。");       //你这么吊你家里人知道么
                Sleep(5000);
                exit(0);
        }
        Linklist p=snake.front->next, q=snake.rear;
        while(p!=q)                              //这里需要详解，判断蛇头与身体是否相撞，如果相撞break，输出 你输了的语句；如果没有和身体相撞最终p=q, 然后需要判断蛇是否与围墙相撞，若相撞，输出你输了，若没相撞，则这一步可以走，返回1
        {
                if(p->x==q->x&&p->y==q->y) break;
                p=p->next;
        }
        if(p==q)
        {
                if(p->x>=1&&p->x<MAX_X&&p->y>=1&&p->y<MAX_Y) return 1;
        }
        system("cls");
        gotoxy(10,30);
        puts("哈哈，你终于输了！！");
        Sleep(5000);
        exit(0);
}


void snake_auto_move(char tmp)      //蛇自己动 ，T-T比较麻烦,tmp是贪吃蛇方向
{
        int x, y;
        do{                                       //while(!kbhit()&&flag()) kbhit()函数，如果你在键盘上按某个键返回1，若不按键盘返回0也就是当你不按键盘而且向前走一步是可行的话那么就向前走
                clear_wei();                                                  //向前走的时候需要把蛇尾删掉
                hua_snake(1);                                    //再画蛇身的一节
                x=snake.rear->x;
                y=snake.rear->y;
                switch(tmp)                                          //前进
                {
                case 'w':x--;break;
                case 's':x++;break;
                case 'a':y--;break;
                case 'd':y++;break;
                }
                enqueue(x,y);                                             //把走的一步当作新的蛇头放入队列中
                if(x==snake.front->x&&y==snake.front->y)         //看是否吃到食物
                {
                        game_info(); 
                        show_food();                                                  //吃掉的话需要再出现一个食物
                }
                else dequeue();                                  //若没吃到食物，因为前面插入队列中一个新的蛇头，为保证蛇身长度不变，需要在尾部删去一节
                hua_snake(0);                                        //在新的蛇头蛇头坐标画一个新的
                int speed=-2*snake.length + 157;         //速度，由函数易知，蛇的长度越长speed越小，而Sleep(speed)即蛇休息时间越短从而实现蛇身越长，蛇前进的速度越快
                Sleep(speed);
        }while(!kbhit()&&flag());                           //每循环一次走一步从而实现蛇的动态移动
}





void snake_move()              //玩家控制方向或游戏功能 
{
        char c, c1=0;
        static char temp=0;
        if(!temp)                                //蛇在初始化的时候是向右方向前进的
        {
                temp='d';
                snake_auto_move(temp); 
        }
        while(1)
        {
                c=getch();
                if(c==ESC)                                   //若按ESC则关闭游戏
                {
                        system("cls");
                        gotoxy(10,30); 
                        puts("游戏退出成功!");
                        exit(0);
                }
                if(c1==SPACE)                         //c是当前按的键，c1是前一次按的键，如果c1=SPACE即空格键暂停，这次按的键C还是SPACE则游戏继续
                {
                        if(c==SPACE)
                        {
                                c1=0;
                                gotoxy(6,20);
                                printf("            ");
                                snake_auto_move(temp);
                        }
                        continue;
                }
                if(c==SPACE)                               //如果C=SPACE而C1!=SPACE即暂停
                {
                        c1=SPACE;
                        gotoxy(6,20);
                        printf("暂停中。。。");
                        continue; 
                }
                if(c=='s'||c=='w'||c=='a'||c=='d')    //如果这次按的键C与前一次蛇前进的方向temp相反，则忽略这次按键行为，蛇继续朝着temp前进
                {
                        if(c=='s'&&temp=='w'||c=='w'&&temp=='s'||c=='a'&&temp=='d'||c=='d'&&temp=='a')
                        {
                                snake_auto_move(temp);
                                continue;
                        }
                }
                break;
        }
        temp=c;                                                                //改变方向
        snake_auto_move(temp);
}





int main()                                                    //main
{
        system("title 贪吃蛇");
        system("mode con cols=77 lines=25");
        system("color");
        system("color FC");
        help_info();
        wall();
        init_snake();
        show_food();
        
        game_info();
        while(flag()){
                snake_move();
        }
        system("pause");
        return 0;
}
