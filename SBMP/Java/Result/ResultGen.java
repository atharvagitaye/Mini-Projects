package Result;
import java.util.*;

class GetStuInfo
{   
    static Scanner sc=new Scanner(System.in);
    String name,dp;
    public String rn;
    int upr,i,sm,tsn,tfs=0,tps=0,ftsm=0,stsm=0;
    int subm[],stm[];
    double sper[],pers;

    public void GetInfo(String s[],int sn) throws Exception
   {
        System.out.println();
        System.out.println("Enter name:");
        name=sc.next();
        System.out.println("Enter roll no.:");
        rn=sc.next();

        tsn=sn;

        stm=new int[tsn];

        for(i=0;i<tsn;i++)
        {
            System.out.println("Enter marks of "+(s[i])+":");
            stm[i]=sc.nextInt();
        }
   }
    
   public void UpdateResult(int upo) throws Exception
   {
        upr=upo;

        switch(upr)
        {
            case 1: System.out.println();
                    System.out.println("Enter name:");
                    name=sc.next();
                    break;

            case 2: System.out.println();
                    System.out.println("Enter roll no.:");
                    rn=sc.next();
                    break;
        }
   }
}

class CalcRes extends GetStuInfo
{
    public void MakeResult(int sn,int tm[])
    {
        sper=new double[tsn];

        for(i=0;i<tsn;i++)
        {
            sper[i]=stm[i]*(tm[i]/100);

            if(sper[i]<35)
            {
                tfs++;
            }
            else
            {
                tps++;
            }
        }

        for(i=0;i<tsn;i++)
        {
            ftsm=ftsm+tm[i];
            stsm=stsm+stm[i];
        }

        pers=(stsm*100)/ftsm;
    }
}

public class ResultGen extends CalcRes
{
    public void FinalResult(String dep,int sem,int tm[],String s[])
    {
        System.out.println();
        System.out.println("Name:"+name);
        System.out.println("Department:"+dep);
        System.out.println("Semester:"+sem);
        System.out.println("Roll no.:"+rn);
        System.out.println();
        System.out.println("Marks:");
        for(i=0;i<tsn;i++)
        {
            System.out.println((s[i])+":"+(stm[i])+"/"+(tm[i]));
        }

        System.out.println();
        System.out.println("Total marks:"+stsm+"/"+ftsm);
        System.out.println("Percentage:"+pers+"%");
        System.out.println("Passed in "+tps+" subjects and failed in "+tfs+" subjects");

        System.out.println();
        System.out.print("Remarks:");
        if(pers>=75 && pers<100)
        {
            System.out.print("Passed with First Class with Distinction");
        }
        else if(pers>=60 && pers<75)
        {
            System.out.print("Passed with First Class");
        }
        else if(pers>=45 && pers<60)
        {
            System.out.print("Passed with Second Class");
        }
        else if(pers>=35 && pers<45)
        {
            System.out.print("Passed");
        }
        else if(pers>=0 && pers<35)
        {
            System.out.print("Failed");
        }
        System.out.println();
        System.out.println();
    }
}