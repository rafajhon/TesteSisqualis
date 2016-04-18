#include <iostream>
#include <string.h>
using namespace std;
char str[1000001];
void ProximoPalindrome()
{
 int x, y, flag, len;
 x = 0;
 len=strlen(str);
 y = strlen(str)-1;
 flag = len / 2;
 bool MaiorQueStr = false;
 while(x <= y)
 {
   if(str[x] < str[y])
   {
     str[y] = str[x];
     MaiorQueStr = false;
   }
   else if(str[x] > str[y])
   {
     str[y] = str[x];
     MaiorQueStr = true;
   }
    x++;
    y--;
   }
  if(MaiorQueStr)return;
  else if(str[flag]!='9')
  {
    str[flag]++;
    str[len - flag - 1] = str[flag];
    return;
   }
   flag = (len-1)/2;
   while(flag >= 0 && str[flag]=='9')
   {
     str[flag] = '0';
     str[len - flag - 1] = '0';
     flag--;
    }
   if(flag>=0)
   {
     str[flag]++;
     str[len - flag - 1] = str[flag];
     return;
   }
   else if(flag<0)
   {
      str[0]='1';
      str[len] = '1';
      str[len+1]='\0';
      return;
    }
}

int main()
{
  int t;
  cin>>t;
  for (int i = 0; i < t; i++)
  {
    cin>>str;
    ProximoPalindrome();
    cout<<str<<endl;
  }
  return 0;
}
