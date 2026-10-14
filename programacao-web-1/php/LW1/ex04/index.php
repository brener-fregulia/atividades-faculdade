<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Exercicio 4</title>
</head>

<body>
    <h2>Numeros pares</h2>

    <form method="POST">
        <label for="numero">Informe um numero:</label>
        <input type="number" id="numero" name="numero" min="0" required>

        <button type="submit">Listar</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $numero = (int) $_POST["numero"];

        echo "<h3>Numeros pares de 0 ate $numero:</h3>";

        for ($i = 0; $i <= $numero; $i += 2) {
            echo "$i ";
        }
    }
    ?>
</body>

</html>