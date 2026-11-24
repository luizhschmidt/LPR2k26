using System;

class Produto
{
    public string nome;
    public double preco;
}

class Pedido
{
    public Produto produto;
    public int quantidade;

    public double CalcularTotal()
    {
        return produto.preco * quantidade;
    }
}

class Program
{
    static void Main()
    {
        Produto produto = new Produto();
        produto.nome = "Notebook";
        produto.preco = 2500;

        Pedido pedido = new Pedido();
        pedido.produto = produto;
        pedido.quantidade = 2;

        Console.WriteLine(pedido.produto.nome);
        Console.WriteLine(pedido.quantidade);
        Console.WriteLine(pedido.CalcularTotal());
    }
}