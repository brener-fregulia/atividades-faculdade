program ArvoreBinaria;

uses
  crt;

type
  PtrNodoArvBin = ^NodoArvBin;

  NodoArvBin = record
    Conteudo: Integer;
    ArvEsq, ArvDir, Pai: PtrNodoArvBin;
  end;

function Maior(A, B: Integer): Integer;
begin
  if A > B then
    Maior := A
  else
    Maior := B;
end;

procedure PreOrdem(Raiz: PtrNodoArvBin);
begin
  if Raiz <> nil then
  begin
    write(Raiz^.Conteudo, '-');
    PreOrdem(Raiz^.ArvEsq);
    PreOrdem(Raiz^.ArvDir);
  end;
end;

procedure EmOrdem(Raiz: PtrNodoArvBin);
begin
  if Raiz <> nil then
  begin
    EmOrdem(Raiz^.ArvEsq);
    write(Raiz^.Conteudo, '-');
    EmOrdem(Raiz^.ArvDir);
  end;
end;

procedure PosOrdem(Raiz: PtrNodoArvBin);
begin
  if Raiz <> nil then
  begin
    PosOrdem(Raiz^.ArvEsq);
    PosOrdem(Raiz^.ArvDir);
    write(Raiz^.Conteudo, '-');
  end;
end;

procedure InicializaArvBin(var Raiz: PtrNodoArvBin);
begin
  Raiz := nil;
end;

function InsereArvBin(var Raiz: PtrNodoArvBin; X: Integer): Boolean;
var
  Atual, Pai, Novo: PtrNodoArvBin;
begin
  Atual := Raiz;
  Pai := nil;

  while Atual <> nil do
  begin
    Pai := Atual;

    if X = Atual^.Conteudo then
    begin
      InsereArvBin := False;
      Exit;
    end;

    if X < Atual^.Conteudo then
      Atual := Atual^.ArvEsq
    else
      Atual := Atual^.ArvDir;
  end;

  New(Novo);

  Novo^.Conteudo := X;
  Novo^.ArvEsq := nil;
  Novo^.ArvDir := nil;
  Novo^.Pai := Pai;

  if Pai = nil then
    Raiz := Novo
  else if X < Pai^.Conteudo then
    Pai^.ArvEsq := Novo
  else
    Pai^.ArvDir := Novo;

  InsereArvBin := True;
end;

procedure MostraNodosFolha(Raiz: PtrNodoArvBin);
begin
  if Raiz <> nil then
  begin
    if (Raiz^.ArvEsq = nil) and (Raiz^.ArvDir = nil) then
      write(Raiz^.Conteudo, '-');

    MostraNodosFolha(Raiz^.ArvEsq);
    MostraNodosFolha(Raiz^.ArvDir);
  end;
end;

procedure ApagaArvBin(Raiz: PtrNodoArvBin);
begin
  if Raiz <> nil then
  begin
    ApagaArvBin(Raiz^.ArvEsq);
    ApagaArvBin(Raiz^.ArvDir);
    Dispose(Raiz);
  end;
end;

procedure ContaNodos(Raiz: PtrNodoArvBin; var Cont: Integer);
begin
  if Raiz <> nil then
  begin
    Inc(Cont);
    ContaNodos(Raiz^.ArvEsq, Cont);
    ContaNodos(Raiz^.ArvDir, Cont);
  end;
end;

procedure SomaNodos(Raiz: PtrNodoArvBin; var Soma: Integer);
begin
  if Raiz <> nil then
  begin
    Soma := Soma + Raiz^.Conteudo;
    SomaNodos(Raiz^.ArvEsq, Soma);
    SomaNodos(Raiz^.ArvDir, Soma);
  end;
end;

function PesquisaArvBinPesq(
  Raiz: PtrNodoArvBin;
  X: Integer
): PtrNodoArvBin;
var
  Ptr: PtrNodoArvBin;
begin
  Ptr := Raiz;

  while (Ptr <> nil) and (Ptr^.Conteudo <> X) do
  begin
    if X > Ptr^.Conteudo then
      Ptr := Ptr^.ArvDir
    else
      Ptr := Ptr^.ArvEsq;
  end;

  PesquisaArvBinPesq := Ptr;
end;

function MenorValor(Raiz: PtrNodoArvBin): PtrNodoArvBin;
begin
  if Raiz^.ArvEsq <> nil then
    MenorValor := MenorValor(Raiz^.ArvEsq)
  else
    MenorValor := Raiz;
end;

function MaiorValor(Raiz: PtrNodoArvBin): PtrNodoArvBin;
begin
  if Raiz^.ArvDir <> nil then
    MaiorValor := MaiorValor(Raiz^.ArvDir)
  else
    MaiorValor := Raiz;
