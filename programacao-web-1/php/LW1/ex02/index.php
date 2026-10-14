<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Exercicio 2</title>
</head>

<body>
    <h2>Informe seus dados</h2>

    <form method="POST">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br><br>

        <label for="idade">Idade:</label>
        <input type="number" id="idade" name="idade" required><br><br>

        <button type="submit">Enviar Dados</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nome = $_POST["nome"];
        $idade = $_POST["idade"];

        $mensagem = "Nome: $nome\nIdade: $idade anos";

        echo "<script>
            alert(" . json_encode($mensagem) . ");
            window.location.href = 'index.php';
        </script>";
    }
    ?>
</body>

</html>