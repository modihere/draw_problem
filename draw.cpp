#include<iostream>
#include<vector>
#include<algorithm>


using namespace std;

void zerofunc(int pref[][300],int n,int p)
{

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(pref[i][j]==p)
				pref[i][j]=0;
		}
	}
}



int main()
{
	
	int pref[300][300];
	int random[300],room[300];
	int n,m,p,q,r;
	cout<<"enter the number of students"<<endl;
	cin>>n;
	
	for(int i=0;i<n;i++)
	{
		if((i+1)%10==1)
			cout<<endl<<"enter the preference of "<< i+1<<"st student"<<endl<<endl;
		else if((i+1)%10==2)
			cout<<endl<<"enter the preference of "<< i+1<<"nd student"<<endl<<endl;
		else if((i+1)%10==3)
			cout<<endl<<"enter the preference of "<< i+1<<"rd student"<<endl<<endl;
		else
			cout<<endl<<"enter the preference of "<< i+1<<"th student"<<endl<<endl;
		for(int j=0;j<n;j++)
		{
			cout<<"enter the preference number "<<j+1<<" -- ";
			cin>>pref[i][j];
		}
	}
	for(int i=0;i<n;i++)
		random[i]=i+1;
	random_shuffle(random, random+n);
	random_shuffle(random,random+rand()%n);

	cout<<endl;
	for(int i=0;i<n;i++)
		cout<<random[i]<<" ";
	cout<<endl;

	for(int k=1;k<=n;k++)
	{
		for(int i=0;i<n;i++)
		{
			if(k==random[i])
			{
				for(int j=0;j<n;j++)
				{
					if(pref[i][j]>0)
					{
						room[i]=pref[i][j];
						r=room[i];
						zerofunc(pref,n,r);
						break;
					}
				}
			}
		}
	}

for(int i=0;i<n;i++)
{
	cout<<"student "<<i+1<<" alloted room number :"<<room[i]<<endl;
}
return 0;
}
