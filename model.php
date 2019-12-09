<?php

class Model {

    // $nimi = $_POST['name'];
    // $email = $_POST['email'];

    // Faili kirjutamine.
    public static function kirjutaJSON($andmed_kasutajalt) {
        $json_data = json_encode($andmed_kasutajalt, JSON_PRETTY_PRINT);
        file_put_contents('scrabble_sisend.json', $json_data); 
    }

    // Loen failist sisse JSONi ja teen sellest array.
    public static function loeJSON() {
        $json = file_get_contents('scrabble_tulemus.json');
        return json_decode($json, true);
    }



    // Kontroll, et kasutaja sisestatud andmed oleksid aktsepteeritaval kujul, mh. ohtlikud skriptid neutraliseeritud.
    public static function testSisend($andmed_sisse) {
        $andmed_sisse = trim($andmed_sisse);
        $andmed_sisse = stripslashes($andmed_sisse);
        $andmed_sisse = htmlentities($andmed_sisse);
        return $andmed_sisse;
    }



    // Funktsioon loob kasutaja sisestatust assoc array, mis on aluseks JSONi tegemisel.
    public static function makeRequestArray() {
        $jsonData = []; 
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            if (isset($_POST["tahed_kaes"])) {
                $tahed_kaes = self::testSisend($_POST["tahed_kaes"]);
                array_push($jsonData, ['tahed_kaes' => $tahed_kaes]);
            }
            if (isset($_POST["taht_laual"])) {
                $taht_laual = self::testSisend($_POST["taht_laual"]);
                array_push($jsonData, ['taht_laual' => $taht_laual]);
            }
            if (isset($_POST["kohti_enne"])) {
                $kohti_enne = self::testSisend($_POST["kohti_enne"]);
                array_push($jsonData, ['kohti_enne' => $kohti_enne]);
            }
            if (isset($_POST["kohti_parast"])) {
                $kohti_parast = self::testSisend($_POST["kohti_parast"]);
                array_push($jsonData, ['kohti_parast' => $kohti_parast]);
            }
            // header("Location: index.php");
        }
        return $jsonData;
    }

}

