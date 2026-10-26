# BWT
## Trasformata di Burrows-Wheeler
### Consegna:

Parte 1:
Scrivere uno script in Python che, data una stringa in input, calcoli la sua trasformata di Burrows-Wheeler.

Parte 2:
Scrivere due script "client.py" e "server.py" che utilizzino dei socket TCP per lo scambio di informazioni. Il client invia una stringa al server; il server elabora la trasformata e la restituisce al client.

Parte 3: 
Scrivere la relazione tecnica.

### Come si calcola:
1. Avere una stringa `banana`, aggiungere un dollaro `banana$`
2. Calcolare tutti gli shift a sinistra:
   - `banana$`
   - `anana$b`
   - `nana$ba`
   - `ana$ban`
   - `na$bana`
   - `a$banan`
   - `$banana`
3. Riordinare in maniera lessico-grafica:
   - `banana$` - (f)
   - `anana$b` - (d)
   - `nana$ba` - (g)
   - `ana$ban` - (c)
   - `na$bana` - (e)
   - `a$banan` - (b)
   - `$banana` - (a)
4. Riorinare in una matrice:
   - `$banana` - (a)
   - `a$banan` - (b)
   - `ana$ban` - (c)
   - `anana$b` - (d)
   - `na$bana` - (e)
   - `banana$` - (f)
   - `nana$ba` - (g)
