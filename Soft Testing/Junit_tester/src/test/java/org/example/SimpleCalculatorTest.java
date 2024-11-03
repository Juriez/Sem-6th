package org.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SimpleCalculatorTest {
  @Test
  void addTwoInteger() {
    var calculator = new SimpleCalculator();
    assertEquals(11, calculator.add(4, 7)); // This should pass
  }
}
