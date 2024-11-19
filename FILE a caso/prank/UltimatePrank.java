import javax.swing.JOptionPane;
import java.awt.Toolkit;
import java.util.Random;

public class UltimatePrank {
    public static void main(String[] args) {
        // Array di titoli per confondere la vittima
        String[] titles = {"Attenzione!", "Errore critico!", "Messaggio importante", "Hai un virus!"};
        Random random = new Random();
        int messageCount = 0;

        while (messageCount < 10) { // Mostra 10 messaggi e poi chiude
            try {
                // Ritardo casuale tra i messaggi
                int delay = random.nextInt(5000) + 1000; // da 1 a 6 secondi
                Thread.sleep(delay);

                // Cambia titolo in modo casuale
                String title = titles[random.nextInt(titles.length)];

                // Emetti un beep di sistema

                // Mostra il messaggio di scherzo
                JOptionPane.showMessageDialog(null, "Messaggio misterioso numero " + (messageCount + 1), title, JOptionPane.WARNING_MESSAGE);

                messageCount++;
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // Messaggio finale e chiusura del programma
        JOptionPane.showMessageDialog(null, "Troppi messaggi! Addio!");
        System.exit(0);
    }
}
