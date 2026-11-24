using System;
using System.Collections.Generic;

class Matricula
{
    public Aluno aluno;
    public Turma turma;
    public DateTime dataMatricula;

    public Matricula(Aluno aluno, Turma turma)
    {
        this.aluno = aluno;
        this.turma = turma;
        dataMatricula = DateTime.Now;
    }
}

class Aluno
{
    public string nome;

    public List<Matricula> matriculas = new List<Matricula>();

    public void AdicionarMatricula(Turma turma)
    {
        foreach (Matricula m in matriculas)
        {
            if (m.turma == turma)
            {
                Console.WriteLine("Aluno já matriculado!");
                return;
            }
        }

        Matricula matricula = new Matricula(this, turma);

        matriculas.Add(matricula);
        turma.AdicionarMatricula(matricula);
    }
}

class Turma
{
    public string nome;

    public List<Matricula> matriculas = new List<Matricula>();

    public void AdicionarMatricula(Matricula matricula)
    {
        matriculas.Add(matricula);
    }

    public List<Aluno> ListarAlunos()
    {
        List<Aluno> alunos = new List<Aluno>();

        foreach (Matricula m in matriculas)
        {
            alunos.Add(m.aluno);
        }

        return alunos;
    }
}

class Program
{
    static void Main()
    {
        Aluno aluno1 = new Aluno();
        aluno1.nome = "Luiz";

        Aluno aluno2 = new Aluno();
        aluno2.nome = "Pedro";

        Turma turma1 = new Turma();
        turma1.nome = "Programação";

        Turma turma2 = new Turma();
        turma2.nome = "Eletrônica";

        aluno1.AdicionarMatricula(turma1);
        aluno1.AdicionarMatricula(turma2);
        aluno2.AdicionarMatricula(turma1);

        // Teste de matrícula duplicada
        aluno1.AdicionarMatricula(turma1);

        Console.WriteLine(turma1.nome);

        foreach (Aluno aluno in turma1.ListarAlunos())
        {
            Console.WriteLine(aluno.nome);
        }
    }
}