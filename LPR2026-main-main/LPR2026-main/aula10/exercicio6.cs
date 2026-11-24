using System;
using System.Collections.Generic;

class Reserva
{
    public string descricao;
    public Cliente cliente;
}

class Cliente
{
    public string nome;
    public List<Reserva> reservas = new List<Reserva>();

    public void AdicionarReserva(Reserva reserva)
    {
        reserva.cliente = this;
        reservas.Add(reserva);
    }

    public void ListarReservas()
    {
        foreach (Reserva reserva in reservas)
        {
            Console.WriteLine(reserva.descricao);
        }
    }
}

class Program
{
    static void Main()
    {
        Cliente cliente = new Cliente();
        cliente.nome = "Luiz";

        Reserva reserva1 = new Reserva();
        reserva1.descricao = "Quarto 101";

        Reserva reserva2 = new Reserva();
        reserva2.descricao = "Quarto 202";

        cliente.AdicionarReserva(reserva1);
        cliente.AdicionarReserva(reserva2);

        Console.WriteLine(cliente.nome);
        cliente.ListarReservas();
    }
}