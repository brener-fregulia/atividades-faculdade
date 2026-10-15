<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require __DIR__ . "/vendor/autoload.php";

$erro = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nome = trim($_POST["nome"]);
    $email = trim($_POST["email"]);
    $mensagem = trim($_POST["mensagem"]);

    if ($nome == "" || !filter_var($email, FILTER_VALIDATE_EMAIL) || $mensagem == "") {
        $erro = "Dados invalidos.";
    } else {
        $mail = new PHPMailer(true);

        try {
            $mail->isSMTP();
            $mail->Host = "smtp.gmail.com";
            $mail->SMTPAuth = true;
            $mail->Username = getenv("SMTP_EMAIL");
            $mail->Password = getenv("SMTP_SENHA");
            $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
            $mail->Port = 587;

            $mail->setFrom(getenv("SMTP_EMAIL"), "Formulario de contato");
            $mail->addAddress(getenv("SMTP_EMAIL"));
            $mail->addReplyTo($email, $nome);

            $mail->CharSet = "UTF-8";
            $mail->Subject = "Contato de $nome";
            $mail->Body = "Nome: $nome\nEmail: $email\n\nMensagem:\n$mensagem";

            $mail->send();

            echo "<script>
                alert('Email enviado com sucesso!');
                window.location.href = 'index.php';
            </script>";
        } catch (Exception $e) {
            $erro = "Erro ao enviar o email.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Exercicio 8</title>
</head>

<body>
    <h2>Formulario de contato</h2>

    <form method="POST">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="mensagem">Mensagem:</label><br>
        <textarea id="mensagem" name="mensagem" required></textarea><br><br>

        <button type="submit">Enviar mensagem</button>
    </form>

    <?php
    if ($erro != "") {
        echo "<p>$erro</p>";
    }
    ?>
</body>

</html>