end;

function Altura(Raiz: PtrNodoArvBin): Integer;
begin
  if Raiz = nil then
    Altura := -1
  else
    Altura := 1 + Maior(
      Altura(Raiz^.ArvEsq),
      Altura(Raiz^.ArvDir)
    );
end;

procedure MostraArvore(
  Raiz: PtrNodoArvBin;
  Lin, Col, ColAnterior: Integer
);
begin
  if Raiz <> nil then
  begin
    MostraArvore(
      Raiz^.ArvEsq,
      Lin + 1,
      Col - Abs(ColAnterior - Col) div 2,
      Col
    );

    GoToXY(Col, Lin);
    write(Raiz^.Conteudo);

    MostraArvore(
      Raiz^.ArvDir,
      Lin + 1,
      Col + Abs(ColAnterior - Col) div 2,
      Col
    );
  end;
end;

function MaiorCaminho(Raiz: PtrNodoArvBin): String;
begin
  if Raiz = nil then
    MaiorCaminho := ''
  else if Altura(Raiz) = 0 then
    MaiorCaminho := ''
  else if Altura(Raiz^.ArvEsq) > Altura(Raiz^.ArvDir) then
    MaiorCaminho := 'E' + MaiorCaminho(Raiz^.ArvEsq)
  else
    MaiorCaminho := 'D' + MaiorCaminho(Raiz^.ArvDir);
end;

procedure Pausar;
begin
  Writeln;
  Write('Pressione Enter para continuar...');
  ReadLn;
end;

procedure ExecutaInsercao(var Raiz: PtrNodoArvBin);
var
  Valor: Integer;
begin
  Writeln;
  Write('Digite o valor a inserir: ');
  ReadLn(Valor);

  if InsereArvBin(Raiz, Valor) then
    Writeln('Valor ', Valor, ' inserido com sucesso.')
  else
    Writeln('O valor ', Valor, ' ja existe na arvore.');

  Pausar;
end;

procedure ExecutaPreOrdem(Raiz: PtrNodoArvBin);
begin
  Writeln;
  Writeln('Percurso em pre-ordem:');

  if Raiz = nil then
    Writeln('Arvore vazia.')
  else
  begin
    PreOrdem(Raiz);
    Writeln;
  end;

  Pausar;
end;

procedure ExecutaEmOrdem(Raiz: PtrNodoArvBin);
begin
  Writeln;
  Writeln('Percurso em ordem:');

  if Raiz = nil then
    Writeln('Arvore vazia.')
  else
  begin
    EmOrdem(Raiz);
    Writeln;
  end;

  Pausar;
end;

procedure ExecutaPosOrdem(Raiz: PtrNodoArvBin);
begin
  Writeln;
  Writeln('Percurso em pos-ordem:');

  if Raiz = nil then
    Writeln('Arvore vazia.')
  else
  begin
    PosOrdem(Raiz);
    Writeln;
  end;

  Pausar;
end;

procedure NaoImplementado;
begin
  Writeln;
  Writeln('Funcionalidade ainda nao implementada.');
  Pausar;
end;

procedure ExibeMenu;
begin
  Writeln('===================================');
  Writeln('       ARVORE BINARIA DE BUSCA');
  Writeln('===================================');
  Writeln('1  - Inserir no');
  Writeln('2  - Excluir no');
  Writeln('3  - Verificar se elemento pertence');
  Writeln('4  - Percorrer em pre-ordem');
  Writeln('5  - Percorrer em ordem');
  Writeln('6  - Percorrer em pos-ordem');
  Writeln('7  - Mostrar folhas');
  Writeln('8  - Verificar altura');
  Writeln('9  - Verificar nivel de elemento');
  Writeln('10 - Verificar se arvore e completa');
  Writeln('0  - Sair');
  Writeln('===================================');
  Write('Opcao: ');
end;

var
  Raiz: PtrNodoArvBin;
  Opcao: Integer;

begin
  InicializaArvBin(Raiz);

  repeat
    ClrScr;
    ExibeMenu;
    ReadLn(Opcao);

    case Opcao of
      1:
        ExecutaInsercao(Raiz);

      2..3:
        NaoImplementado;

      4:
        ExecutaPreOrdem(Raiz);

      5:
        ExecutaEmOrdem(Raiz);

      6:
        ExecutaPosOrdem(Raiz);

      7..10:
        NaoImplementado;

      0:
        begin
          Writeln;
          Writeln('Encerrando...');
        end;

    else
      begin
        Writeln;
        Writeln('Opcao invalida.');
        Pausar;
      end;
    end;

  until Opcao = 0;

  ApagaArvBin(Raiz);

  Halt(0);
end.