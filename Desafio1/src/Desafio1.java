public class Desafio1 {
    public static void main(String[] args) {
        String text = "Esqueci o isqueiro na esquina da escola.";
        StringBuilder newText = new StringBuilder();

        String[] words = text.split(" ");

        int countLetters = 0;
        int limiteLiner = 20;

        for (String word : words) {

            if(countLetters + word.length() >= limiteLiner) {
                countLetters = 0;
                newText.append('\n');
            }
            newText.append(word);
            newText.append(' ');
            countLetters += word.length() + 1;
        }
        System.out.println(newText);
    }
}

/*
Link do desafio -> https://dojopuzzles.com/problems/quebra-de-linha/
 */