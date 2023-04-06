import java.util.*;


public class Main {
    public static void main(String[] args)
    {
        System.out.println("Flight code: " + flightCode());
        System.out.println("Seat number: " +seat((int)(Math.random()*99)+1));
        System.out.println("Group Number: " + groupNum());
        System.out.println("Gate Number: " + gate());
    }


    public static String flightCode()
    {
        int char1;
        int char2;
        int num;

        char1 = (int)(Math.random()*25)+65;
        char2 = (int)(Math.random()*25)+65;
        num = (int)(Math.random()*8999)+1000;

        String str =""+(char)char1+(char)char2+num;


       return str;
    }

    public static String seat(int age)
    {
        int char1;
        int num;

        char1 = (int)(Math.random()*9)+65;
        num = (int)(Math.random()*29)+1;

        String str =""+num+(char)char1;

        if (age <18)
            str +="-M";

        return str;
    }

    public static int groupNum()
    {

        return (int)(Math.random()*4)+1;
    }

    public static String gate()
    {
        String str ="";

        int char1 = (int)(Math.random()*8)+65;
        int num = (int)(Math.random()*33)+1;
        str+=num+char1;
        return str;
    }
}
