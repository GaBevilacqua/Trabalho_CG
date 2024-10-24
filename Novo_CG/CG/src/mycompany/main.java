package mycompany;

import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class main extends JFrame {
    private JPanel cardPanel;
    private CardLayout cardLayout;
    private JTextField textField;
    private JTextField textField_1;
    private JTextField textField_2;
    private JTextField textField_3;
    private JTextField textField_4;
    private JTextField textField_5;
    private JPanel colorPanel;

    public main() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 736, 488);
        cardLayout = new CardLayout();
        cardPanel = new JPanel(cardLayout);
        getContentPane().add(cardPanel, BorderLayout.CENTER); 
        JPanel panelCirculo = new JPanel();
        
        JPanel panelConversorRGB = new JPanel();
        panelConversorRGB.setLayout(null);

        
        cardPanel.add(panelConversorRGB, "ConversorRGB");
        JLabel lblNewLabel = new JLabel("RGB");
        lblNewLabel.setBounds(127, 75, 45, 13);
        panelConversorRGB.add(lblNewLabel);
        JLabel lblNewLabel_1 = new JLabel("HSL");
        lblNewLabel_1.setBounds(515, 75, 45, 13);
        panelConversorRGB.add(lblNewLabel_1);
 
        JLabel lblNewLabel_2 = new JLabel("R");
        lblNewLabel_2.setBounds(63, 153, 45, 13);
        panelConversorRGB.add(lblNewLabel_2);
        
        JLabel lblNewLabel_3 = new JLabel("G");
        lblNewLabel_3.setBounds(63, 208, 45, 13);
        panelConversorRGB.add(lblNewLabel_3);
        
        JLabel lblNewLabel_4 = new JLabel("B");
        lblNewLabel_4.setBounds(63, 269, 45, 13);
        panelConversorRGB.add(lblNewLabel_4);
        
        textField = new JTextField();
        textField.setBounds(91, 150, 96, 19);
        panelConversorRGB.add(textField);
        textField.setColumns(10);
        
        textField_1 = new JTextField();
        textField_1.setBounds(91, 205, 96, 19);
        panelConversorRGB.add(textField_1);
        textField_1.setColumns(10);
        
        textField_2 = new JTextField();
        textField_2.setBounds(91, 266, 96, 19);
        panelConversorRGB.add(textField_2);
        textField_2.setColumns(10);
        
        JLabel lblNewLabel_5 = new JLabel("H");
        lblNewLabel_5.setBounds(474, 153, 45, 13);
        panelConversorRGB.add(lblNewLabel_5);
        
        JLabel lblNewLabel_6 = new JLabel("S");
        lblNewLabel_6.setBounds(474, 208, 45, 13);
        panelConversorRGB.add(lblNewLabel_6);
        
        JLabel lblNewLabel_7 = new JLabel("I");
        lblNewLabel_7.setBounds(474, 269, 45, 13);
        panelConversorRGB.add(lblNewLabel_7);
        
        textField_3 = new JTextField();
        textField_3.setBounds(515, 150, 96, 19);
        panelConversorRGB.add(textField_3);
        textField_3.setColumns(10);
        
        textField_4 = new JTextField();
        textField_4.setBounds(515, 205, 96, 19);
        panelConversorRGB.add(textField_4);
        textField_4.setColumns(10);
        
        textField_5 = new JTextField();
        textField_5.setBounds(515, 269, 96, 19);
        panelConversorRGB.add(textField_5);
        textField_5.setColumns(10);
        
        JButton btnNewButton = new JButton("RGB -> HSL");
        btnNewButton.setBounds(63, 327, 124, 27);
        panelConversorRGB.add(btnNewButton);
        
        JButton btnNewButton_1 = new JButton("HSL -> RGB");
        btnNewButton_1.setBounds(474, 330, 137, 21);
        panelConversorRGB.add(btnNewButton_1);
        
        colorPanel = new JPanel();
        colorPanel.setBounds(237, 150, 198, 203);
        panelConversorRGB.add(colorPanel);

        JMenuBar menuBar = new JMenuBar();
        setJMenuBar(menuBar);
        
        
        JMenu mnNewMenu_1 = new JMenu("Conversor");
        menuBar.add(mnNewMenu_1);
        
        JMenuItem mntmConversorRGB = new JMenuItem("Conversor RGB e HSL");
        mntmConversorRGB.addActionListener(e -> cardLayout.show(cardPanel, "ConversorRGB"));
        mnNewMenu_1.add(mntmConversorRGB);
        
        btnNewButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int R = Integer.parseInt(textField.getText());
                int G = Integer.parseInt(textField_1.getText());
                int B = Integer.parseInt(textField_2.getText());

                int[] hsl = Converter.rgbTohsl(R, G, B);

                textField_3.setText(String.valueOf(hsl[0]));
                textField_4.setText(String.valueOf(hsl[1]));
                textField_5.setText(String.valueOf(hsl[2]));
                colorPanel.setBackground(new Color(R, G, B)); 
            }
        });
        
        btnNewButton_1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                float H = Float.parseFloat(textField_3.getText());
                float S = Float.parseFloat(textField_4.getText());
                float L = Float.parseFloat(textField_5.getText());
                int[] rgb = Converter.hslToRgb(H, S, L);


                textField.setText(String.valueOf(rgb[0]));
                textField_1.setText(String.valueOf(rgb[1]));
                textField_2.setText(String.valueOf(rgb[2]));
                colorPanel.setBackground(new Color(rgb[0], rgb[1], rgb[2]));
            }
        });
    }
    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            try {
                main frame = new main();
                frame.setVisible(true);
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }
}
