export class Exame {
    constructor(respostasCorretas, pesos) {
      this.respostasCorretas = respostasCorretas;
      this.pesos = pesos;
      this.listaExames = [];
    }
  
    adicionarExame(respostasAluno) {
      let nota = 0;
      for (let questao in respostasAluno) {
        if (respostasAluno[questao] === this.respostasCorretas[questao]) {
          nota += this.pesos[questao];
        }
      }
      this.listaExames.push({ respostas: respostasAluno, nota });
    }
  
    calcularMedia() {
      if (this.listaExames.length === 0) return 0;
      const somaNotas = this.listaExames.reduce((soma, exame) => soma + exame.nota, 0);
      return somaNotas / this.listaExames.length;
    }
  
    menorNota(qtd = 1) {
      const notas = this.listaExames.map((exame) => exame.nota);
      return notas.sort((a, b) => a - b).slice(0, qtd);
    }
  
    maiorNota(qtd = 1) {
      const notas = this.listaExames.map((exame) => exame.nota);
      return notas.sort((a, b) => b - a).slice(0, qtd);
    }
  
    notasAbaixoDe(limite) {
      return this.listaExames.filter((exame) => exame.nota < limite);
    }
  
    notasAcimaDe(limite) {
      return this.listaExames.filter((exame) => exame.nota > limite);
    }
  
    gerarRelatorio() {
      console.log("Relatório de Exames:");
      this.listaExames.forEach((exame, indice) => {
        console.log(`Exame ${indice + 1}: Nota ${exame.nota}`);
      });
      console.log(`Média Geral: ${this.calcularMedia()}`);
    }
  }
  