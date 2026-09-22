class Base{
    int i, j;

    void fun()
    { System.out.println("Base fun");}
    void gun()
    { System.out.println("Base gun");}
    void sun()
    { System.out.println("Base sun");}
    void run()
    { System.out.println("Base run");}
}

class Derived extends Base{
    int x;
    void fun()
    { System.out.println("Derived fun");}
    void sun()
    { System.out.println("Derived sun");}
    void mun()
    { System.out.println("Derived mun");}
    void bun()
    { System.out.println("Derived bun");}
    
}

class VirtualDemo6 {

    public static void main(String A []){
        System.err.println("Great");
        Base bp = new Derived();
        bp.fun();   // Derived fun
        bp.gun();   // Base gun
        bp.sun();   // Derived sun
        bp.run();   // Base run
        // bp.mun();   // not allowed
        // bp.bun();   // not allowed
    }
}
