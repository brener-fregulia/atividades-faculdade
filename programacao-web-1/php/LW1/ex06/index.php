<?php
session_start();
date_default_timezone_set("America/Sao_Paulo");

$mensagem = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $acao = $_POST["acao"];

    if ($acao == "sortear") {
        $numeros = [];

        while (count($numeros) < 6) {
            $numero = random_int(0, 60);

            if (!in_array($numero, $numeros)) {
                $numeros[] = $numero;
            }
        }

        sort($numeros);

        $_SESSION["numeros"] = $numeros;
        $_SESSION["salvo"] = false;
    }

    if ($acao == "salvar" && isset($_SESSION["numeros"]) && !$_SESSION["salvo"]) {
        $data = date("d/m/Y H:i:s");
        $numeros = implode(" - ", $_SESSION["numeros"]);

        $linha = "$data | $numeros" . PHP_EOL;

        $arquivo = __DIR__ . "/sorteios.txt";

        if (file_put_contents($arquivo, $linha, FILE_APPEND | LOCK_EX) !== false) {
            $_SESSION["salvo"] = true;
            $mensagem = "Sorteio salvo com sucesso!";
        } else {
            $mensagem = "Erro ao salvar o sorteio.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Exercicio 6</title>
</head>

<body>
    <h2>Sorteio Mega Sena</h2>

    <form method="POST">
        <button type="submit" name="acao" value="sortear">Sortear numeros</button>

        <?php if (isset($_SESSION["numeros"]) && !$_SESSION["salvo"]): ?>
            <button type="submit" name="acao" value="salvar">Salvar sorteio</button>
        <?php endif; ?>
    </form>

    <?php
    if (isset($_SESSION["numeros"])) {
        echo "<h3>Numeros sorteados:</h3>";
        echo implode(" - ", $_SESSION["numeros"]);
    }

    if ($mensagem != "") {
        echo "<p>$mensagem</p>";
    }
    ?>
</body>

</html>