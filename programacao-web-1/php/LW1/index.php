<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Programacao Web I</title>
</head>
<body>
    <h1>Lista 1 - Exercicios PHP</h1>

    <?php for ($i = 1; $i <= 8; $i++): ?>
        <p>
            <a href="ex<?= sprintf('%02d', $i) ?>/">
                Exercicio <?= $i ?>
            </a>
        </p>
    <?php endfor; ?>
</body>
</html>