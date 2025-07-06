import javax.swing.*;

public class StudentPortal {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Student Portal");
        JLabel label = new JLabel("Welcome to Student Portal");
        label.setBounds(50, 50, 200, 30);
        frame.add(label);
        frame.setSize(300, 200);
        frame.setLayout(null);
        frame.setVisible(true);
    }
}