import java.util.*; 
import Result.*;

class StudentResult
{
    public static void main(String args[]) throws Exception
    {
        System.out.println();
        System.out.println("Welcome to Student Result Application");

        Scanner sc=new Scanner(System.in);

        ResultGen r[]=new ResultGen[100];
        int sco=0,id=0,i=0,choice,sem;
        int stuupop,sturf,sn;
        String updrer,dep;
        String s[];
        int tm[];

        System.out.println();
        System.out.println("Enter department:");
        dep=sc.next();

        labelsem:
        while(true)
        {
            System.out.println("Enter semester:");
            sem=sc.nextInt();

            if(sem<0 || sem>8)
            {
                System.out.println();
                System.out.println("Enter valid semester in range of(1,8)");
                continue labelsem;
            }
            else
            {
                break labelsem;
            }
        }

        System.out.println();
        System.out.println("Enter total number of subjects:");
        sn=sc.nextInt();

        s=new String[sn];

        for(i=0;i<sn;i++)
        {
            System.out.println("Enter name of subject "+(i+1)+":");
            s[i]=sc.next();
        }   

        tm=new int[sn];

        System.out.println();
        System.out.println("Enter total marks of all subjects:");

        for(i=0;i<sn;i++)
        {
            System.out.println("Enter total marks of "+s[i]+":");
            tm[i]=sc.nextInt();
        }

        while(true)
        {
            System.out.println();
            System.out.println("-----Menu-----");
            System.out.println("1. Make student result");
            System.out.println("2. Update student result");
            System.out.println("3. Search student result");
            System.out.println("4. Display total no. of results");
            System.out.println("5. Display all students result");
            System.out.println("6. Change department");
            System.out.println("7. Change semester");
            System.out.println("8. Exit");

            System.out.println();
            System.out.println("Enter the choice:");
            choice=sc.nextInt();

            switch(choice)
            {
                case 1: System.out.println();
                        System.out.println("Enter data of student "+(id+1)+":");
                        r[id]=new ResultGen();
                        r[id].GetInfo(s,sn);
                        r[id].MakeResult(sn,tm);
                        id++;
                        sco++;
                        break;

                case 2: System.out.println();

                        labeluprnf:
                        while(true)
                        {
                            System.out.println("Enter roll no. of student:");
                            updrer=sc.next();

                            for(i=0;i<sco;i++)
                            {
                                   
                                if((r[i].rn).equals(updrer))
                                {
                                    break labeluprnf;
                                }
                                
                                if(i==(sco-1))
                                {
                                    System.out.println();
                                    System.out.println("Roll no. not found !!");
                                    System.out.println("Enter correct roll no.");
                                    continue labeluprnf;
                                }
                                
                            }
                        }
                        
                        labelupd:
                        while(true)
                        {    
                            System.out.println();
                            System.out.println("1. Update name");
                            System.out.println("2. Update roll no.");
                            System.out.println("Enter the choice:");
                            System.out.println();
                            stuupop=sc.nextInt();

                            if(stuupop<1 || stuupop>2)
                            {
                                continue labelupd;
                            }
                            else
                            {
                                break labelupd;
                            }
                        }
                        
                        switch(stuupop)
                        {
                            case 1: r[i].UpdateResult(stuupop);
                                    break;

                            case 2: r[i].UpdateResult(stuupop);
                                    break;
                        }

                        break;
            
                case 3: System.out.println();

                        labelsere:
                        while(true)
                        {
                            System.out.println("Enter roll no. of student:");
                            updrer=sc.next();

                            for(i=0;i<sco;i++)
                            {
                                   
                                if((r[i].rn).equals(updrer))
                                {
                                    r[i].FinalResult(dep,sem,tm,s);
                                    break labelsere;
                                }
                                
                                if(i==(sco-1))
                                {
                                    System.out.println();
                                    System.out.println("Roll no. not found !!");
                                    System.out.println("Enter correct roll no.");
                                    continue labelsere;
                                }
                            }
                        }

                        break;

                case 4: System.out.println();
                        System.out.println("Total no. of results= "+sco);
                        sc.nextLine();
                        break;

                case 5: System.out.println();
                        System.out.println("Result of all students:");
                        System.out.println();
                        
                        for(i=0;i<sco;i++)
                        {
                            System.out.println("Result of student "+(i+1)+":");

                            r[i].FinalResult(dep,sem,tm,s);
                        }
                        
                        break;

                case 6: System.out.println();
                        System.out.println("Enter depatment:");
                        dep=sc.next();
                        break;

                case 7: System.out.println();
                        
                        labelsem2:
                        while(true)
                        {
                            System.out.println("Enter semester:");
                            sem=sc.nextInt();

                            if(sem<0 || sem>8)
                            {
                                System.out.println();
                                System.out.println("Enter valid semester in range of(1,8)");
                                continue labelsem2;
                            }
                            else
                            {
                                break labelsem2;
                            }
                        } 

                        System.out.println();
                        System.out.println("Enter total number of subjects:");
                        sn=sc.nextInt();

                        s=new String[sn];

                        for(i=0;i<sn;i++)
                        {   
                            System.out.println("Enter name of subject "+(i+1)+":");
                            s[i]=sc.next();
                        }     

                        tm=new int[sn];

                        System.out.println();
                        System.out.println("Enter total marks of all subjects:");

                        for(i=0;i<sn;i++)
                        {
                            System.out.println("Enter total marks of "+s[i]+":");
                            tm[i]=sc.nextInt();
                        }

                        break;

                case 8: System.out.println();
                        System.out.println("Thanks for using our application :-)");
                        sc.nextLine();
                        System.exit(0);
                        break;
            }
        }
    }
}