package com.company;

import java.util.Scanner;

class Sdz1 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double aConvertir, convertit=0;
        char reponse=' ', mode = ' ';

        System.out.println("CONVERTISSEUR DEGRÉS CELSIUS ET DEGRÉS FAHRENHEIT");
        System.out.println("-------------------------------------------------");

        do{

            do{
                mode = ' ';
                System.out.println("Choisissez le mode de conversion : ");
                System.out.println("1 - Convertisseur Celsius - Fahrenheit");
                System.out.println("2 - Convertisseur Fahrenheit - Celsius ");
                mode = sc.nextLine().charAt(0);

                if(mode != '1' && mode != '2')
                    System.out.println("Mode inconnu, veuillez réitérer votre choix.");

            }while (mode != '1' && mode != '2');

            System.out.println("Température à convertir :");
            aConvertir = sc.nextDouble();
            sc.nextLine();

            if(mode == '1'){
                convertit = ((9.0/5.0) * aConvertir) + 32.0;
                System.out.print(aConvertir + " °C correspond à : ");
                System.out.println(arrondi(convertit, 2) + " °F.");
            }
            else{
                convertit = ((aConvertir - 32) * 5) / 9;
                System.out.print(aConvertir + " °F correspond à : ");
                System.out.println(arrondi(convertit, 2) + " °C.");
            }

            do{
                System.out.println("Souhaitez-vous convertir une autre température ?(O/N)");
                reponse = sc.nextLine().charAt(0);

            }while(reponse != 'O' && reponse != 'N');

        }while(reponse == 'O');

        System.out.println("Au revoir !");

    }

    public static double arrondi(double A, int B) {
        return (double) ( (int) (A * Math.pow(10, B) + .5)) / Math.pow(10, B);
    }
}
