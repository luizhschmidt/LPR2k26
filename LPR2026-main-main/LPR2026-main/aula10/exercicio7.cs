using System;
using System.Collections.Generic;

class Livro
{
    public string Titulo { get; set; }
    public string Autor { get; set; }
    public int AnoPublicacao { get; set; }

    public Livro(string titulo, string autor, int ano)
    {
        Titulo = titulo;
        Autor = autor;
        AnoPublicacao = ano;
    }
}

class Biblioteca
{
    public List<Livro> livros = new List<Livro>();

    public void AdicionarLivro(Livro livro)
    {
        livros.Add(livro);
    }

    public void ListarLivros()
    {
        foreach (Livro livro in livros)
        {
            Console.WriteLine(livro.Titulo);
            Console.WriteLine(livro.Autor);
            Console.WriteLine(livro.AnoPublicacao);
        }
    }
}

class Program
{
    static void Main()
    {
        Biblioteca biblioteca = new Biblioteca();

        Livro livro1 = new Livro("Vidas Secas",
                                "Graciliano Ramos", 1938);

        Livro livro2 = new Livro("Dom Casmurro",
                                "Machado de Assis", 1899);

        biblioteca.AdicionarLivro(livro1);
        biblioteca.AdicionarLivro(livro2);

        biblioteca.ListarLivros();
    }
}