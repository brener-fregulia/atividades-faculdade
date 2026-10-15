<?php
session_start();

if (!isset($_SESSION["nomes"])) {
    $_SESSION["nomes"] = [];
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $acao = $_POST["acao"];

    if ($acao == "adicionar") {
        $nome = trim($_POST["nome"]);

        if ($nome != "") {
            $_SESSION["nomes"][] = $nome;
        }
    }

    if ($acao == "limpar") {
        $_SESSION["nomes"] = [];
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Exercicio 7</title>
</head>

<body>
    <h2>Cadastro de nomes</h2>

    <form method="POST">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome">

        <button type="submit" name="acao" value="adicionar">Adicionar</button>
        <button type="submit" name="acao" value="listar">Listar nomes</button>
        <button type="submit" name="acao" value="limpar">Limpar lista</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST" && $acao == "listar") {
        echo "<h3>Nomes cadastrados:</h3>";

        if (empty($_SESSION["nomes"])) {
            echo "<p>Nenhum nome cadastrado.</p>";
        } else {
            echo "<ul>";

            foreach ($_SESSION["nomes"] as $nome) {
                echo "<li>" . htmlspecialchars($nome) . "</li>";
            }

            echo "</ul>";
        }
    }
    ?>
</body>

</html>