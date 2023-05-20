#include<iostream>
#include<string>
#include<conio.h>
using namespace std;

class result
{
private:
    char fn[20],mn[20],ln[20];
    int rollno,gr,ssm[10],tm=0,ps=0,fs=0,sg[10];
    float p=0;

public:
    void getinfo(int sn,string s[10]);
    float calcinfo(int sn,int atm);
    float gcalcinfo();
    void printinfo(int sn,string s[10],int atm,int sm[10]);
};

void result::getinfo(int sn,string s[10])
{
    int i;

    cout<<"Enter first name of the student:"<<endl;     //Getting student's info
    cin>>fn;
    cout<<"Enter middle name of the student:"<<endl;
    cin>>mn;
    cout<<"Enter last name of the student:"<<endl;
    cin>>ln;
    cout<<"Enter roll no. of the student:"<<endl;
    cin>>rollno;
    cout<<"Enter GR no. of the student:"<<endl;
    cin>>gr;

    cout<<"\nEnter students marks:"<<endl;      //Getting marks of the student
    for(i=1;i<=sn;i++)
    {
        cout<<s[i]<<":";
        cin>>ssm[i];
    }
}

float result::calcinfo(int sn,int atm)
{
    int i;

    for(i=1;i<=sn;i++)      //Calculating total marks
    {
        tm=tm+ssm[i];
    }

    p=(tm*100)/atm;

    for(i=1;i<=sn;i++)      //Calculating in how many subjects student is passed & failed
    {
        if(ssm[i]>=35)
        {
            ps++;
        }
        else if(ssm[i]<35)
        {
            fs++;
        }
    }

    if(p>=35)       //Calculating percentage
    {
        return 1;
    }
    else if(p<35)
    {
        return 0;
    }
}


void result::printinfo(int sn,string s[10],int atm, int sm[10])
{
    int i;

    cout<<"\n**********Result**********"<<endl;     //Printing general info
    cout<<"Name:"<<fn<<" "<<mn<<" "<<ln<<endl;
    cout<<"Roll No.:"<<rollno<<endl;
    cout<<"GR No.:"<<gr<<endl;

    cout<<"\nMarks:"<<endl;     //Printing marks
    for(i=1;i<=sn;i++)
    {
        cout<<s[i]<<":"<<ssm[i]<<endl;
    }

    for(i=1;i<=sn;i++)      //Calculating subject grades
    {
        sg[i]=(ssm[i]*100)/sm[i];
    }

    cout<<"\nGrades:"<<endl;        //Printing grades
    for(i=1;i<=sn;i++)
    {
        cout<<s[i]<<":";

        if(sg[i]>=91 && sg[i]<=100)
        {
            cout<<"A1"<<endl;
        }
        else if(sg[i]>=81 && sg[i]<91)
        {
            cout<<"A2"<<endl;
        }
        else if(sg[i]>=71 && sg[i]<81)
        {
            cout<<"B1"<<endl;
        }
        else if(sg[i]>=61 && sg[i]<71)
        {
            cout<<"B2"<<endl;
        }
        else if(sg[i]>=51 && sg[i]<61)
        {
            cout<<"C1"<<endl;
        }
        else if(sg[i]>=35 && sg[i]<51)
        {
            cout<<"C2"<<endl;
        }
        else if(sg[i]>=0 && sg[i]<35)
        {
            cout<<"E"<<endl;
        }
    }

    cout<<"\nTotal marks:"<<tm<<"/"<<atm<<endl;     //Printing overall marks & percentage
    cout<<"Percentage:"<<p<<" %"<<endl;
    cout<<"You have passed in "<<ps<<" subjects and failed in "<<fs<<" subjects"<<endl;

    cout<<"\nRemarks:";     //Giving remarks

    if(p>=75 && p<100)
    {
        cout<<"Passed with First Class with Distinction"<<endl;
    }
    else if(p>=60 && p<75)
    {
        cout<<"Passed with First Class"<<endl;
    }
    else if(p>=45 && p<60)
    {
        cout<<"Passed with Second Class"<<endl;
    }
    else if(p>=35 && p<45)
    {
        cout<<"Passed"<<endl;
    }
    else if(p>=0 && p<35)
    {
        cout<<"Failed"<<endl;
    }
}

int main()
{
    result r[100];
    string s[10];
    int n,i,sn,cv,cvfg,sm[10],atm=0,tps=0,tfs=0;

    cout<<" **********Welcome to the student result software**********"<<endl;

    cout<<"\nYou can make maximum 100 student's result"<<endl;
    cout<<"Enter how many student's you want to make:"<<endl;       //How many student's result
    cin>>n;

    cout<<"\nEnter how many subjects are there:"<<endl;     //How many subjects
    cin>>sn;

    cout<<"\nAssign names of the subjects:"<<endl;      //Assigning name to subjects

    for(i=1;i<=sn;i++)
    {
        cout<<"Subject "<<i<<":"<<endl;
        cin>>s[i];
    }

    cout<<"\nEnter the total marks of each subject:"<<endl;     //Taking total marks of each subject

    for(i=1;i<=sn;i++)
    {
        cout<<s[i]<<":";
        cin>>sm[i];
    }

    for(i=1;i<=sn;i++)      //Calculating total marks of all subjects
    {
        atm=atm+sm[i];
    }

    for(i=1;i<=n;i++)       //Getting student's info
    {
        cout<<"\n\nEnter the info of "<<i<<" student:"<<endl;
        r[i].getinfo(sn,s);
    }

    for(i=1;i<=n;i++)       //Calculating marks
    {
        cv=r[i].calcinfo(sn,atm);

        if(cv==1)
        {
            tps++;
        }
        else if(cv==0)
        {
            tfs++;
        }
    }

    for(i=1;i<=n;i++)       //Printing of result
    {
        cout<<"\n\nResult of "<<i<<" student"<<endl;
        r[i].printinfo(sn,s,atm,sm);
    }

    cout<<"\n\n**********Class performance**********"<<endl;        //Printing overall class performance

    cout<<"\nTotal passed students:"<<tps<<endl;
    cout<<"Total failed students:"<<tfs<<endl;

    getch();
}
