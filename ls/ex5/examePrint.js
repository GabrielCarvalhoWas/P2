import { Exame } from './Exame.js';

const respostasCorretas = { q1: "a", q2: "b", q3: "a", q4: "c", q5: "d" };
const pesos = { q1: 2, q2: 2, q3: 2, q4: 2, q5: 2 };

const exame = new Exame(respostasCorretas, pesos);

exame.adicionarExame({ q1: "a", q2: "b", q3: "b", q4: "b", q5: "b" });
exame.adicionarExame({ q1: "a", q2: "b", q3: "a", q4: "c", q5: "d" });

exame.gerarRelatorio();

console.log("Menor nota:", exame.menorNota());
console.log("Maior nota:", exame.maiorNota());
console.log("Notas abaixo de 6:", exame.notasAbaixoDe(6));
console.log("Notas acima de 4:", exame.notasAcimaDe(4));
