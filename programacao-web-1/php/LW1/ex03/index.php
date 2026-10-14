<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Exercicio 3</title>
</head>

<body>
    <h2>Verificar maioridade</h2>

    <form method="POST">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br><br>

        <label for="nascimento">Data de nascimento:</label>
        <input type="date" id="nascimento" name="nascimento" required><br><br>

        <button type="submit">Verificar</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nome = $_POST["nome"];
        $nascimento = new DateTime($_POST["nascimento"]);
        $hoje = new DateTime();

        $idade = $nascimento->diff($hoje)->y;

        if ($nascimento > $hoje) {
            $mensagem = "Data de nascimento invalida";
        } elseif ($idade >= 18) {
            $mensagem = "$nome tem $idade anos e e maior de idade";
        } else {
            $mensagem = "$nome tem $idade anos e e menor de idade";
        }

        echo "<script>
            alert(" . json_encode($mensagem) . ");
        </script>";
    }
    ?>
</body>

</html>