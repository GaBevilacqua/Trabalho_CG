package mycompany;


public class Converter {
	

	public static int[] rgbTohsl(int R, int G, int B) {
        float r = R / 255.0f;
        float g = G / 255.0f;
        float b = B / 255.0f;
        float max = Math.max(r, Math.max(g, b));
        float min = Math.min(r, Math.min(g, b));
        float luminosidade = (max + min) / 2;
        float saturacao;
        if (max == min) {
            saturacao = 0; 
        } else {
            if (luminosidade < 0.5) {
                saturacao = (max - min) / (max + min);
            } else {
                saturacao = (max - min) / (2.0f - max - min);
            }
        }
        float matiz = 0;
        if (max == min) {
            matiz = 0; 
        } else if (max == r) {
            matiz = ((g - b) / (max - min)) % 6;
        } else if (max == g) {
            matiz = ((b - r) / (max - min)) + 2;
        } else if (max == b) {
            matiz = ((r - g) / (max - min)) + 4;
        }
        matiz *= 60;
        if (matiz < 0) {
            matiz += 360;
        }
        int H = Math.round(matiz);
        int S = Math.round(saturacao * 100);
        int L = Math.round(luminosidade * 100);
        System.out.println("Valores convertidos para HSL:");
        System.out.println("H (Matiz): " + H);
        System.out.println("S (Satura��o): " + S);
        System.out.println("L (Luminosidade): " + L);

        return new int[]{H, S, L};
    }
    
	public static int[] hslToRgb(float h2, float s2, float l2) {
	    float h = h2 / 360.0f; 
	    float s = s2 / 100.0f; 
	    float l = l2 / 100.0f; 
	    float c = (1 - Math.abs(2 * l - 1)) * s;
	    float x = c * (1 - Math.abs((h * 6) % 2 - 1));
	    float m = l - c / 2;
	    float rp, gp, bp;
	    if (h < 1.0 / 6.0) {
	        rp = c; gp = x; bp = 0;
	    } else if (h < 2.0 / 6.0) {
	        rp = x; gp = c; bp = 0;
	    } else if (h < 3.0 / 6.0) {
	        rp = 0; gp = c; bp = x;
	    } else if (h < 4.0 / 6.0) {
	        rp = 0; gp = x; bp = c;
	    } else if (h < 5.0 / 6.0) {
	        rp = x; gp = 0; bp = c;
	    } else {
	        rp = c; gp = 0; bp = x;
	    }

	    // Ajustar com m
	    float r = (rp + m);
	    float g = (gp + m);
	    float b = (bp + m);


	    int R = Math.round(r * 255);
	    int G = Math.round(g * 255);
	    int B = Math.round(b * 255);
	    System.out.println("Valores convertidos para RGB:");
	    System.out.println("R: " + R);
	    System.out.println("G: " + G);
	    System.out.println("B: " + B);

	    return new int[]{R, G, B};
	}

}
