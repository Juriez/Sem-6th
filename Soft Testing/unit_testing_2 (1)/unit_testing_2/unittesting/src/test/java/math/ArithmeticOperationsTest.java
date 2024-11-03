package math;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ArithmeticOperationsTest {

    ArithmeticOperations arithmeticOperations = new ArithmeticOperations();

    @Test
    public void testDivide_ValidInputs() {
        assertEquals(2.0, arithmeticOperations.divide(4.0, 2.0));
        assertEquals(5.0, arithmeticOperations.divide(10.0, 2.0));
    }

    @Test
    public void testDivide_DenominatorZero() {
        // Testing division by zero to ensure it throws ArithmeticException
        assertThrows(ArithmeticException.class, () -> arithmeticOperations.divide(5.0, 0.0));
    }

    @Test
    public void testMultiply_ValidInputs() {
        assertEquals(20, arithmeticOperations.multiply(4, 5));
        assertEquals(0, arithmeticOperations.multiply(4, 0)); // Multiplying with zero
    }

    @Test
    public void testMultiply_NegativeInputs() {
        // Testing for negative inputs
        assertThrows(IllegalArgumentException.class, () -> arithmeticOperations.multiply(-4, 5));
        assertThrows(IllegalArgumentException.class, () -> arithmeticOperations.multiply(4, -5));
    }

    @Test
    public void testMultiply_Overflow() {
        // Testing multiplication overflow
        assertThrows(IllegalArgumentException.class, () -> arithmeticOperations.multiply(Integer.MAX_VALUE, 2));
    }
}
