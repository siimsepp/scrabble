<?php

class Form {

    public static function printHeader() { 
        $str = '<!DOCTYPE html>';
        $str .= '<html lang="en">';
        $str .= '<head>';
        $str .= '<meta charset="UTF-8">';
        $str .= '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
        $str .= '<meta http-equiv="X-UA-Compatible" content="ie=edge">';
        $str .= '<title>Scrabble</title>';
        $str .= '<link rel = "stylesheet" type = "text/css" href = "style.css" />';
        $str .= '</head>';
        $str .= '<body>';
        
        return $str;
    }


    public static function printForm() { 
        $str = '<form action="" method="POST">';
        $str .= 'Tähed käes:<br>';
        $str .= '<input type="text" name="tahed_kaes" placeholder="tähed käes" value="abcdefg"><br>';
        $str .= 'Täht laual:<br>';
        $str .= '<input type="text" name="taht_laual" placeholder="täht laual" value="h"><br>';
        $str .= 'Mitu tähte maksimaalselt mahub ennne lauas olevat tähte:<br>';
        $str .= '<input type="text" name="kohti_enne" placeholder="mitu enne" value="7"><br>';
        $str .= 'Mitu tähte maksimaalselt mahub pärast lauas olevat tähte:<br>';
        $str .= '<input type="text" name="kohti_parast" placeholder="mitu pärast" value="7"><br>';
        $str .= 'Sisesta tähe kordistajad enne lauas olevat tähte:<br>';
        $str .= '<input type="text" name="tahe_kord_enne" placeholder="tähe kordistajad enne" value="1111111"><br>';
        $str .= 'Sisesta tähe kordistajad pärast lauas olevat tähte:<br>';
        $str .= '<input type="text" name="tahe_kord_parast" placeholder="tähe kordistajad pärast" value="1111111"><br>';
        $str .= 'Sisesta sõna kordistajad enne lauas olevat tähte:<br>';
        $str .= '<input type="text" name="sona_kord_enne" placeholder="sõna kordistajad enne" value="1111111"><br>';
        $str .= 'Sisesta sõna kordistajad pärast lauas olevat tähte:<br>';
        $str .= '<input type="text" name="sona_kord_parast" placeholder="sõna kordistajad pärast" value="1111111"><br>';
        $str .= '<input type="submit" value="Tee päring">';
        $str .= '</form>';

        return $str;
    }


    public static function printFooter() { 
        $str = '</body>';
        $str .= '</html>';
        
        return $str;
    }


    public static function HTMLandmetabel($massiiv) {
        $str = '<table>';
        $str .= '<tr>';
        $str .= '<th>Sõna</th>';
        $str .= '<th>Punktid</th>';
        $str .= '</tr>';
        foreach($massiiv as $k => $v) {
            $str .= '<tr>';
            $str .= '<td>' . $k . '</td>';
            $str .= '<td>' . $v . '</td><br>';
            $str .= '</tr>';
        }
        $str .= '</table>';
        return $str;
    } 

}

