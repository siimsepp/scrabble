<?php

class Form {

    public static function printHeader() { 
        $str = '<!DOCTYPE html>';
        $str .= '<html lang="en">';
        $str .= '<head>';
        $str .= '<meta charset="UTF-8">';
        $str .= '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
        $str .= '<meta http-equiv="X-UA-Compatible" content="ie=edge">';
        $str .= '<title>Document</title>';
        $str .= '</head>';
        $str .= '<body>';
        
        return $str;
    }


    // tahed_kaes = 'tlaajka'
    // taht_laual = 'g'
    // mitu_enne = 7
    // mitu_parast = 7


    public static function printForm() { 
        $str = '<form action="" method="POST">';
        $str .= 'Tähed käes: <input type="text" name="tahed_kaes"><br>';
        $str .= 'Täht laual: <input type="text" name="taht_laual"><br>';
        $str .= 'Mitu tähte maksimaalselt mahub ennne lauas olevat tähte: <input type="text" name="kohti_enne"><br>';
        $str .= 'Mitu tähte maksimaalselt mahub pärast lauas olevat tähte: <input type="text" name="kohti_parast"><br>';
        $str .= '<input type="submit">';
        $str .= '</form>';

        return $str;
    }

    public static function printFooter() { 
        $str = '</body>';
        $str .= '</html>';
        
        return $str;
    }

}






 
