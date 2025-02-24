
import com.mycompany.unittest.UnitTest;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author admin
 */
public class Test01 {

    @Test
    public void test1() {
        Assertions.assertEquals(0, UnitTest.Power(0, -2));
    }

    @Test
    public void test2() {
        Assertions.assertEquals(25, UnitTest.Power(-5, 2));
    }

    @Test
    public void test3() {
        Assertions.assertThrows(ArithmeticException.class, () -> {
            UnitTest.Power(0, -2);
        });
    }

}
