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

var
  Raiz: PtrNodoArvBin;

begin
  InicializaArvBin(Raiz);

  Halt(0);
end.