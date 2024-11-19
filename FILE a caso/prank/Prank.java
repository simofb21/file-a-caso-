import javax.swing.JOptionPane;
import java.awt.Toolkit;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Random;

public class Prank {
    public static void main(String[] args) {
        String ipAddress;
        try {
            // Ottieni l'indirizzo IP del sistema locale
            ipAddress = InetAddress.getLocalHost().getHostAddress();
        } catch (UnknownHostException e) {
            ipAddress = "Sconosciuto";
        }

        // Array di titoli per confondere l'utente
        String[] titles = {
            "Attenzione!",
            "Errore Fatale!",
            "Virus Detected!",
            "Avviso di Sicurezza",
            "Warning",
            "Critico!"
        };

        Random random = new Random();
        int messageCount = 0;
        int maxMessages = 100;  // Numero massimo di messaggi prima della chiusura

        while (messageCount < maxMessages) {
            // Emetti un beep di sistema
            Toolkit.getDefaultToolkit().beep();

            // Genera un numero casuale per i virus ogni volta che mostra un messaggio
            int virusCount = random.nextInt(1000) + 1;

            // Array di messaggi per lo scherzo (il numero di virus è rigenerato ogni volta)
            String[] messages = {
                "SEI FOTTUTO! Ho preso il tuo IP di merda: " + ipAddress,
                "Trovati " + virusCount + " nuovi virus!",
                "Usa Linux per evitare i virus!",
                "Errore Critico: Si prega di chiudere questa finestra al più presto.",
                "Non hai chiuso la finestra, il tuo computer potrebbe esplodere!"
            };

            // Seleziona un messaggio e un titolo casuali
            String message = messages[random.nextInt(messages.length)];
            String title = titles[random.nextInt(titles.length)];

            // Crea e configura la finestra di dialogo con larghezza adattata alla lunghezza del messaggio
            int width = Math.max(400, message.length() * 7); // Adatta larghezza alla lunghezza del messaggio
            int height = 150;
            JOptionPane pane = new JOptionPane(message, JOptionPane.WARNING_MESSAGE);
            pane.setPreferredSize(new java.awt.Dimension(width, height));

            // Mostra la finestra di dialogo
            JOptionPane.showMessageDialog(null, pane, title, JOptionPane.WARNING_MESSAGE);

            messageCount++;
        }

        // Messaggio finale e chiusura del programma
        JOptionPane.showMessageDialog(null, "Scherzo finito! Alla prossima!");
        System.exit(0);
    }
}
