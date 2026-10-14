<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Exercicio 5</title>
</head>

<body>
    <h2>Sorteio Mega Sena</h2>

    <form method="POST">
        <button type="submit">Sortear numeros</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $numeros = [];

        while (count($numeros) < 6) {
            $numero = random_int(0, 60);

            if (!in_array($numero, $numeros)) {
                $numeros[] = $numero;
            }
        }

        sort($numeros);

        echo "<h3>Numeros sorteados:</h3>";
        echo implode(" - ", $numeros);
    }
    ?>
</body>

</html>