public class If_try
{   public class Addition{
        public static int max(int No1, int No2,int No3)
        {
            if(No1 > No2)
            {
                return No1;
            }
            else
            {
                return No2;
            }
        }
    }
    public static void main(String[] arg)
    {
        int Ans = Addition.max(15,20,55);
        System.err.println(Ans);
    }
}
