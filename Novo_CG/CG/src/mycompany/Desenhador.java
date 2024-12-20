package mycompany;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Desenhador extends JFrame {

    private JPanel painelDesenho;
    private String modoDesenho = "livre";
    private Point pontoInicial;

    public Desenhador() {
        setTitle("Draw");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JMenuBar menuBar = new JMenuBar();
        JMenu menuDesenho = new JMenu("Desenho");
        JMenuItem itemLivre = new JMenuItem("Desenho Livre");
        JMenuItem itemLinha = new JMenuItem("Desenhar Linha");
        JMenuItem itemLinhaBresenham = new JMenuItem("Desenhar Linha Bresenham");
        JMenuItem itemCirculo = new JMenuItem("Desenhar C�rculo");
        JMenuItem ItemParametrico = new JMenuItem("Desenhar Circulo com Param\u00E9trica e Sim\u00E9trica");
        JMenuItem ItemSenCos = new JMenuItem("Desenhar Circulo com rota\u00E7\u00E3o (sen cos)");
        JMenuItem ItemBresenham = new JMenuItem("Desenhar C\u00EDrculo com Bresenham");
        JMenuItem ItemCohenSutherland = new JMenuItem("Recorte Cohen-Sutherland");
        JMenuItem ItemCasinha = new JMenuItem("Casinha");
        
        
        itemLivre.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                modoDesenho = "livre";
            }
        });

        itemLinha.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                modoDesenho = "linha";
            }
        });

        itemCirculo.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                modoDesenho = "circulo";
            }
        });
        itemLinhaBresenham.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                modoDesenho= "bresenham";
            }
        });
        
        ItemParametrico.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                modoDesenho = "circunferencia_parametrica";
            }
        });

        ItemSenCos.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                modoDesenho = "rotacao_sen_cos";
            }
        });

        ItemBresenham.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                modoDesenho = "bresenham_circunferencia";
            }
        });

        ItemCohenSutherland.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                modoDesenho = "recorte_cohen_sutherland";
            }
        });


        menuDesenho.add(itemLivre);
        menuDesenho.add(itemLinha);
        menuDesenho.add(itemLinhaBresenham);
        menuDesenho.add(itemCirculo);
        menuBar.add(menuDesenho);
        menuDesenho.add(ItemParametrico);
        menuDesenho.add(ItemSenCos);
        menuDesenho.add(ItemBresenham);
        menuDesenho.add(ItemCohenSutherland);
        menuDesenho.add(ItemCasinha);
        
        
        setJMenuBar(menuBar);

        painelDesenho = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
      
            }
        };

        painelDesenho.setBackground(Color.WHITE);
        painelDesenho.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                pontoInicial = e.getPoint();
            }
        });

        painelDesenho.addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                Graphics g = painelDesenho.getGraphics();
                g.setColor(Color.RED); 
                if (modoDesenho.equals("livre")) {
                    
                    g.drawLine(pontoInicial.x, pontoInicial.y, e.getX(), e.getY());
                    pontoInicial = e.getPoint();
                }
            }
        });

        painelDesenho.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseReleased(MouseEvent e) {
                Graphics g = painelDesenho.getGraphics();
                switch (modoDesenho) {
                    case "linha":
                        desenharLinha(g, pontoInicial.x, pontoInicial.y, e.getX(), e.getY());
                        break;
                    case "circulo":
                        desenharCirculo(g, pontoInicial.x, pontoInicial.y, e.getX(), e.getY());
                        break;
                    case "bresenham":
                        desenharLinhaBresenham(g, pontoInicial.x, pontoInicial.y, e.getX(), e.getY());
                        break;
                    case "circunferencia_parametrica":
                        desenharCirculoParametrico(g, pontoInicial.x, pontoInicial.y, e.getX(), e.getY());
                        break;
                    case "rotacao_sen_cos":
                        sencosCirculo(g, pontoInicial.x, pontoInicial.y, e.getX(), e.getY());
                        break;
                    case "bresenham_circunferencia":
                        int raio = (int) Math.sqrt(Math.pow(e.getX() - pontoInicial.x, 2) + Math.pow(e.getY() - pontoInicial.y, 2));
                        desenharCircunferenciaBresenham(g, pontoInicial.x, pontoInicial.y, raio);
                        break;
                    case "recorte_cohen_sutherland":
                        double xmin = 100;
                        double ymin = 100;
                        double xmax = 700;
                        double ymax = 500;
                        CohenSutherland(g, pontoInicial.x, pontoInicial.y, e.getX(), e.getY(), xmin, ymin, xmax, ymax);
                        break;
                    default:
                        break;
                }
            }
        });



        getContentPane().add(painelDesenho);
    }
    private void limparTela(Graphics g){
       g.fillRect(0, 0, getWidth(), getHeight());
    }
    private void desenharLinha(Graphics g, int x0, int y0, int x1, int y1) {
        int deltay = y1 - y0;
        int deltax = x1 - x0;
        float m = (deltax != 0) ? (float) deltay / deltax : Float.POSITIVE_INFINITY; 

        if (Math.abs(deltax) > Math.abs(deltay)) { 
            if (x1 < x0) {
                for (int x = x1; x <= x0; x++) {
                    int y = (int) Math.round(m * (x - x0) + y0);
                    g.drawLine(x, y, x, y);  
                    System.out.println("entrou aqui 1");
                }
            } else {
                for (int x = x0; x <= x1; x++) {
                    int y = (int) Math.round(m * (x - x0) + y0);
                    g.drawLine(x, y, x, y);  
                    System.out.println("entrou aqui 2");
                }
            }
        } else { 
            if (y1 < y0) {
                for (int y = y1; y <= y0; y++) {
                    int x = (int) Math.round((y - y0) / m + x0);
                    g.drawLine(x, y, x, y); 
                    System.out.println("entrou aqui 3");
                }
            } else {
                for (int y = y0; y <= y1; y++) {
                    int x = (int) Math.round((y - y0) / m + x0);
                    g.drawLine(x, y, x, y);  
                    System.out.println("entrou aqui 4");
                }
            }
        }

        System.out.println("Ponto inicial: (" + x0 + ", " + y0 + ")");
        System.out.println("Ponto final: (" + x1 + ", " + y1 + ")");
        System.out.println("Delta X: " + deltax);
        System.out.println("Delta Y: " + deltay);
    }

    private void desenharCirculo(Graphics g, int x0, int y0, int x1, int y1) {
       double raio = Math.sqrt(Math.pow((x1-x0),2)+Math.pow((y1-y0),2));
       int numPoints = (int) Math.max(1, 2*Math.PI*raio);
        
        for (int i = 0; i < numPoints; i++) {
            double angle = 2 * Math.PI * i / numPoints;
            int x = (int) Math.round(x0 + raio * Math.cos(angle));
            int y = (int) Math.round(y0 + raio * Math.sin(angle));
            g.drawLine(x, y, x, y);  
        }

        
    }

    private void desenharLinhaBresenham(Graphics g, int x0, int y0, int x1, int y1) {
        int dx = Math.abs(x1 - x0);
        int dy = Math.abs(y1 - y0);
        int sx = (x0 < x1) ? 1 : -1;
        int sy = (y0 < y1) ? 1 : -1;
        int err = dx - dy;

        while (true) {
            g.drawLine(x0, y0, x0, y0); 
            if (x0 == x1 && y0 == y1) {
                break;
            }
            int e2 = err * 2;
            if (e2 > -dy) {
                err -= dy;
                x0 += sx;
            }
            if (e2 < dx) {
                err += dx;
                y0 += sy;
            }
        }
    }
    
    private void desenharLinhaBresenham2(Graphics g, int x0, int y0, int x1, int y1) {
        int dx = x1-x0;
        int dy = y1-y0;
        int error = 2*dy-dx;
        
        int x = x0;
        int y= y0;
        for(; x<=x1;x++){
            g.drawLine(x, y, x, y);
            if (error>0){
                y++;
                error-=2*dx;
            }
            else{
                error+=2*dy;
            }
        }
      }
    
    private void desenharCirculoParametrico(Graphics g, int x0, int y0, int x1, int y1) {
        double raio = Math.sqrt(Math.pow((x1 - x0), 2) + Math.pow((y1 - y0), 2));
        for (double t = 0; t <= 6.28; t += 0.01) {
            int x = (int) Math.round(raio * Math.cos(t));
            int y = (int) Math.round(raio * Math.sin(t));
            desenharSimetria(g, x0, y0, x, y);
        }
    }

    private void desenharSimetria(Graphics g, int x0, int y0, int x, int y) {
        g.drawLine(x0 + x, y0 + y, x0 + x, y0 + y); 
        g.drawLine(x0 - x, y0 + y, x0 - x, y0 + y); 
        g.drawLine(x0 + x, y0 - y, x0 + x, y0 - y); 
        g.drawLine(x0 - x, y0 - y, x0 - x, y0 - y); 
        g.drawLine(x0 + y, y0 + x, x0 + y, y0 + x); 
        g.drawLine(x0 - y, y0 + x, x0 - y, y0 + x); 
        g.drawLine(x0 + y, y0 - x, x0 + y, y0 - x); 
        g.drawLine(x0 - y, y0 - x, x0 - y, y0 - x); 
    }

    
    private void desenharCircunferenciaBresenham(Graphics g, int x0, int y0, int raio) {
        int x = 0, y = raio;
        int d = 3 - 2 * raio;

        desenharSimetria(g, x0, y0, x, y);

        while (y >= x) {
            x++;
            if (d > 0) {
                y--;
                d = d + 4 * (x - y) + 10;
            } else {
                d = d + 4 * x + 6;
            }
            desenharSimetria(g, x0, y0, x, y);
        }
    }

    
    //Seno e cosseno
    private void sencosCirculo(Graphics g, int x0, int y0, int x1, int y1) {
        double raio = Math.sqrt(Math.pow((x1 - x0), 2) + Math.pow((y1 - y0), 2));
        double anguloRad; 
        double x = raio; 
        double y = 0; 

        for (int i = 0; i <= 360; i++) {
            anguloRad = Math.toRadians(i); 
            double cos1 = Math.cos(anguloRad);
            double sin1 = Math.sin(anguloRad);
            
            double xn = x * cos1 - y * sin1; 
            y = x * sin1 + y * cos1; 
            x = xn; 
            g.drawLine((int)(x0 + x), (int)(y0 + y), (int)(x0 + x), (int)(y0 + y));
        }
    }
    
    private final int INSIDE = 0; 
    private final int LEFT = 1;   
    private final int RIGHT = 2;  
    private final int BOTTOM = 4; 
    private final int TOP = 8;   

    private int calcCode(double x, double y, double xmin, double ymin, double xmax, double ymax) {
        int code = INSIDE;
        if (x < xmin) {
            code |= LEFT;
        } else if (x > xmax) {
            code |= RIGHT;
        }
        if (y < ymin) {
            code |= BOTTOM;
        } else if (y > ymax) {
            code |= TOP;
        }
        return code;
    }

    private void CohenSutherland(Graphics g, double x0, double y0, double x1, double y1, double xmin, double ymin, double xmax, double ymax) {
        int codigo0 = calcCode(x0, y0, xmin, ymin, xmax, ymax);
        int codigo1 = calcCode(x1, y1, xmin, ymin, xmax, ymax);
        boolean aceitar = false;

        while (true) {
            if ((codigo0 | codigo1) == 0) { 
                aceitar = true;
                break;
            } else if ((codigo0 & codigo1) != 0) { 
                break;
            } else {
                double x, y;

                int out_cod = (codigo0 != 0) ? codigo0 : codigo1;

                if ((out_cod & TOP) != 0) {
                    x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0);
                    y = ymax;
                } else if ((out_cod & BOTTOM) != 0) {
                    x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0);
                    y = ymin;
                } else if ((out_cod & RIGHT) != 0) {
                    y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0);
                    x = xmax;
                } else {
                    y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0);
                    x = xmin;
                }

                if (out_cod == codigo0) {
                    x0 = x;
                    y0 = y;
                    codigo0 = calcCode(x0, y0, xmin, ymin, xmax, ymax);
                } else {
                    x1 = x;
                    y1 = y;
                    codigo1 = calcCode(x1, y1, xmin, ymin, xmax, ymax);
                }
            }
        }

        if (aceitar) {
            g.drawLine((int) x0, (int) y0, (int) x1, (int) y1);
        }
    }



    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new Desenhador().setVisible(true);
            }
        });
    }
}